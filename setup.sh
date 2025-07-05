#!/bin/bash
set -e

# Install system dependencies (Render doesn't allow apt-get)
curl -sL https://deb.nodesource.com/setup_14.x | bash -
apt-get install -y graphviz

# Install Python dependencies
pip install -r requirements.txt
