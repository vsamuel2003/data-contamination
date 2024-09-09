#!/bin/bash

python  ../run.py \
        --experiment llama3/DROP/train \
        --filename ../../../datasets/DROP/token_overlap/train.csv \
        --task sum \
        --dataset "DROP" \
        --split train \
        --model meta-llama/Llama-3-70b-chat-hf \
        --text_column text \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
