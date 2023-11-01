import json
import tqdm
import argparse
import time
from utils import *
from eval import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str,
                        default="gsm8k", help="the dataset.")
    parser.add_argument("--max_length", type=int,
                        default=500, help="the max length of LLMs output.")
    parser.add_argument("--batch_size", type=int,
                        default=20, help="20 samples each batch.")
    parser.add_argument("--method", type=str, help="strong or weak or zero_shot")
    parser.add_argument("--iter_num", type=int, default=1)
    parser.add_argument("--shot_num", type=int)
    args = parser.parse_args()
    args.stage = "inference"
    path = parse_path(args)
    test_data = read_test_dataset(args, path)
    with open(path["inference_output"], 'w', encoding="UTF-8") as out:
        if args.method == "strong" or args.method == "weak":
            data = [test_data["few_shot"] + '\n' + "\n\nQ: " + i + "\nA: Reasoning Process:" for i in test_data["test_data"]]
        elif args.method == "zero_shot":
            data = [ test_data["prompt"] + i + "\n A: Let's think step by step, " for i in test_data["test_data"]]
        else:
            raise ValueError("No such methods.")
        count = len(data) // args.batch_size
        batch_data = [data[i:i+args.batch_size] for i in range(0, args.batch_size * count, args.batch_size)]
        batch_data.append(data[(args.batch_size * count):])
        for i in tqdm.tqdm(batch_data, total=len(batch_data)):
            flag = 0
            while (flag == 0):
                try:
                    answer = gpt(i, response_length=args.max_length)
                    flag = 1
                except:
                    time.sleep(3)
            for j in range(len(i)):
                out.write(json.dumps({"prompt": i[j]}) + "\n")
            out.write(json.dumps({"answer": answer.to_dict()}) + "\n")

    eval(args)