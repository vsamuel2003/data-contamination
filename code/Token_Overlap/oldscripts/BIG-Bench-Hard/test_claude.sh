#!/bin/bash

python  ../run.py \
        --experiment claude-sonnet/BIG-Bench-Hard/test \
        --filename ../../../datasets/BIG-Bench-Hard/token_overlap/full.csv \
        --task cls \
        --dataset "BIG-Bench-Hard" \
        --split test \
        --model claude-3-sonnet-20240229 \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
