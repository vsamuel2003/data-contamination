#!/bin/bash

python  ../run.py \
        --experiment claude-sonnet/DROP/test \
        --filename ../../../datasets/DROP/token_overlap/test.csv \
        --task sum \
        --dataset "DROP" \
        --split test \
        --model claude-3-sonnet-20240229 \
        --text_column text \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
