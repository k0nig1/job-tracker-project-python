#!/bin/bash
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if venv is activated
if [[ -z "$VIRTUAL_ENV" ]]; then
  echo -e "${RED}Virtual environment is not active. Please run 'source run_vir.sh' first.${NC}"
  exit 1
fi

echo "Running tests..."

PYTHONPATH=. pytest -v --tb=short --disable-warnings

# Check the exit status of pytest
if [ $? -eq 0 ]; then
    echo -e "${GREEN}All tests passed successfully.${NC}"
else
    echo -e "${RED}Some tests failed. Please check the output above.${NC}"
fi