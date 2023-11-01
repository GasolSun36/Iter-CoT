
# Enhancing Chain-of-Thoughts Prompting with Iterative Bootstrapping in Large Language Models

This repository is the official implementation of Enhancing Chain-of-Thoughts Prompting with Iterative Bootstrapping in Large Language Models. 


## Requirements

To install requirements:

```setup
pip install -r requirements.txt
```

Please put your `OpenAI API KEY` to the `api_key` variable and the model to use to the `model` variable in utils.py.

### Datasets
The eleven datasets among three different reasoning tasks are in `/Iter-CoT/dataset/`. In particular, for the **Date Understanding** without training set, we sampled a small portion of the test set as the training set (see the paper for the details).

## Training

### Iter-CoT
To employ Iter-CoT to generate the demonstrations, you can use the following command:
```bash
iter_num=1
python run.py --dataset "gsm8k" --iter_num $iter_num
```
The demonstrations will be saved in `output/gsm8k/run/iter1_fewshot.json`, which will be used in the inference stage.

If you want to use the demonstrations generated after multi iterations, change the `iter_num` and use the following command:

```bash
iter_num=2 # 3,4,5...
for ((i=1; i<=$iter_num; i++));
do
    python run.py --dataset "gsm8k" --iter_num $i;
done
```
The demonstrations generated in each iteration will be saved in `output/gsm8k/run/iter$i_fewshot.json`, which will be used in the inference stage.


### Important arguments
- `--dataset`: The name of a dataset. Choices = [gsm8k, addsub, svamp, asdiv, singleeq, aqua, csqa, stqa, date, object_tracking, letter]
- `--method`: The chain-of-thought method. Choices = [iter-cot, zero_shot]
- `--iter_num`: The `iter_num` iteration in Iter-CoT.
- `--shot_num`: The number of demonstrations used in inference stage.
- `--stage`: The stage of Iter-CoT

## Evaluation

To evaluate the performance of the demonstrations on different datasets, you can use the following command:
```bash
iter_num=1
python inference.py --dataset "gsm8k" --iter_num $iter_num  --method "run" --shot_num 8
```
The output will be saved in `output/gsm8k/run/iter1_inf_output.json` and the statistic result will be saved in `output/gsm8k/run/iter1_inf_result.json`.


## Contributing

MIT License

Copyright (c) [2023] [anonymous]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.