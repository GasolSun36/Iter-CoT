
import json
import requests
from iter_cot_few_shot import *


def gpt(prompt, n=1, model='', response_length=500, temperature=0, top_p=1, frequency_penalty=0,
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


def decoder_for_gpt(input, max_length):
    response = gpt(input, response_length=max_length)
    response = response.json()
    return response["choices"][0]["text"]


def read_dataset(args):
    if args.dataset == "aqua":
        args.dataset_path = "../dataset/aqua/test.json"
        args.output_path = "../output/aqua.txt"
        args.strong_few_shot = few_shot_4_aqua_strong
        args.weak_few_shot = few_shot_4_aqua_weak
    elif args.dataset == "gsm8k":
        args.dataset_path = "../dataset/gsm8k/test.jsonl"
        args.output_path = "../output/gsm8k.txt"
        args.strong_few_shot = few_shot_4_gsm8k_strong
        args.weak_few_shot = few_shot_4_gsm8k_weak
    elif args.dataset == "commonsenseqa":
        args.dataset_path = "../dataset/commonsenseqa/test.jsonl"
        args.output_path = "../output/commonsenseqa.txt"
        args.strong_few_shot = few_shot_4_commonsense_strong
        args.weak_few_shot = few_shot_4_commonsenseqa_weak
    elif args.dataset == "addsub":
        args.dataset_path = "../dataset/addsub/AddSub.json"
        args.output_path = "../output/addsub.txt"
        args.strong_few_shot = few_shot_4_gsm8k_strong
        args.weak_few_shot = few_shot_4_gsm8k_weak
    elif args.dataset == "strategyqa":
        args.dataset_path = "../dataset/strategyqa/train.json"
        args.output_path = "../output/strategyqa.txt"
        args.weak_few_shot = few_shot_4_strategyqa_weak
        # no strong_few_shot for strategyqa
    elif args.dataset == "svamp":
        args.dataset_path = "../dataset/svamp/SVAMP.json"
        args.output_path = "../output/svamp.txt"
        args.strong_few_shot = few_shot_4_gsm8k_strong
        args.weak_few_shot = few_shot_4_gsm8k_weak
    elif args.dataset == "asdiv":
        args.dataset_path = "../dataset/asdiv/asdiv.json"
        args.output_path = "../output/asdiv.txt"
        args.strong_few_shot = few_shot_4_gsm8k_strong
        args.weak_few_shot = few_shot_4_gsm8k_weak
    elif args.dataset == "singleeq":
        args.dataset_path = "../dataset/singleeq/questions.json"
        args.output_path = "../output/singleeq.txt"
        args.strong_few_shot = few_shot_4_gsm8k_strong
        args.weak_few_shot = few_shot_4_gsm8k_weak
    elif args.dataset == "date":
        args.dataset_path = "../dataset/date/test.json"
        args.output_path = "../output/date.txt"
        args.strong_few_shot = few_shot_4_date_strong
        args.weak_few_shot = few_shot_4_date_weak
    elif args.dataset == "object_tracking":
        args.dataset_path = "../dataset/object_tracking/test.json"
        args.output_path = "../output/object_tracking.txt"
        args.strong_few_shot = few_shot_4_object_strong
        args.weak_few_shot = few_shot_4_object_weak
    elif args.dataset == "letter":
        args.dataset_path = "../dataset/lastletter/last_letters.json"
        args.output_path = "../output/lastletter.txt"
        args.strong_few_shot = few_shot_4_lastletter_strong
        args.weak_few_shot = few_shot_4_lastletter_weak
    else:
        raise ValueError("dataset is not properly defined ...")
    return args


def process4evaluate(args):
    golden = []
    re_pattern_pre = ""
    re_pattern_post = ""
    if args.dataset == "aqua":
        with open("../data/aqua/test.json", 'r', encoding='utf-8') as f:
            lines = f.readlines()
        decoder = json.JSONDecoder()
        for line in lines:
            json_res = decoder.raw_decode(line)[0]
            golden.append(json_res["correct"])
        re_pattern_pre = "\[[\s\S]*?\]"
    elif args.dataset == "gsm8k":
        with open("../data/gsm8k/gold/math_test_answer.txt", 'r') as label_f:
            golden = label_f.readlines()
        re_pattern_pre="{.*(([1-9]\d*\.?\d*)|(0\.\d*[1-9])|([0-9]+)).*?}"
        re_pattern_post="([1-9]\d*\.?\d*)|(0\.\d*[1-9])|([0-9]+)"
    elif args.dataset == "commonsenseqa":
        with open("../data/commonsenseqa/test.jsonl", 'r', encoding="UTF-8") as label_f:
            for i in label_f.readlines():
                golden.append(json.loads(i)["answer"])
        re_pattern_pre = "\[[\s\S]*?\]"
    elif args.dataset == "addsub":
        with open("../data/addsub/AddSub.json", 'r') as label_f:
            datas = json.load(label_f)
        golden = []
        for data in datas:
            a = str(data["lSolutions"][0])
            if a[-2:] == ".0":
                a = a[:-2]
            golden.append(a)
        re_pattern_pre="{.*(([1-9]\d*\.?\d*)|(0\.\d*[1-9])|([0-9]+)).*?}"
        re_pattern_post="([1-9]\d*\.?\d*)|(0\.\d*[1-9])|([0-9]+)"
    elif args.dataset == "strategyqa":
        with open("../data/strategyqa/strategyqa_test.json", 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        for data in json_data:
            if data["answer"]:
                golden.append("yes")
            else:
                golden.append("no")
        re_pattern_pre = "\[.*?\]"
    elif args.dataset == "svamp":
        with open("../data/svamp/SVAMP.json", 'r') as label_f:
            datas = json.load(label_f)
        golden = []
        for data in datas:
            a = str(data["Answer"])
            if a[-2:] == ".0":
                a = a[:-2]
            golden.append(a)
        re_pattern_pre = "{.*(([1-9]\d*\.?\d*)|(0\.\d*[1-9])|([0-9]+)).*?}"
        re_pattern_post="([1-9]\d*\.?\d*)|(0\.\d*[1-9]|([0-9]+))"
    elif args.dataset == "asdiv":
        with open("../data/asdiv/asdiv.json", 'r') as label_f:
            datas = json.load(label_f)['Instances']
        golden = [i['output'][0] for i in datas]
        re_pattern_pre = "{.*(([1-9]\d*\.?\d*)|(0\.\d*[1-9])|([0-9]+)).*?}"
        re_pattern_post="([1-9]\d*\.?\d*)|(0\.\d*[1-9]|([0-9]+))"
    elif args.dataset == "singleeq":
        with open("../data/singleeq/questions.json", 'r') as label_f:
            datas = json.load(label_f)
        golden = []
        for data in datas:
            a = str(data["lSolutions"][0])
            if a[-2:] == ".0":
                a = a[:-2]
            golden.append(a)
        re_pattern_pre="{.*(([1-9]\d*\.?\d*)|(0\.\d*[1-9])|([0-9]+)).*?}"
        re_pattern_post="([1-9]\d*\.?\d*)|(0\.\d*[1-9]|([0-9]+))"
    elif args.dataset == "date":
        with open("../data/date/test.json", 'r', encoding='utf-8') as f:
            lines = json.load(f)
        for line in lines:
            golden.append(line["answer"])
        re_pattern_pre="\{[\s\S]*?\}"
    elif args.dataset == "object_tracking":
        with open("../data/object_tracking/test.json", 'r', encoding='utf-8') as f:
            lines = json.load(f)
        for line in lines:
            golden.append(line["answer"])
        re_pattern_pre = "\{[\s\S]*?\}"
    elif args.dataset == "letter":
        with open("../data/lastletter/last_letters.json", 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        json_data = json_data["examples"]
        for line in json_data:
            golden.append(line["answer"])
        re_pattern_pre="{.*?}"
    else:
        raise ValueError("dataset is not properly defined ...")
    return golden, re_pattern_pre, re_pattern_post