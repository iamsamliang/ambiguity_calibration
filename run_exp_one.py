import numpy as np
import time
import os
import sys
import openai

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

# from https://github.com/tonyzhaozh/few-shot-learning/blob/main/utils.py
def complete(prompt, l, model_name, temp=0, num_log_probs=None, echo=False, n=None):
    with open(os.path.join(ROOT_DIR, 'openai_key.txt'), 'r') as f:
        key = f.readline().strip()
        openai.api_key = key

    # call GPT-3 API until result is provided and then return it
    response = None
    received = False
    while not received:
        try:
            response = openai.Completion.create(model=model_name, prompt=prompt, max_tokens=l, temperature=temp, n=n,
                                                logprobs=num_log_probs, echo=echo, stop='\n')
            received = True
        except:
            error = sys.exc_info()[0]
            if error == openai.error.InvalidRequestError:  # something is wrong: e.g. prompt too long
                print(
                    f"InvalidRequestError\nPrompt passed in:\n\n{prompt}\n\n")
                assert False

            print("API error:", error)
            time.sleep(1)
    return response

def generate_prompt():
    return

def main():
    model_name = "davinci"
    prompt = generate_prompt()
    respones = complete(...)
