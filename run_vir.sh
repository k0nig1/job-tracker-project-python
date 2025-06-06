#!/bin/bash
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt
echo "Virtual environment activated. Dependencies installed."
echo "Running tests..."
PYTHONPATH=. pytest -v --tb=short --disable-warnings
if [ $? -eq 0 ]; then
    echo "All tests passed successfully."
else
    echo "Some tests failed. Please check the output above."
fi
deactivate
echo "Virtual environment deactivated."
echo "Script execution completed."
echo "You can now run your application or continue with further development."
echo "To reactivate the virtual environment later, run: source venv/bin/activate"
echo "To install additional packages, use: pip install <package_name>"
echo "To remove the virtual environment, simply delete the 'venv' directory."
echo "Thank you for using this script!"
echo "Have a great day!"
echo "For any issues, please refer to the documentation or contact support."
echo "Goodbye!"
echo "Remember to commit your changes to version control if applicable."
echo "If you need to run this script again, just execute: ./run_vir.sh"     