#!/bin/bash

python  ../run.py \
        --experiment llama3/BIG-Bench-Hard/test \
        --filename ../../../datasets/BIG-Bench-Hard/token_overlap/full.csv \
        --task cls \
        --dataset "BIG-Bench-Hard" \
        --split test \
        --model meta-llama/Llama-3-70b-chat-hf \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
