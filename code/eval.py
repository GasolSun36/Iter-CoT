import json
import re
import argparse
from utils import *

def eval(args):
    path = parse_path(args)
    golden, re_pattern_pre, re_pattern_post = process4evaluate(args, path)
    if args.stage == "initialization":
        model_output_file = path["init_output"]
        result_file = path["init_statistic_result"]
        path["wrong_answer"] = "../output/" + args.dataset + "/" + args.method + "/iter0_wrong.json"
        save_correct = False
        save_wrong = True
    elif args.stage == "bootstrapping":
        model_output_file = path["bootstrap_output"]
        result_file = path["bootstrap_statistic_result"]
        save_correct = True
        save_wrong = True
    elif args.stage == "summarization":
        model_output_file = path["summary_output"]
        result_file = path["summary_statistic_result"]
        save_correct = False
        save_wrong = False
    elif args.stage == "inference":
        model_output_file = path["inference_output"]
        result_file = path["inference_statistic_result"]
        save_correct = False
        save_wrong = False
    else:
        raise ValueError("stage is not properly defined ...")

    with open(model_output_file, 'r') as f:
        d = f.readlines()
        data = [json.loads(d[i]) for i in range(len(d))]
        with open(result_file, 'w') as sf:
            if save_correct:
                cf = open(path["correct_answer"], 'w')
            if save_wrong:
                wf = open(path["wrong_answer"], 'w')
            count = 0
            acc = 0
            prompt = []
            for i in data:
                if "prompt" in i or "steps" in i or "T" in i:
                    if "prompt" in i:
                        prompt.append(i)
                else:
                    if "choices" in i["answer"]:
                        for j in range(len(i["answer"]["choices"])):
                            if re.search(re_pattern_pre, i["answer"]["choices"][j]["text"]) == None:
                                    print(i["answer"]["choices"][j]["text"])
                                    print("id:", count)
                                    sf.write("error_max_length" + '\n')
                            else:
                                if args.dataset in ['gsm8k', 'addsub', 'svamp', 'asdiv', 'singleeq']:
                                    answer = re.search(re_pattern_pre, i["answer"]["choices"][j]["text"]).group()
                                    pred = re.search(re_pattern_post, answer).group()
                                    answer = (float(pred))
                                    flag = 0
                                    if answer == float(golden[count].strip()):
                                        acc += 1
                                        flag = 1

                                elif args.dataset in ['aqua', "csqa", "date", "object_tracking"]:
                                    answer = re.search(re_pattern_pre, i["answer"]["choices"][j]["text"]).group()[1:-1].lower().split('.')
                                    flag = 0
                                    for a in answer:
                                        a = a.replace("the correct answer is:", "")
                                        for c in golden[count]:
                                            if a.replace(" ", "") == c.replace(" ", ""):
                                                acc += 1
                                                flag = 1
                                                break
                                        if flag == 1:
                                            break

                                elif args.dataset == 'stqa':
                                    answer = re.search(re_pattern_pre, i["answer"]["choices"][j]["text"]).group()[1:-1]
                                    flag = 0
                                    answer = answer.lower().replace("the correct answer is:", "")
                                    if answer.strip() == golden[count].strip():
                                        acc += 1
                                        flag = 1

                                elif args.dataset == 'letter':
                                    answer = re.search(re_pattern_pre, i["answer"]["choices"][j]["text"]).group()[1:-1]
                                    flag = 0
                                    answer = answer.lower().replace("the correct answer is:", "")
                                    if answer.strip() == golden[count].strip():
                                        acc += 1
                                        flag = 1
                                else:
                                    raise ValueError("dataset is not properly defined ...")

                                if save_correct and flag == 1:
                                    cf.write(json.dumps({"prompt": prompt[count]["prompt"],
                                                         "answer": i["answer"]["choices"][j]["text"],
                                                         "correct": golden[count].strip()}) + "\n")
                                if save_wrong and flag == 0:
                                    wf.write(json.dumps({"prompt": prompt[count]["prompt"],
                                                         "answer": i["answer"]["choices"][j]["text"],
                                                         "correct": golden[count].strip()}) + "\n")
                                sf.write(str(answer) + ':' + str(flag) + '\n')
                            count += 1
            sf.write("acc:" + str(acc) + " count:" + str(count)+'\n')
            sf.write("exact match:" + str(acc/count))

def eval_for_single(args, response, gold):
    path = parse_path(args)
    golden, re_pattern_pre, re_pattern_post = process4evaluate(args, path)
    golden = gold
    if args.dataset in ['gsm8k', 'addsub', 'svamp', 'asdiv', 'singleeq']:
        answer = re.search(re_pattern_pre, response).group()
        pred = re.search(re_pattern_post, answer).group()
        answer = (float(pred))
        if answer == float(golden.strip()):
            return True

    elif args.dataset in ['aqua', "csqa", "date", "object_tracking"]:
        answer = re.search(re_pattern_pre, response).group()[1:-1].lower().split('.')
        for a in answer:
            a = a.replace("the correct answer is:", "")
            for c in golden:
                if a.replace(" ", "") == c.replace(" ", ""):
                    return True

    elif args.dataset == 'stqa':
        answer = re.search(re_pattern_pre, response).group()[1:-1]
        answer = answer.lower().replace("the correct answer is:", "")
        if answer.strip() == golden.strip():
            return True

    elif args.dataset == 'letter':
        answer = re.search(re_pattern_pre, response).group()[1:-1]
        answer = answer.lower().replace("the correct answer is:", "")
        if answer.strip() == golden.strip():
            return True
    else:
        return False
    return False


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, default='gsm8k', help="Dataset to be evaluated")
    parser.add_argument("--stage", type=str, required=True,
                        help="initialization, bootstrapping, summarization or inference")
    parser.add_argument("--iter_num", type=int, default=1)
    parser.add_argument("--method", type=str, help="strong or weak or zero_shot")
    args = parser.parse_args()
    eval(args)