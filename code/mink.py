import logging
logging.basicConfig(level='ERROR')
import numpy as np
from pathlib import Path
from tqdm import tqdm
import numpy as np

import sys
from pathlib import Path

current_directory = Path(__file__).parent
parent_directory = current_directory.parent
sys.path.append(str(parent_directory))

from utils import *
MODEL = "meta-llama/Llama-3-70b-chat-hf"


def log_probs(text):
    client = Together(api_key=LLAMA_API_KEY)
    message=[{"role": "user", "content": text}]
    model_card = MODEL
    temperature = 1.0
    max_tokens = 1
    retries = 2

    while retries > 0:
        try:
            response = client.chat.completions.create(
                        model= model_card,
                        messages = message,
                        temperature=temperature,
                        max_tokens=max_tokens,
                        logprobs=1,
                        echo=True
                    )
            return response.prompt[0].logprobs.token_logprobs
        except Exception as e:
            retries -= 1
    
    return []


def inference(text, ex):

    all_prob = log_probs(text)
    if len(all_prob) == 0:
        return []
    
    all_prob = all_prob[4:-4]

    ratio = 0.2
    k_length = int(len(all_prob)*ratio)
    topk_prob = np.sort(all_prob)[:k_length]
    return -np.mean(topk_prob).item()


def evaluate_data(test_data, col_name):
    print(f"all data size: {len(test_data)}")
    all_output = []
    test_data = test_data
    for ex in tqdm(test_data): 
        text = ex[col_name]
        text = text.replace("Passage:", "").strip()
        text = text.replace("Question:", "").strip()

        new_ex = inference(text, ex)
        if new_ex == []:
            continue

        all_output.append(new_ex)
    
    all_output = np.array(all_output)
    mean = np.mean(all_output)
    std = np.std(all_output)

    return all_output, mean, std


def mink(dataset, split):
    data = data_loader(f"{dataset}/{split}.txt")
    
    _, mean, std = evaluate_data(data,"question")

    print(f'Mean: {mean}, STD: {std} for {split} set in {dataset}')
    print()


datasets = ["MMLU", "DROP", "AGNews", "IMDB", "ARC-Challenge", "BIG-Bench-Hard", "HumanEval", "GSM8K"]
data_dir = "../datasets"
for dataset in datasets:
    directory = f'{data_dir}/{dataset}'

    for file in os.listdir(directory):
        if ".txt" not in file:
            continue
        split = file.split(".")[0]

        if split == "dev":
            continue
        mink(dataset, split)


