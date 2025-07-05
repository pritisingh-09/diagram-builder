#!/bin/bash
set -e  # Exit on error

# System dependencies
sudo apt-get update
sudo apt-get install -y graphviz gcc python3-dev

# Python dependencies (with legacy resolver)
pip install --use-deprecated=legacy-resolver -r requirements.txt
