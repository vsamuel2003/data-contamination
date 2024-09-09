#!/bin/bash

python  ../run.py \
        --experiment llama2/IMDB/test \
        --filename ../../../datasets/IMDB/token_overlap/test.csv \
        --task cls \
        --dataset "IMDB" \
        --split test \
        --model meta-llama/Llama-2-70b-chat-hf \
        --text_column text \
        --label_column label \
        --process_guided_replication  \
        --process_general_replication \
        --rouge_eval \
        --icl_eval \
