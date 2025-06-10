#!/bin/bash

if [[ -z "$VIRTUAL_ENV" && ! -d "venv" ]]; then
    echo "No active virtual environment and 'venv' directory not found. Nothing to deactivate."
    exit 0
else
    echo "Deactivating virtual environment..."
    echo "---------------------------------------------------------"
    echo "Virtual environment deactivated. You can reactivate it with 'source venv/bin/activate'."
    echo "Or, don't forget to delete the 'venv' directory if you no longer need it."
    # Deactivate the virtual environment
    deactivate

    rm -rf venv
    echo "Virtual environment 'venv' removed."
    echo "---------------------------------------------------------"
    echo "You can now safely close the terminal or continue with other tasks."
fi