# Iter-CoT

Source code for paper "Enhancing Chain-of-Thoughts Prompting with Iterative Bootstrapping in Large Language Models"

Iter-CoT outperforms existing prompting approaches on three distinct reasoning tasks (arithmetic, commonsense and symbolic) across eleven datasets, and demonstrate that LLMs have the capability to enhance their performance by integrating iterative bootstrapping for self-correction and summarization to obtain better reasoning chains for demonstrations.



This repo is still developing, feel free to report bugs and we will fix them.
## Requirements 

 - python 3.8
 - jsonlines
 - openai



***
## Code
### Datasets
The eleven datasets among three different reasoning tasks are in `/Iter-CoT/dataset/`. In particular, for the **Object Tracking** and **Date Understanding** without training set, we sampled a small portion of the test set as the training set (see the paper for the details). We use gsm8k as an example to run the code.
### Zero-Shot-CoT
In order to start generating Iter-CoT, we first perform Zero-Shot-CoT, execute the following command:
```bash
python inference.py --dataset gsm8k \
--max_length 256 \
--batch_size 20 \
--method zero_shot_cot
```
### Iter-CoT(S)
Once we have the results of Zero-Shot-CoT, we can generate Iter-CoT(S) with the following command:
```bash
python iter_cot_strong.py
```
### Iter-CoT(W)
We can generate Iter-CoT(W) with the following command:
```bash
python iter_cot_weak.py
```
### Run Inference
To test the performance of the demonstration on different datasets, we use the following command:
```bash
python inference.py --dataset gsm8k \
--max_length 500 \
--batch_size 20 \
--method strong # or weak
```

### Evaluate
After running the inference in the previous step, we clean the generated answers and calculate the final accuracy (exact match):
```bash
python evaluate.py --data_file gsm8k \
--result_file ../output/gsm8k.json \ # generated from inference
--prompt_file ../output/gsm8k_samples.txt \
--output_file ../output/gsm8k_results.txt \ final results
```
