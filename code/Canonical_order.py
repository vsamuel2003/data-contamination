import os

import math
import random 

import numpy as np 
from scipy.stats import binom
from scipy.stats import t as tdist
from tqdm import tqdm

import json
from utils import *
import time
import pickle

MODEL = "finetuned_model_name"

flatten = lambda l : [x for s in l for x in s]
shuffle = lambda l : random.sample(l, k=len(l))

def llama_chat_gen(text, model_card="finetuned-model-name"):
    client = Together(api_key=LLAMA_API_KEY)
    message=[{"role": "user", "content": text}]
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

def load_logprobs(file_path, num_shards, type="canonical"):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            log_probs = pickle.load(file)
    elif type == "canonical":
        log_probs = [None for _ in range(num_shards)]
    else:
        log_probs = [[] for _ in range(num_shards)]

    
    return log_probs

def load_dataset(dataset_path):
    if dataset_path.endswith(".json"):
        print("loading from json...")
        with open(dataset_path, "r") as f:
            examples = json.load(f)
            return examples

    with open(dataset_path, "r") as f:
        lines = f.readlines()
    return lines

def get_logprob(shard):

    shard_str = "\n".join(shard)
    log_probs = llama_chat_gen(shard_str, model_card=MODEL)
    logp_sum = sum(log_probs[1:])
    return logp_sum


def main(dataset_path,
         num_shards=10,
         permutations_per_shard=25,
         random_seed=0,
         log_file_path=None,
         max_examples=100,
         dataset = None,
         split = None):

    # Set random seed(s).
    random.seed(random_seed)
    np.random.seed(random_seed)

    # Load the dataset.
    examples = load_dataset(dataset_path)
    examples = examples[:max_examples]
    num_examples = len(examples)
    print(f"Loaded {num_examples} examples from {dataset_path}")
    
    # Compute the number of examples for each shard.
    shard_counts = [(x + 1 if i < num_examples % num_shards else x) 
       for i, x in enumerate([num_examples // num_shards] * num_shards)]
    shard_counts = np.asarray(shard_counts)

    # Compute the starting index (into the list of examples) for each shard.
    shard_example_indices = [0] + np.cumsum(shard_counts).tolist()
    shards = []


    
    for i, (start, end) in enumerate(zip(shard_example_indices, shard_example_indices[1:])):

        shard = examples[start:end]
        shards.append(shard)



    canonical_logprobs = load_logprobs(f'../canonical/shard_results/{dataset}_{split}_canonical.pkl', num_shards)
    shuffled_logprobs  = load_logprobs(f'../canonical/shard_results/{dataset}_{split}_shuffle.pkl', num_shards, "shuffled")
    empty_list_count = sum(1 for lst in shuffled_logprobs if lst == [])

    for i in range(len(canonical_logprobs) - 1, len(canonical_logprobs) - 1 - empty_list_count, -1):
        canonical_logprobs[i] = None



    offset = len(shards) - sum(x is None for x in canonical_logprobs)

    

    for i in range(offset, len(shards)):
        shard = shards[i]
        canonical_logprob = get_logprob(shard)
        canonical_logprobs[i] = canonical_logprob

        with open(f'../canonical/shard_results/{dataset}_{split}_canonical.pkl', 'wb') as file:
            pickle.dump(canonical_logprobs, file)

        for _ in range(permutations_per_shard):
            perm_shard = shuffle(shard)
            perm_logprob = get_logprob(perm_shard)
            shuffled_logprobs[i].append(perm_logprob)
        
        print(f'Done with shard {i + 1}/{len(shards)}')
        with open(f'../canonical/shard_results/{dataset}_{split}_shuffle.pkl', 'wb') as file:
            pickle.dump(shuffled_logprobs, file)

    

    # Calculate p-value. ----------> just need to get log probs for canonical and shuffled at this point
    canonical_logprobs = np.asarray(canonical_logprobs)
    shuffled_logprobs  = np.asarray(shuffled_logprobs)
    
    # T-test.
    diffs = canonical_logprobs - shuffled_logprobs.mean(axis=1)
    z = np.mean(diffs) / np.std(diffs) * np.sqrt(len(diffs))
    pval = 1 - tdist.cdf(z, df=len(diffs)-1)
    print(f"{pval=}")

    # Log.
    if log_file_path is not None:
        print(f"Writing logprobs to: {log_file_path}")
        with open(f"{log_file_path}", 'w') as f:
            f.write(json.dumps({
                'pval': pval, 
                'permutations_per_shard': permutations_per_shard,
                'num_shards': num_shards,
                'canonical_logprobs': canonical_logprobs.tolist(),
                'shuffled_logprobs': shuffled_logprobs.tolist(),
            }))



directory = "../canonical/datasets"
for item in os.listdir(directory):
    if item not in ["MMLU", "DROP", "ARC-Challenge", "BIG-Bench-Hard", "HumanEval", "GSM8K"]:
        continue
    item_path = os.path.join(directory, item)
    if os.path.isdir(item_path):
        for filename in os.listdir(item_path):
            if filename.endswith('.jsonl'):
                file_path = os.path.join(item_path, filename)
                log_path = f'../canonical/logs/{item}_oracle_{filename.split(".")[0]}.json'
                if os.path.exists(log_path):
                    continue
                try:
                    main(file_path, log_file_path = log_path, dataset = item, split = filename.split(".")[0], max_examples=100)
                except Exception as e:
                    continue



