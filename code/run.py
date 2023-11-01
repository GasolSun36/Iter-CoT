import json
import tqdm
import argparse
import time
import jsonlines
from utils import *
from eval import eval

def generate(data, output_file):
    with open(output_file, 'w', encoding="UTF-8") as out:
        count = len(data) // args.batch_size
        batch_data = [data[i:i+args.batch_size] for i in range(0, args.batch_size * count, args.batch_size)]
        batch_data.append(data[(args.batch_size * count):])
        for i in tqdm.tqdm(batch_data, total=len(batch_data)):
            flag = 0
            while (flag == 0):
                try:
                    answer = gpt(i, response_length=args.max_length, temperature=0.7)
                    flag = 1
                except:
                    time.sleep(3)
            for j in range(len(i)):
                out.write(json.dumps({"prompt": i[j]}) + "\n")
            out.write(json.dumps({"answer": answer.to_dict()}) + "\n")

def gen_few_shot(path):
    with open(path["summary_output"], 'r', encoding="UTF-8") as f:
        with open(path["few_shot"], 'w') as of:
            Q = []
            A = []
            d = f.readlines()
            data = [json.loads(i) for i in d]
            for i in data:
                if "prompt" in i:
                    Q.append(re.search("Q:.*[\s\S].*?Assistant", i["prompt"]).group().replace("\nAssistant","").replace("Q:","").strip())
                if "answer" in i:
                    if "choices" in i["answer"]:
                        for j in range(len(i["answer"]["choices"])):
                            A.append(i["answer"]["choices"][j]["text"])
            assert len(Q) == len(A)
            for i in range(len(Q)):
                of.write(json.dumps({"Question": Q[i], "Answer": A[i]}) + "\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str,
                        default="gsm8k", help="the dataset.")
    parser.add_argument("--max_length", type=int,
                        default=500, help="the max length of LLMs output.")
    parser.add_argument("--batch_size", type=int,
                        default=20, help="20 samples each batch.")
    parser.add_argument("--iter_num", type=int, default=1)
    args = parser.parse_args()

    if args.iter_num == 1:
        args.stage = "initialization"
    else:
        args.stage = "bootstrapping"

    args.method = "weak"
    path = parse_path(args)

    #initialization
    if args.iter_num == 1:
        data = prepare_dataset(args, path)
        generate(data, path['init_output'])
        path["wrong_answer"] = "../output/" + args.dataset + "/" + args.method + "/iter0_wrong.json"
        eval(args)

    #bootstrapping
    args.stage = "bootstrapping"
    data = prepare_dataset(args, path)
    generate(data, path['bootstrap_output'])
    eval(args)

    #summarization
    args.stage = "summarization"
    data = prepare_dataset(args, path)
    generate(data, path['summary_output'])

    #building demonstration pool
    gen_few_shot(path)





