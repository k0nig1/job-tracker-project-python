#!/bin/bash

if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Please run 'source run_vir.sh' first to create and activate it."
    exit 1
fi

source venv/bin/activate

python main.py --resume data/resume.pdf --output data/report.csv --title developer --location remote