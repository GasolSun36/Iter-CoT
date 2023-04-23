import json
import tqdm
import argparse
import time
import jsonlines
from utils import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str,
                        default="gsm8k", help="the dataset.")
    parser.add_argument("--max_length", type=int,
                        default=500, help="the max length of LLMs output.")
    parser.add_argument("--batch_size", type=int,
                        default=20, help="20 samples each batch.")
    parser.add_argument("--method", type=str, help="strong or weak or zero_shot")

    args = parser.parse_args()
    data = read_dataset(args)
    with open(args.output_file, 'a+', encoding="UTF-8") as out:
        if args.method == "strong" or args.method == "weak":
            data = [i["few_shot"] + '\n' + "\n\nQ: " + i["test_data"] + "\nA: Reasoning Process:" for i in data]
        elif args.method == "zero_shot":
            data = ["Please solve the following math word question and put the final digital result into a curly brace {like this} after 'the correct answer is: '. " + "Q: " + i["test_data"] + "\n A: Let's think step by step, " for i in data]
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
            out.write(json.dumps({"answer": answer.json()}) + "\n")

