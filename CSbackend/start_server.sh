#!/bin/bash

# Source the environment variables
source ../venv/Scripts/activate
source ../.env

# Run system check
python manage.py check

# Check if system check identified no issues
if [ $? -eq 0 ]; then
    # If no issues, run the server
    python manage.py runserver 8001
else
    # If issues found, print a message
    echo "System check identified issues. Please fix them before starting the server."
fi

# To run 
# chmod +x start_server.sh
# ./start_server.sh
