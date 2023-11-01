iter_num=1
python weak.py --dataset "gsm8k" --iter_num $iter_num
python inference.py --dataset "gsm8k" --iter_num $iter_num  --method "weak" --shot_num 8