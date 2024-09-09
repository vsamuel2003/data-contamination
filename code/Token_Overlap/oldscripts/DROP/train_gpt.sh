#!/bin/bash

python  ../run.py \
        --experiment gpt4/DROP/train \
        --filename ../../../datasets/DROP/token_overlap/train.csv \
        --task sum \
        --dataset "DROP" \
        --split train \
        --model gpt-4 \
        --text_column text \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
