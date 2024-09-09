import random
import sys
from pathlib import Path
from .dataset_descriptions import *

current_directory = Path(__file__).parent
parent_directory = current_directory.parent
sys.path.append(str(parent_directory))

from utils import *
import re
import json
import os





def get_indices(qbank, instance, num_options=4):
    '''  
    given the dataset (list of dicts), get the index of the target datapoint and options
    '''
    indices = list(range(len(qbank) - 1))
    prob_set = random.sample(indices, num_options) 
    tar_idx = instance["idx"] 
    gt_idx = tar_idx + 1 

    if tar_idx in prob_set:
        input_idx = prob_set.index(tar_idx)
    else:
        input_idx = 0
    
    prob_set[input_idx] = gt_idx

    option_idc = prob_set
    random.shuffle(option_idc)
    gt_location = option_idc.index(gt_idx)
    return tar_idx, option_idc, gt_location
    

def full_example_text(q, dataset = 'GSM8K'):
    
    # modify this to get example text for different datasets that is close to the original form on the internet
    if dataset == 'GSM8K':
        return q['question']
    else:
        return q['question']



def gen_p(qbank, instance, dataset, num_options=4): 
    
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'] # can be longer
    
    tar_idx, option_idc, gt_location = get_indices(qbank, instance, num_options) # e.g., (1234, [1235, 175, 430, 780], 0)
    
    tar_text = full_example_text(qbank[tar_idx], dataset)
    
    option_text = ''
    for letter, opt_idx in zip(letters[:len(option_idc)], option_idc):
        option_text += letter + ') ' + full_example_text(qbank[opt_idx], dataset) + '\n'
    
    gt_letter = letters[gt_location]
    
    return {'tar_text': tar_text, 'options':option_text, 'gt': gt_letter}

def parse_llm_output(text):
    patterns = [
        r'THE ANSWER IS OPTION\s*([A-Z])[\)\.]?',
        r'THE ANSWER IS\s*([A-Z])[\)\.]?',
        r'THE ANSWER IS\s*\(\s*([A-Z])\s*\)',
        r'THE ANSWER IS OPTION\s*\(\s*([A-Z])\s*\)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text.upper())
        if match:
            option = match.group(1)
            return option
    
    return "Answer format not found"

    
    
def order(dataset, num_options, split, model):
    res = []
    acc = 0

    

    description = get_description(dataset)

    # LOAD IN DATASET AND SPLIT CORRECTLY ----> FULL DATASETS
    sampled_qs = data_loader(f'../full_datasets/{dataset}/{split}.json')
    # print(len(sampled_qs))

    template = '''{Description_of_dataset}\nGiven the target data example in the {split} of the {dataset_name} dataset, Which of the following examples was next to it in the original order of the dataset? Exactly one of the choices must be selected and you need to output the answer in your final sentence like "The answer is ..."
    Target example: ```{tar_example}```
    
    Options: ```{options}```
    '''

    for instance in sampled_qs:
        # if "category" in instance:
        #     qb = data_loader(f'../full_datasets/{dataset}/{instance["category"]}.txt')
        # else:
        #     qb = data_loader(f'../full_datasets/{dataset}/{split}.txt')

        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

        list_of_examples = sampled_qs[instance][:5]
        example = list_of_examples[0]["question"]
        gt = list_of_examples[1]

        list_of_examples = list_of_examples[1:]
        random.shuffle(list_of_examples)
        gt_location = list_of_examples.index(gt)

        option_text = ''
        # for letter, opt_idx in zip(letters[:len(list_of_examples)], list_of_examples):
        for opt_idx in range(len(list_of_examples)):
            letter = letters[opt_idx]

            option_text += letter + ') ' + list_of_examples[opt_idx]["question"] + '\n'
        
        the_gt = letters[gt_location]




        prompt = template.format(Description_of_dataset = description,
                            split = f'{split} set',
                            dataset_name = dataset,
                            tar_example = example,
                            options = option_text)



        
        raw_output = run_model(prompt, model_card=model, temperature=0)   


        pred = parse_llm_output(raw_output)



        if len(pred) == 3:
            if pred[1] == the_gt:
                acc += 1
        
        elif len(pred) < 3:
            if pred[0] == the_gt:
                acc += 1
        

        inp = {
            "example": example,
            "dataset": dataset,
            "ground_truth": the_gt,
            "raw_output": raw_output,
        }


        res.append(inp)
        print(f'Done with {len(res)}/{len(sampled_qs)} for dataset {dataset}')

    
    acc /= 100
    
    return res, acc





    