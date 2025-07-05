#!/bin/bash

# Install Graphviz
apt-get update
apt-get install -y graphviz

# Install Python dependencies
pip install -r requirements.txt
