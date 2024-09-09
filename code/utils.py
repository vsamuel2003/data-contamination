#import openai
import time
from openai import OpenAI
from together import Together
import anthropic
import os
import json

OPENAI_API_KEY = 'OPENAI_KEY'
CLAUDE_API_KEY = 'CLAUDE_KEY'
LLAMA_API_KEY = 'TOGETHERAI_KEY'


def run_model(
                    input_prompt,
                    model_card = 'gpt-3.5-turbo',
                    temperature = 0.9, 
                    top_p = 0.9,
                    max_tokens = 4000,
                ):
    if "gpt" in model_card:
        return openai_chat_gen(input_prompt, model_card=model_card, temperature=temperature, top_p=top_p, max_tokens=max_tokens)
    elif "claude" in model_card:
        return claude_chat_gen(input_prompt, model_card=model_card, temperature=temperature, top_p=top_p, max_tokens=max_tokens)
    else:
        return llama_chat_gen(input_prompt, model_card=model_card, temperature=temperature, top_p=top_p, max_tokens=max_tokens)

def openai_chat_gen(input_prompt,
                    apikey = OPENAI_API_KEY,
                    model_card = 'gpt-3.5-turbo',
                    temperature = 0.3, 
                    top_p = 0.9,
                    max_tokens = 4000,
                    max_attempt = 3,
                    time_interval = 0.005
                   ):

    assert (type(input_prompt) == str
            ), "openai api does not support batch inference."

  
    client = OpenAI(api_key=apikey)
    
    message=[{"role": "user", "content": input_prompt}]
    
    while max_attempt > 0:

        try:
            response = client.chat.completions.create(
                model= model_card,
                messages = message,
                temperature=temperature,
                top_p = top_p,
                max_tokens=max_tokens,
                frequency_penalty=0,
                presence_penalty=0,
                stop=None,
            )
            return response.choices[0].message.content

        except Exception as e:

            print('Exception Raised: ', e)

            max_attempt -= 1
            time.sleep(time_interval)

            print('Retrying left: ', max_attempt)

    return 'Error'

def claude_chat_gen(input_prompt,
                    apikey = CLAUDE_API_KEY,
                    model_card = 'claude-3-haiku-20240307',
                    temperature = 0.9, 
                    top_p = 0.9,
                    max_tokens = 4000,
                    max_attempt = 6,
                    time_interval = 10
                   ):
    

    assert (type(input_prompt) == str
            ), "claude api does not support batch inference."

    client = anthropic.Anthropic(api_key=apikey)
    
    message=[{"role": "user", "content": input_prompt}]
    
    while max_attempt > 0:

        try:
            response = client.messages.create(
                model= model_card,
                messages = message,
                temperature=temperature,
                top_p = top_p,
                max_tokens=max_tokens,
            )
            return response.content[0].text

        except Exception as e:

            print('Exception Raised: ', e)

            max_attempt -= 1
            time.sleep(time_interval)

            print('Retrying left: ', max_attempt)

    return 'Error'


def llama_chat_gen(input_prompt,
                    apikey = LLAMA_API_KEY,
                    model_card = 'meta-llama/Meta-Llama-3-70B',
                    temperature = 0.9, 
                    top_p = 0.9,
                    max_tokens = 4000,
                    max_attempt = 3,
                    time_interval = 0.005
                   ):

    assert (type(input_prompt) == str
            ), "openai api does not support batch inference."

  
    client = Together(api_key=apikey)
    
    message=[{"role": "user", "content": input_prompt}]
    # message=[{"role": "system", "content": "You are a knowledgeable assistant with expertise in reasoning tasks. You will provide detailed, evidence-based, step-by-step solutions while avoiding unsubstantiated assumptions."},
    #          {"role": "user", "content": input_prompt}]
    
    while max_attempt > 0:

        try:
            response = client.chat.completions.create(
                model= model_card,
                messages = message,
                temperature=temperature,
                top_p = top_p,
            )
            return response.choices[0].message.content

        except Exception as e:

            print('Exception Raised: ', e)

            max_attempt -= 1
            time.sleep(time_interval)

            print('Retrying left: ', max_attempt)

    return 'Error'

def data_loader(rel_fp, print_info=False, full=False):

    if full:
        abspath = os.path.abspath('').rstrip('/code') + f'/full_datasets/{rel_fp}'
    else:
        abspath = os.path.abspath('').rstrip('/code') + f'/datasets/{rel_fp}'
    

    with open(abspath) as file:
        qb = json.load(file)


    if print_info:

        print('Example:')
        for k, v in qb[0].items():
            print(f'{k} -> {v}')
            print('-' * 40)
        print('=' * 40)
    return qb


