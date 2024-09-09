#!/bin/bash

python  ../run.py \
        --experiment gpt4/ARC-Challenge/train \
        --filename ../../../datasets/ARC-Challenge/token_overlap/train.csv \
        --task cls \
        --dataset "ARC-Challenge" \
        --split train \
        --model gpt-4 \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
