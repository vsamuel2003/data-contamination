#!/bin/bash

python  ../run.py \
        --experiment claude-sonnet/DROP/train \
        --filename ../../../datasets/DROP/token_overlap/train.csv \
        --task sum \
        --dataset "DROP" \
        --split train \
        --model claude-3-sonnet-20240229 \
        --text_column text \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
