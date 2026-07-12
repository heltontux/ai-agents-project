#!/bin/bash

DIRS=(app agents api services tools memory prompts config tests docs scripts)

# Cria os diretórios
mkdir -p "${DIRS[@]}"

# Cria o mesmo arquivo em todos eles
for dir in "${DIRS[@]}"; do
    touch "$dir/__init.py__"
done
