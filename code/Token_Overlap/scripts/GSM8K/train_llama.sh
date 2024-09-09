#!/bin/bash

python  ../run.py \
        --experiment llama2/GSM8K/train \
        --filename ../../../datasets/GSM8K/token_overlap/train.csv \
        --task cls \
        --dataset "GSM8K" \
        --split train \
        --model meta-llama/Llama-2-70b-chat-hf \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
