#!/bin/bash

python  ../run.py \
        --experiment gpt4/DROP/test \
        --filename ../../../datasets/DROP/token_overlap/test.csv \
        --task sum \
        --dataset "DROP" \
        --split test \
        --model gpt-4 \
        --text_column text \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
