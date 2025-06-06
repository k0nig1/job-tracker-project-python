#!/bin/bash

if ! command -v python3 &>/dev/null; then
    echo "Python3 not found. Please install it first."
    exit 1
fi

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate

if [ ! -f "requirements.txt" ]; then
    echo "requirements.txt not found!"
    exit 1
fi
python3 -m pip install -r requirements.txt

echo "Virtual environment activated. Dependencies installed." 
echo "---------------------------------------------------------"
echo "Virtual environment activated. Run this script with 'source run_vir.sh' to persist activation in your current shell."
echo "If you want to run tests, use 'source run_tests.sh' after activating the virtual environment."
echo "To deactivate the virtual environment, run 'source stop_vir.sh'."