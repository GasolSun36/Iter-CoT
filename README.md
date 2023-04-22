# Iter-CoT

Source code for paper "Enhancing Chain-of-Thoughts Prompting with Iterative Bootstrapping in Large Language Models"

## Requirements 

 - python 3.8
 - jsonlines
 - openai

***
## Code
### Datasets
The eleven datasets among three different reasoning tasks are in `/Iter-CoT/dataset/`. In particular, for the **Object Tracking** and **Date Understanding** without training set, we sampled a small portion of the test set as the training set (see the paper for the details).
### Zero-Shot-CoT
In order to start generating Iter-CoT, we first perform Zero-Shot-CoT, execute the following command:
```bash
python zero_shot_cot.py
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
python main.py
```

### Evaluate
After running the inference in the previous step, we clean the generated answers and calculate the final accuracy (exact match):
```bash
python evaluate.py
```
