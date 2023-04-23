import jsonlines
import json
import requests
from iter_cot_few_shot import *
import re

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
        with open("../dataset/aqua/test.json", 'r', encoding="UTF-8") as f:
            test_data = [json.loads(i)["question"] for i in f.readlines()]
        args.output_path = "../output/aqua.json"

    elif args.dataset == "gsm8k":
        with jsonlines.open("../dataset/gsm8k/test.jsonl", "r", encoding="UTF-8") as f:
            test_data = [i["question"] for i in f]
        args.output_path = "../output/gsm8k.json"

    elif args.dataset == "csqa":
        with jsonlines.open("../dataset/csqa/test.jsonl", "r", encoding="UTF-8") as f:
            test_data = [i["question"] for i in f]
        args.output_path = "../output/csqa.json"

    elif args.dataset == "addsub":
        with open("../dataset/addsub/AddSub.json", 'r', encoding="UTF-8") as f:
            test_data = [i["sQuestion"].strip() for i in json.load(f)]
        args.output_path = "../output/addsub.json"

    elif args.dataset == "stqa":
        with open("../dataset/stqa/test.json", 'r', encoding="UTF-8") as f:
            test_data = [i["question"] for i in json.load(f)]
        args.output_path = "../output/stqa.json"

    elif args.dataset == "svamp":
        with open("../dataset/svamp/SVAMP.json", 'r', encoding="UTF-8") as f:
            test_data = [i["Body"].strip() + " " + i["Question"].strip() for i in json.load(f)]
        args.output_path = "../output/svamp.json"

    elif args.dataset == "asdiv":
        with open("../dataset/asdiv/asdiv.json", 'r', encoding="UTF-8") as f:
            test_data = [ i["input"].strip() for i in json.load(f)["Instances"]]
        args.output_path = "../output/asdiv.json"

    elif args.dataset == "singleeq":
        with open("../dataset/singleeq/questions.json", 'r', encoding="UTF-8") as f:
            test_data = [i["sQuestion"].strip() for i in json.load(f)]
        args.output_path = "../output/singleeq.json"

    elif args.dataset == "date":
        with open("../dataset/date/test.json", 'r', encoding="UTF-8") as f:
            test_data = [i["question"] for i in json.load(f)]
        args.output_path = "../output/date.json"

    elif args.dataset == "object_tracking":
        with open("../dataset/object_tracking/test.json", 'r', encoding="UTF-8") as f:
            test_data = [i["question"] for i in json.load(f)]
        args.output_path = "../output/object_tracking.json"

    elif args.dataset == "letter":
        with open("../dataset/lastletter/last_letters.json", 'r', encoding="UTF-8") as f:
            test_data = [i["question"] for i in json.load(f)["examples"]]
        args.output_path = "../output/lastletter.json"

    else:
        raise ValueError("dataset is not properly defined ...")

    if args.method == "strong" or args.method == "weak":
        shared_fewshot = ["gsm8k", "asdiv", "svamp", "singleeq", "addsub"]
        with open("../dataset/few_shot.json", 'r', encoding="UTF-8") as f:
            fewshots = json.load(f)
            if args.dataset in shared_fewshot:
                few_shot = fewshots["gsm8k"][args.method]
            else:
                few_shot = fewshots[args.dataset][args.method]
                # no strong_few_shot for stqa
    else:
        few_shot = ""
    data = {"test_data":test_data,"few_shot":few_shot}

    return data


def process4evaluate(args):
    golden = []
    re_pattern_pre = ""
    re_pattern_post = ""
    if args.dataset == "aqua":
        with open("../data/aqua/test.json", 'r', encoding='utf-8') as label_f:
            for i in label_f.readlines():
                for j in json.loads(i)["options"]:
                    if json.loads(i)["correct"] == j[0]:
                        golden.append(j.split(")", 1))
        re_pattern_pre = "\[[\s\S]*?\]"

    elif args.dataset == "gsm8k":
        with jsonlines.open("../data/gsm8k/test.jsonl", 'r') as label_f:
            for data in label_f:
                golden.append(re.search("[0-9]+", data["answer"]).group())
        re_pattern_pre="{.*(([1-9]\d*\.?\d*)|(0\.\d*[1-9])|([0-9]+)).*?}"
        re_pattern_post="([1-9]\d*\.?\d*)|(0\.\d*[1-9])|([0-9]+)"

    elif args.dataset == "csqa":
        with open("../data/csqa/test.jsonl", 'r', encoding="UTF-8") as label_f:
            for i in label_f:
                golden.append(json.loads(i)["answer"])
        re_pattern_pre = "\[[\s\S]*?\]"

    elif args.dataset == "addsub":
        with open("../data/addsub/AddSub.json", 'r') as label_f:
            datas = json.load(label_f)
        for data in datas:
            a = str(data["lSolutions"][0])
            golden.append(a)
        re_pattern_pre="{.*(([1-9]\d*\.?\d*)|(0\.\d*[1-9])|([0-9]+)).*?}"
        re_pattern_post="([1-9]\d*\.?\d*)|(0\.\d*[1-9])|([0-9]+)"

    elif args.dataset == "stqa":
        with open("../data/stqa/strategyqa_test.json", 'r', encoding='utf-8') as f:
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