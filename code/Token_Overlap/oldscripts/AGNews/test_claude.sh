#!/bin/bash

python  ../run.py \
        --experiment claude-sonnet/AGNews/test \
        --filename ../../../datasets/AGNews/token_overlap/test.csv \
        --task cls \
        --dataset "AG News" \
        --split test \
        --model claude-3-sonnet-20240229 \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
