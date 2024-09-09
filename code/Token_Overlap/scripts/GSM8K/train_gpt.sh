#!/bin/bash

python  ../run.py \
        --experiment gpt4/GSM8K/train \
        --filename ../../../datasets/GSM8K/token_overlap/train.csv \
        --task cls \
        --dataset "GSM8K" \
        --split train \
        --model gpt-4 \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
