#!/bin/bash

DIRECTORIES=("GSM8K" "MMLU")

for DIR in "${DIRECTORIES[@]}"; do
    SCRIPT_DIR="$DIR"
    for script in "$SCRIPT_DIR"/*.sh; do
        echo "Setting execute permission for $script in $SCRIPT_DIR..."
        chmod +x "$script"
        echo "Running $script in $SCRIPT_DIR..."
        bash "$script"
    done
done