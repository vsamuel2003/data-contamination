#!/bin/bash

python  ../run.py \
        --experiment claude-sonnet/ARC-Challenge/test \
        --filename ../../../datasets/ARC-Challenge/token_overlap/test.csv \
        --task cls \
        --dataset "ARC-Challenge" \
        --split test \
        --model claude-3-sonnet-20240229 \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
