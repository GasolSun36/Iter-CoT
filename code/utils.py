
import json
import requests

def lora_gpt3(prompt, n=1, model='', response_length=500, temperature=0, top_p=1, frequency_penalty=0,
              presence_penalty=0, start_text='', restart_text='', stop_seq=[], api_key='', **kwargs):
    model = "Your Base Large Language Models"
    api_key = "Your own API keys"
    headers = {'Content-Type': 'application/json', 'Openai-Internal-ResampleUnstableTokens': 'true',
               'ocp-apim-subscription-key': api_key, 'Authorization': ('Bearer ' + api_key)}
    input_str = dict()
    input_str['prompt'] = prompt
    input_str['temperature'] = temperature
    input_str['top_p'] = top_p
    input_str['max_tokens'] = response_length
    input_str['n'] = n
    input_str.update(**kwargs)
    input_prompt = json.dumps(input_str)
    response = requests.post(model, data=input_prompt, headers=headers)
    return response