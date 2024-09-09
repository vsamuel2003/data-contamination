#!/bin/bash

python  ../run.py \
        --experiment llama3/ARC-Challenge/train \
        --filename ../../../datasets/ARC-Challenge/token_overlap/train.csv \
        --task cls \
        --dataset "ARC-Challenge" \
        --split train \
        --model meta-llama/Llama-3-70b-chat-hf \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
