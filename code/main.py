import json
import tqdm
import argparse
import time
import jsonlines
from utils import *
from iter_cot_few_shot import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str,
                        default="gsm8k", help="the dataset.")
    parser.add_argument("--output_file", type=str,
                        default="../output/gsm8k.txt", help="the output file.")
    parser.add_argument("--max_length", type=int,
                        default=500, help="the max length of LLMs output.")
    parser.add_argument("--batch_size", type=int,
                        default=20, help="20 samples each batch.")
    parser.add_argument("--method", type=str, help="strong or weak")
    parser.add_argument("--strong_few_shot", type=str, help="Iter-CoT(S)")
    parser.add_argument("--weak_few_shot", type=str, help="Iter-CoT(W)")  
    args = parser.parse_args()
    args = read_dataset(args)
    with jsonlines.open(args.data_file, 'r') as f:
        with open(args.output_file, 'a+', encoding="UTF-8") as out:
            if args.method == "strong":
                data = [
                    args.strong_few_shot + '\n' + "\n\nQ: " + i["question"] + "\nA: Reasoning Process:" for i in f]
            elif args.method == "weak":
                data = [
                    args.weak_few_shot + '\n' + "\n\nQ: " + i["question"] + "\nA: Reasoning Process:" for i in f]
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

