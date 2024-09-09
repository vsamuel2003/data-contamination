import os
from utils import *
import re

# Specify the main directory path
main_directory = '../results/order'

def parse_llm_output(text):
    pattern = r"The answer is ([A-Z]\))"
    match = re.search(pattern, text)
    
    if match:
        # Return the found option
        return match.group(1)
    else:
        return "Answer format not found"

def score(path):
    data = data_loader(path)
    acc = 0
    for instance in data:
        raw_output = instance["raw_output"]
        gt = instance["ground_truth"]
        pred = parse_llm_output(raw_output)
        if pred[0] == gt:
            acc += 1
    
    acc /= len(data)
    return acc


for model in os.listdir(main_directory):
    model_path = os.path.join(main_directory, model)
    print("------------------------------------------")
    print(f'model {model}')
    if os.path.isdir(model_path):
        for dataset in os.listdir(model_path):
            dataset_path = os.path.join(model_path, dataset)
            if os.path.isdir(dataset_path):
                for filename in os.listdir(dataset_path):
                    file_path = os.path.join(dataset_path, filename)
                    if os.path.isfile(file_path):
                        split = filename.split(".")[0]

                        acc = score(file_path)

                        
                        print(f'Accuracy for {split} set in {dataset} is {acc}')
                        
