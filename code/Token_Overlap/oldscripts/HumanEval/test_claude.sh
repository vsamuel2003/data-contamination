#!/bin/bash

python  ../run.py \
        --experiment claude-sonnet/HumanEval/test \
        --filename ../../../datasets/HumanEval/token_overlap/full.csv \
        --task xsum \
        --dataset "HumanEval" \
        --split test \
        --model claude-3-sonnet-20240229 \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
