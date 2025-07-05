#!/bin/bash
set -e  # Exit on error

# System dependencies (no sudo needed)
apt-get update && apt-get install -y graphviz

# Python dependencies
pip install -r requirements.txt
