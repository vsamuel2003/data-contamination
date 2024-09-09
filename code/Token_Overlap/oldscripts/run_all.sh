#!/bin/bash

SCRIPT_DIR="BIG-Bench-Hard"

for script in "$SCRIPT_DIR"/*.sh; do
    echo "Setting execute permission for $script..."
    chmod +x "$script"
    echo "Running $script..."
    bash "$script"
done
