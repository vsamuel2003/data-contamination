#!/bin/bash

python  ../run.py \
        --experiment claude-sonnet/IMDB/train \
        --filename ../../../datasets/IMDB/token_overlap/train.csv \
        --task cls \
        --dataset "IMDB" \
        --split train \
        --model claude-3-sonnet-20240229 \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
