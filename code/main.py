import os
import json

from WPQ import *
from WPQ.dca import *
from Token_Overlap import *
from Local_Order_Quiz import *
from Local_Order_Quiz.pilot_asking_order import *
# from DataOrder.rerun_drop import *

def get_model_name(model):
    if "gpt" in model:
        return "gpt_4"
    elif "sonnet" in model:
        return "claude_sonnet"
    elif "oracle" in model:
        return "oracle"
    elif "Llama-3" in model:
        return "llama_3"
    elif "Llama-2" in model:
        return "llama_2"
    

def run_dca(datasets, model, data_dir, save_dir):
    for dataset in datasets:
        directory = f'{data_dir}/{dataset}'

        for file in os.listdir(directory):
            if ".txt" not in file:
                continue

            split = file.split(".")[0]
            if split == "dev":
                continue

            result, acc = dca(dataset, split, model)
            model_name = get_model_name(model)
            file_path = f'{save_dir}/pertubation/{model_name}/{dataset}'
            if not os.path.exists(file_path):
                os.makedirs(file_path)

            with open(f'{file_path}/{split}.json', 'w') as file:
                json.dump(result, file, indent=4)


def run_order(datasets, model, data_dir, save_dir, num_options=4):
    for dataset in datasets:
        directory = f'{data_dir}/{dataset}'

        for file in os.listdir(directory):
            if ".json" not in file:
                continue

            split = file.split(".")[0]
            if split == "dev":
                continue

            result, acc = order(dataset, num_options, split, model)
            model_name = get_model_name(model)

            file_path = f'{save_dir}/order/{model_name}/{dataset}'
            if not os.path.exists(file_path):
                os.makedirs(file_path)

            with open(f'{file_path}/{split}.json', 'w') as file:
                json.dump(result, file, indent=4)



def main():
    data_dir = "../full_datasets"
    save_dir = "../results"

    datasets = ["MMLU", "DROP", "AGNews", "IMDB", "ARC-Challenge", "BIG-Bench-Hard", "HumanEval", "GSM8K"]
    models = ["gpt-4","claude-3-sonnet-20240229", "meta-llama/Llama-3-70b-chat-hf", "meta-llama/Llama-2-70b-chat-hf"]

    for model in models:
        run_dca(datasets, model, data_dir, save_dir)
        run_order(datasets, model, data_dir, save_dir) 

main()