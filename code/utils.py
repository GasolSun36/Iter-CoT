import random

import jsonlines
import json
import requests
import re
import os
import openai

openai.api_key = "Your own API keys"
def gpt(prompt, n=1, model='', response_length=500, temperature=0, top_p=1, frequency_penalty=0,
              presence_penalty=0, start_text='', restart_text='', stop_seq=[], api_key='', **kwargs):
    response = openai.Completion.create(
        model = "Your Base Large Language Models",
        prompt=prompt,
        temperature=temperature,
        max_tokens=response_length,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty)

    return response


def decoder_for_gpt(input, response_length, temperature):
    response = gpt(input, response_length=response_length, temperature=temperature)
    response = response.to_dict()
    return response["choices"][0]["text"]

zero_shot_prompt = {"option":"Please find one of the following options that can answer the question. You should put the correct option into a curly brace {like this} after 'the correct answer is:'. Q: ",
          "digit": "Please solve the following math word question and put the final digital result into a curly brace {like this} . Q: ",
          "yes_no": "Please read the following question and answer it (only Yes or No). You should put the answer into a curly brace {like this} after 'the correct answer is:'. Q: ",
          "letter": "Please put the answer into a curly brace {like this} after 'the correct answer is: '. "}

def read_test_dataset(args, path):
    if args.dataset in ['gsm8k', 'addsub', 'svamp', 'asdiv', 'singleeq']:
        prompt = zero_shot_prompt["digit"]
    elif args.dataset in ["aqua", "csqa", "date", "object_tracking"]:
        prompt = zero_shot_prompt["option"]
    else:
        prompt = zero_shot_prompt["letter"]
    if args.dataset == "aqua":
        with open("../dataset/aqua/test.json", 'r', encoding="UTF-8") as f:
            test_data = [json.loads(i)["question"] + "\nOptions: " +  "  ".join(json.loads(i)["options"]) for i in f.readlines()]

    elif args.dataset == "gsm8k":
        with jsonlines.open("../dataset/gsm8k/test.jsonl", "r") as f:
            test_data = [i["question"] for i in f]

    elif args.dataset == "csqa":
        with jsonlines.open("../dataset/csqa/test.jsonl", "r") as f:
            test_data = [i["question"] for i in f]

    elif args.dataset == "addsub":
        with open("../dataset/addsub/AddSub.json", 'r', encoding="UTF-8") as f:
            test_data = [i["sQuestion"].strip() for i in json.load(f)]

    elif args.dataset == "stqa":
        with open("../dataset/stqa/test.json", 'r', encoding="UTF-8") as f:
            test_data = [i["question"] for i in json.load(f)]

    elif args.dataset == "svamp":
        with open("../dataset/svamp/SVAMP.json", 'r', encoding="UTF-8") as f:
            test_data = [i["Body"].strip() + " " + i["Question"].strip() for i in json.load(f)]

    elif args.dataset == "asdiv":
        with open("../dataset/asdiv/asdiv.json", 'r', encoding="UTF-8") as f:
            test_data = [ i["input"].strip() for i in json.load(f)["Instances"]]

    elif args.dataset == "singleeq":
        with open("../dataset/singleeq/questions.json", 'r', encoding="UTF-8") as f:
            test_data = [i["sQuestion"].strip() for i in json.load(f)]

    elif args.dataset == "date":
        with open("../dataset/date/test.json", 'r', encoding="UTF-8") as f:
            test_data = [i["question"] for i in json.load(f)]

    elif args.dataset == "object_tracking":
        with open("../dataset/object_tracking/test.json", 'r', encoding="UTF-8") as f:
            test_data = [i["question"] for i in json.load(f)]

    elif args.dataset == "letter":
        with open("../dataset/letter/test.json", 'r', encoding="UTF-8") as f:
            test_data = [json.loads(i)["question"] for i in f.readlines()]

    else:
        raise ValueError("dataset is not properly defined ...")

    if args.method in ["weak", "strong"]:
        shared_fewshot = ["gsm8k", "asdiv", "svamp", "singleeq", "addsub"]
        if args.dataset in shared_fewshot:
            few_shot_file = "../output/" + "gsm8k" + "/"+ args.method + "/iter"  +str(args.iter_num) + "_fewshot.json"
        else:
            few_shot_file = path["few_shot"]
        few_shot = ''
        with open(few_shot_file, 'r', encoding="UTF-8") as f:
            fewshots = [json.loads(i) for i in f.readlines()]
            fewshots = random.sample(fewshots, args.shot_num)
            for i in fewshots:
                few_shot += ("Q: " + i["Question"] + "\nA: Reasoning Process: " + i["Answer"] + "\n")
                # no strong_few_shot for stqa
    else:
        few_shot = ""
    data = {"prompt":prompt, "test_data":test_data,"few_shot":few_shot}

    return data

def prepare_dataset(args, path):
    if args.iter_num == 1 and args.stage == 'initialization':
        if args.dataset in ['gsm8k', 'addsub', 'svamp', 'asdiv', 'singleeq']:
            prompt = zero_shot_prompt["digit"]
        elif args.dataset in ["aqua", "csqa", "date", "object_tracking"]:
            prompt = zero_shot_prompt["option"]
        else:
            prompt = zero_shot_prompt["letter"]
        end = "\n A: Let's think step by step, "
        if args.dataset == "aqua":
            with open("../dataset/aqua/train.json", 'r', encoding="UTF-8") as f:
                data = [prompt + json.loads(i)["question"] + "\nOptions: " +  "  ".join(json.loads(i)["options"]) + end for i in f.readlines()]
        elif args.dataset == "gsm8k":
            with jsonlines.open("../dataset/gsm8k/train.jsonl", "r") as f:
                data = [prompt + i["question"] + end for i in f]

        elif args.dataset == "csqa":
            with jsonlines.open("../dataset/csqa/train.jsonl", "r") as f:
                data = [prompt + i["question"] + end for i in f]

        elif args.dataset == "addsub":
            with open("../dataset/addsub/AddSub.json", 'r', encoding="UTF-8") as f:
                data = [prompt + i["sQuestion"].strip() + end for i in json.load(f)]

        elif args.dataset == "stqa":
            with open("../dataset/stqa/train.json", 'r', encoding="UTF-8") as f:
                data = [prompt + i["question"] + end for i in json.load(f)]

        elif args.dataset == "svamp":
            with open("../dataset/svamp/SVAMP.json", 'r', encoding="UTF-8") as f:
                data = [prompt + i["Body"].strip() + " " + i["Question"].strip() for i in json.load(f)]

        elif args.dataset == "asdiv":
            with open("../dataset/asdiv/asdiv.json", 'r', encoding="UTF-8") as f:
                data = [prompt + i["input"].strip() for i in json.load(f)["Instances"]]

        elif args.dataset == "singleeq":
            with open("../dataset/singleeq/questions.json", 'r', encoding="UTF-8") as f:
                data = [prompt + i["sQuestion"].strip() for i in json.load(f)]

        elif args.dataset == "date":
            with open("../dataset/date/train.json", 'r', encoding="UTF-8") as f:
                data = [prompt + i["question"] for i in json.load(f)]

        elif args.dataset == "object_tracking":
            with open("../dataset/object_tracking/train.json", 'r', encoding="UTF-8") as f:
                data = [prompt + i["question"] for i in json.load(f)]

        elif args.dataset == "letter":
            with open("../dataset/letter/train.json", 'r', encoding="UTF-8") as f:
                data = [prompt + json.loads(i)["question"] for i in f.readlines()]

        else:
            raise ValueError("dataset is not properly defined ...")

    elif args.stage == "bootstrapping":
        iter_num = re.search("iter.*",path["wrong_answer"]).group()
        iter_num = re.search("[1-9]",iter_num).group()
        wrong_answer = path["wrong_answer"].replace(iter_num,str(int(iter_num)-1))
        with open(wrong_answer, 'r', encoding="UTF-8") as wf:
            error = wf.readlines()
            end = "A: Let's think step by step,"
            if args.iter_num == 1:
                data = ["User: " + json.loads(i)["prompt"].replace(end, '').strip() + "\nAssistant: Let's think step by step, " +
                        json.loads(i)["answer"].strip() + "\nUser: The answer is not right, can you think more carefully and give me the final answer? \n Assistant: "
                        for i in error]
            else:
                data = [json.loads(i)["prompt"] + json.loads(i)["answer"].strip() + "\nUser: The answer is still not right, can you think more carefully and give me the final answer? \n Assistant: "
                        for i in error]

    elif args.stage == "summarization":
        with open(path["correct_answer"], 'r', encoding="UTF-8") as cf:
            correct = cf.readlines()
            data = [json.loads(i)["prompt"] + json.loads(i)["answer"] +
                    "\nUser: You're right! Can you give me a complete reasoning process and final answer again?\n Assistant: Sure! Reasoning process: "
                    for i in correct]

    return data

def parse_path(args):
    path = dict()
    dir = "../output/" + args.dataset + "/" + args.method + "/"
    if not os.path.exists(dir):
        os.makedirs(dir)
    if args.method in ["weak", "strong"]:
        path["inference_output"] = dir + "iter" + str(args.iter_num) + "_inf_output.json"
        path["inference_statistic_result"] = dir + "iter" + str(args.iter_num) + "_inf_result.json"
    else:
        path["inference_output"] = dir + "output.json"
        path["inference_statistic_result"] = dir + "result.json"
    path["init_output"] = dir + "init_output.json"
    path["init_statistic_result"] = dir + "init_result.json"
    path["bootstrap_output"] = dir + "iter" + str(args.iter_num) + "_bp_output.json"
    path["bootstrap_statistic_result"] = dir + "iter" + str(args.iter_num) + "_bp_result.json"
    path["summary_output"] = dir + "iter" + str(args.iter_num) + "_summary_output.json"
    path["summary_statistic_result"] = dir + "iter" + str(args.iter_num) + "_summary_result.json"
    path["correct_answer"] = dir + "iter" + str(args.iter_num) + "_correct.json"
    path["wrong_answer"] = dir + "iter" + str(args.iter_num) + "_wrong.json"
    path["few_shot"] = dir + "iter" + str(args.iter_num) + "_fewshot.json"
    if args.stage == "bootstrapping":
        if os.path.exists(dir + "iter" + str(args.iter_num - 1) + "_wrong.json"):
            path["golden"] = dir + "iter" + str(args.iter_num - 1) + "_wrong.json"
        else:
            raise FileNotFoundError("The golden file can't be found! ")
    return path


def process4evaluate(args, path):
    golden = []
    re_pattern_pre = ""
    re_pattern_post = ""
    datafile = ""
    if args.stage == "bootstrapping":
        with open(path["golden"], 'r', encoding='utf-8') as label_f:
            golden = label_f.readlines()
            golden = [json.loads(i)["correct"] for i in golden]
    if args.dataset == "aqua":
        if args.stage == "inference":
            datafile = "../dataset/aqua/test.json"
        elif args.stage == "initialization":
            datafile = "../dataset/aqua/train.json"
        if datafile != '':
            with open(datafile, 'r', encoding='utf-8') as label_f:
                for i in label_f.readlines():
                    for j in json.loads(i)["options"]:
                        if json.loads(i)["correct"] == j[0]:
                            golden.append(j.split(")", 1))
        re_pattern_pre = "\{[\s\S]*?\}"

    elif args.dataset == "gsm8k":
        if args.stage == "inference":
            datafile = "../dataset/gsm8k/test.jsonl"
        elif args.stage == "initialization":
            datafile = "../dataset/gsm8k/train.jsonl"
        if datafile != "":
            with jsonlines.open(datafile, 'r') as label_f:
                for data in label_f:
                    golden.append(data["answer"].split("####")[1].strip())
        re_pattern_pre="{.*(([1-9]\d*\.?\d*)|(0\.\d*[1-9])|([0-9]+)).*?}"
        re_pattern_post="([1-9]\d*\.?\d*)|(0\.\d*[1-9])|([0-9]+)"

    elif args.dataset == "csqa":
        if args.stage == "inference":
            datafile = "../dataset/csqa/test.jsonl"
        elif args.stage == "initialization":
            datafile = "../dataset/csqa/train.jsonl"
        if datafile != "":
            with open(datafile, 'r', encoding="UTF-8") as label_f:
                for i in label_f:
                    golden.append(json.loads(i)["answer"])
        re_pattern_pre = "\{[\s\S]*?\}"

    elif args.dataset == "addsub":
        if args.stage == "inference":
            with open("../dataset/addsub/AddSub.json", 'r') as label_f:
                datas = json.load(label_f)
            for data in datas:
                a = str(data["lSolutions"][0])
                golden.append(a)
        re_pattern_pre="{.*(([1-9]\d*\.?\d*)|(0\.\d*[1-9])|([0-9]+)).*?}"
        re_pattern_post="([1-9]\d*\.?\d*)|(0\.\d*[1-9])|([0-9]+)"

    elif args.dataset == "stqa":
        if args.stage == "inference":
            datafile = "../dataset/stqa/test.json"
        elif args.stage == "initialization":
            datafile = "../dataset/stqa/train.json"
        if datafile != "":
            with open(datafile, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
                for data in json_data:
                    if data["answer"]:
                        golden.append("yes")
                    else:
                        golden.append("no")
        re_pattern_pre = "\{.*?\}"

    elif args.dataset == "svamp":
        if args.stage == "inference":
            with open("../dataset/svamp/SVAMP.json", 'r') as label_f:
                datas = json.load(label_f)
            for data in datas:
                a = str(data["Answer"])
                golden.append(a)
        re_pattern_pre = "{.*(([1-9]\d*\.?\d*)|(0\.\d*[1-9])|([0-9]+)).*?}"
        re_pattern_post="([1-9]\d*\.?\d*)|(0\.\d*[1-9]|([0-9]+))"

    elif args.dataset == "asdiv":
        if args.stage == "inference":
            with open("../dataset/asdiv/asdiv.json", 'r') as label_f:
                datas = json.load(label_f)['Instances']
            golden = [i['output'][0] for i in datas]
        re_pattern_pre = "{.*(([1-9]\d*\.?\d*)|(0\.\d*[1-9])|([0-9]+)).*?}"
        re_pattern_post="([1-9]\d*\.?\d*)|(0\.\d*[1-9]|([0-9]+))"

    elif args.dataset == "singleeq":
        if args.stage == "inference":
            with open("../dataset/singleeq/questions.json", 'r') as label_f:
                datas = json.load(label_f)
            for data in datas:
                a = str(data["lSolutions"][0])
                golden.append(a)
        re_pattern_pre="{.*(([1-9]\d*\.?\d*)|(0\.\d*[1-9])|([0-9]+)).*?}"
        re_pattern_post="([1-9]\d*\.?\d*)|(0\.\d*[1-9]|([0-9]+))"

    elif args.dataset == "date":
        if args.stage == "inference":
            datafile = "../dataset/date/test.json"
        elif args.stage == "initialization":
            datafile = "../dataset/date/train.json"
        if datafile != "":
            with open(datafile, 'r', encoding='utf-8') as f:
                lines = json.load(f)
                for line in lines:
                    golden.append(line["answer"])
        re_pattern_pre="\{[\s\S]*?\}"

    elif args.dataset == "object_tracking":
        if args.stage == "inference":
            datafile = "../dataset/object_tracking/test.json"
        elif args.stage == "initialization":
            datafile = "../dataset/object_tracking/train.json"
        if datafile != "":
            with open(datafile, 'r', encoding='utf-8') as f:
                lines = json.load(f)
                for line in lines:
                    golden.append(line["answer"])
        re_pattern_pre = "\{[\s\S]*?\}"

    elif args.dataset == "letter":
        if args.stage == "inference":
            datafile = "../dataset/letter/test.json"
        elif args.stage == "initialization":
            datafile = "../dataset/letter/train.json"
        if datafile != "":
            with open(datafile, 'r', encoding='utf-8') as label_f:
                for i in label_f.readlines():
                    golden.append(json.loads(i)["answer"].strip())
        re_pattern_pre="{.*?}"

    else:
        raise ValueError("dataset is not properly defined ...")
    return golden, re_pattern_pre, re_pattern_post

