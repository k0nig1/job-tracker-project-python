#!/bin/bash

if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "Virtual environment is not active. Nothing to deactivate."
    exit 0
else
    echo "Deactivating virtual environment..."
    # Deactivate the virtual environment
    deactivate
fi