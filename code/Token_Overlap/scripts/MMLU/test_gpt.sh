#!/bin/bash

python  ../run.py \
        --experiment gpt4/MMLU/test \
        --filename ../../../datasets/MMLU/token_overlap/test.csv \
        --task cls \
        --dataset "MMLU" \
        --split test \
        --model gpt-4 \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
