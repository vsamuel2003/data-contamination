#!/bin/bash

python  ../run.py \
        --experiment gpt4/GSM8K/test \
        --filename ../../../datasets/GSM8K/token_overlap/test.csv \
        --task cls \
        --dataset "GSM8K" \
        --split test \
        --model gpt-4 \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
