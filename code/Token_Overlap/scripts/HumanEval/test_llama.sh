#!/bin/bash

python  ../run.py \
        --experiment oracle/HumanEval/test \
        --filename ../../../datasets/HumanEval/token_overlap/full.csv \
        --task cls \
        --dataset "HumanEval" \
        --split test \
        --model vsamuel@andrew.cmu.edu/llama-2-70b-chat-final_oracle-2024-07-29-02-47-08-4d586374 \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
