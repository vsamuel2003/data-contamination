import sys
from pathlib import Path
from .perturbation_prompts import pertubation_prompts


current_directory = Path(__file__).parent
parent_directory = current_directory.parent
sys.path.append(str(parent_directory))

from utils import *
import random
import ast
import re

def load_data(dataset, split):
    path = f'{dataset}/{split}.txt'
    return data_loader(path)

def process_humaneval(perturb):
    res = []
    cleaned_data = perturb.strip('[""]')
    functions = re.split(r'""",\s*"""', cleaned_data)

    for func in functions:
        res.append(func)

    return res 

def split_options(text):
    import re
    # Pattern to find the start of each option
    pattern = r"Option \d+ -"
    
    # Find all matches of the pattern
    matches = list(re.finditer(pattern, text))
    
    # Split the text into options based on these matches
    options = []
    for i in range(len(matches)):
        # Start the text right after the match ends to exclude the marker
        start_index = matches[i].end()
        
        # If it's not the last match, the end index is the start of the next match
        if i < len(matches) - 1:
            end_index = matches[i + 1].start()
            options.append(text[start_index:end_index].strip())
        else:
            # If it's the last match, the option continues to the end of the text
            options.append(text[start_index:].strip())
    
    return options

def perturb_drop(dataset, instance, model):
    perturb_prompt = pertubation_prompts[dataset].format(instance = instance)
    perturb = None

    for _ in range(5):
        perturb = run_model(perturb_prompt, model_card=model)
        perturb = split_options(perturb)

        if len(perturb) == 4:
            break
    
    return perturb


def perturb_humaneval(dataset, instance, model):
    delim = '\"\"\"' if '\"\"\"' in instance else "'''"
    parts = instance.split(delim)
    for i in range(1, len(parts), 2):
        parts[i] = delim + parts[i] + delim

  
    if len(parts) <= 3:
        docstring = parts[1]
        func_definition = parts[0]
        ending = parts[2] if len(parts) == 3 else None

    else:
        if parts[-1] == "\n":
            docstring = parts[-2]
            func_definition = "".join(parts[:-2])
            ending = parts[-1] 
        else:
            docstring = parts[-1]
            func_definition = "".join(parts[:-1])
            ending = None
    res = []

    docstring = docstring.split(delim)[1]
    perturb_prompt = pertubation_prompts[dataset].format(instance = docstring)
    perturb = run_model(perturb_prompt, model_card=model)
    perturb = split_options(perturb)
    
    
    for string in perturb:
        if ending:
            res.append(f'{func_definition}{delim}{string}{delim}{ending}')
        else:
            res.append(f'{func_definition}{delim}{string}{delim}')
    
    return res

def perturb_mmlu(dataset, instance, model):
    if "\n(A)" in instance:
        instance = instance.split("\n(A)")[0]
    elif "\nA." in instance:
        instance = instance.split("\nA.")[0]

    

    perturb_prompt = pertubation_prompts[dataset].format(instance = instance)
    perturb = run_model(perturb_prompt, model_card=model)
    perturb = split_options(perturb)
    
    return perturb

def perturb_bbh(dataset, instance, model):
    if "\nOptions:" in instance:
        temp_instance = instance.split("\nOptions:")[0]
        options = instance.split("\nOptions:")[1]
    else:
        temp_instance = instance
        options = None

    
    perturb_prompt = pertubation_prompts[dataset].format(instance = instance)
    perturb = run_model(perturb_prompt, model_card=model)
    perturb = split_options(perturb)

    # if options:
    #     for i in range(len(perturb)):
    #         perturb[i] = perturb[i] + "\nOptions:" + options
    
    return perturb


def perturb_instance(dataset, instance, model):
    if dataset == "DROP":
        perturb = perturb_drop(dataset, instance, model)
    elif dataset == "HumanEval":
        perturb = perturb_humaneval(dataset, instance, model)
    elif dataset == "BIG-Bench-Hard":
        perturb = perturb_bbh(dataset, instance, model)
    elif dataset in ["MMLU", "AGNews", "IMDB", "ARC-Challenge", "GSM8K"]:
        perturb = perturb_mmlu(dataset, instance, model)

    
    return perturb


def get_choices(options):
    res = {}
    for i in range(len(options)):
        choice = f"({chr(ord('A') + i)})"
        res[choice] = options[i]
    
    return res



def parse_llm_output(output):
    if len(output) == 1:
        return f'({output})'
    
    pattern = r'correct answer is \((.*?)\)'
    match = re.search(pattern, output)
    if match:
        option = match.group(1)
        return "(" + option + ")"
    
    match = re.search(r'\([A-Z]\)', output)
    return match.group(0) if match else None


def get_corr_choice(choices):
    valid_keys = [key for key, value in choices.items() if 'None of the provided options' not in value]
    random_key = random.choice(valid_keys) if valid_keys else None
    return random_key


def standard_quiz(dataset, split, choices, model):
    prompt = f'''
            Instruction: You are provided with a five-choice quiz. Your task is to correctly select the option that exactly corresponds to an instance from the {split} split of the {dataset} dataset.

            When selecting the option, you must ensure that you follow the following rules:
            (1) You must ensure that you only generate a single option letter as your answer.
            (2) If you do not know the dataset or the correct answer, you must select option "(E) None of the provided options."
            (3) You must output the answer in your final sentence like "The correct answer is ..."

            Hint: While all the following options seem similar in terms of meaning, there is only one option that reflects the exact wording with respect to the original instance.
            ---
            (A) {choices["(A)"]}
            (B) {choices["(B)"]}
            (C) {choices["(C)"]}
            (D) {choices["(D)"]}
            (E) {choices["(E)"]}
            ---
            Answer:
            '''

    
    output = run_model(prompt, model_card=model, temperature=0)

    pred = parse_llm_output(output)

    


    return pred

def dca(dataset, split, model):
    
    data = load_data(dataset, split)
    acc = 0
    result = {"outputs":[]}

    for idx, instance in enumerate(data):

        question = instance["question"]
        label = instance["label"] if "label" in instance else None

        for _ in range(5):
            pertubed_options = perturb_instance(dataset, question, "meta-llama/Llama-3-70b-chat-hf")

            if len(pertubed_options) == 4:
                break


        if len(pertubed_options) != 4:
            print(f'FAILED on idx {idx}')
            continue


        if label:
            question = f'{question}\n{label}'
            for i in range(len(pertubed_options)):
                pertubed_options[i] = f'{pertubed_options[i]}\n{label}'
        
        pertubed_options.append("None of the provided options.")

        
        choices = get_choices(pertubed_options)

        corr_option = get_corr_choice(choices)
        choices[corr_option] = question
        prediction = standard_quiz(dataset, split, choices, model)



        if prediction and prediction == corr_option:
            acc += 1
        
        res = {
            "ground_truth": question,
            "corr_choice": corr_option,
            "choices": choices,
            "prediction": prediction
        }
        result["outputs"].append(res)

        print(f'Done with {idx}/{len(data)} for {split} in {dataset}')
    
    acc /= len(data)
    result["acc"] = acc
    return result, acc




