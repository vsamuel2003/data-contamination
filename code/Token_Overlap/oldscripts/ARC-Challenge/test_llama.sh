#!/bin/bash

python  ../run.py \
        --experiment llama3/ARC-Challenge/test \
        --filename ../../../datasets/ARC-Challenge/token_overlap/test.csv \
        --task cls \
        --dataset "ARC-Challenge" \
        --split test \
        --model meta-llama/Llama-3-70b-chat-hf \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
