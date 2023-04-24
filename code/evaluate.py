import json
import re
import argparse
import parser
from utils import *
parser = argparse.ArgumentParser()
parser.add_argument("--data_file", type=str, default='gsm8k', help="Please use lowercase dataset.")
parser.add_argument("--result_file", type=str, default='../output/gsm8k.json')
parser.add_argument("--prompt_file", type=str,
                    default='../output/gsm8k_samples.txt')
parser.add_argument("--output_file", type=str,
                    default='../output/gsm8k_results.txt')
args = parser.parse_args()

golden, re_pattern_pre, re_pattern_post = process4evaluate(args)

with open(args.result_file, 'r') as f:
    d = f.readlines()
    data = [json.loads(d[i]) for i in range(len(d))]
    with open(args.prompt_file, 'w') as pf:
        with open(args.output_file, 'w') as of:
            count = 0
            acc = 0
            for i in data:
                if "prompt" in i or "steps" in i:
                    pf.write(json.dumps(i) + "\n")
                else:
                    if "choices" in i["answer"]:
                        for j in range(len(i["answer"]["choices"])):
                            if re.search(re_pattern_pre, i["answer"]["choices"][j]["text"]) == None:
                                    print(i["answer"]["choices"][j]["text"])
                                    print("id:", count)
                                    of.write("error_max_length" + '\n')
                            else:
                                if args.dataset in ['gsm8k', 'addsub', 'svamp', 'asdiv', 'singleeq']:
                                    answer = re.search(re_pattern_pre, i["answer"]["choices"][j]["text"]).group()
                                    pred = re.search(re_pattern_post, answer).group()
                                    answer = (float(pred))
                                    flag = 0
                                    if answer == float(golden[count]):
                                        acc += 1
                                        flag = 1
                                    of.write(str(answer) + ':' + str(flag) + '\n')
                                elif args.dataset == 'aqua':
                                    answer = re.search(re_pattern_pre, i["answer"]["choices"][j]["text"]).group()[1:-1].split('.')
                                    flag = 0
                                    for a in answer:
                                        a = a.replace("the correct option is:", "")
                                        for c in golden[count]:
                                            if a.replace(" ", "") == c.replace(" ", ""):
                                                acc += 1
                                                flag = 1
                                                break
                                        if flag == 1:
                                            break
                                    of.write(str(answer) + ':' + str(flag) + '\n')
                                elif args.dataset == 'csqa':
                                    answer = re.search(re_pattern_pre, i["answer"]["choices"][j]["text"]).group()[1:-1].split('.')
                                    flag = 0
                                    for a in answer:
                                        if "The correct answer is:".lower() in a.lower():
                                            a = a.replace("The correct answer is:", "")
                                        for c in golden[count]:
                                            if a.replace(" ", "") == c.replace(" ", ""):
                                                acc += 1
                                                flag = 1
                                                break
                                        if flag == 1:
                                            break
                                    of.write(answer[0] + ':' + str(flag) + '\n')
                                elif args.dataset == 'stqa':
                                    answer = re.search(re_pattern_pre, i["answer"]["choices"][j]["text"]).group()[1:-1]
                                    flag = 0
                                    if "the correct answer is:" in answer.lower():
                                        answer = answer.lower().replace("the correct answer is:", "")
                                    if answer.lower().replace(" ", "") == golden[count]:
                                        acc += 1
                                        flag = 1
                                    of.write(str(answer) + ':' + str(flag) + '\n')
                                elif args.dataset in ['date', 'object']:
                                    answer = re.search(re_pattern_pre, i["answer"]["choices"][j]["text"]).group()[1:-1].split('.')
                                    flag = 0
                                    for a in answer:
                                        a = a.replace("The correct answer is:", "").replace("the correct answer is:", "").replace(" ", "")
                                        for c in golden[count]:
                                            if c in a:
                                                acc += 1
                                                flag = 1
                                                break
                                        if flag == 1:
                                            break
                                    of.write(str(answer) + ':' + str(flag) + '\n')
                                elif args.dataset == 'lastletter':
                                    answer = re.search(re_pattern_pre, i["answer"]["choices"][j]["text"]).group()[1:-1]
                                    flag = 0
                                    if answer == golden[count]:
                                        acc += 1
                                        flag = 1
                                    of.write(str(answer) + ':' + str(flag) + '\n')
                                else:
                                    raise ValueError("dataset is not properly defined ...")
                            count += 1
            of.write("acc:" + str(acc) + " count:" + str(count)+'\n')
            of.write("exact match:" + str(acc/count))
