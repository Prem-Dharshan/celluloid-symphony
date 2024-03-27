#!/bin/bash

# Step 1: Create virtual environment
python3 -m venv venv

# Step 2: Activate virtual environment
source venv/bin/activate

# Step 3: Install requirements
pip install -r CSbackend/requirements.txt

# Step 4: Change directory to CSbackend
cd CSbackend

# Step 5: Source .env file
source ../.env

echo "Setup completed. Virtual environment activated and .env file sourced."
