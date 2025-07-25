#!/bin/bash

# Install system dependencies
sudo apt-get update
sudo apt-get install -y python3-pip

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Set environment variables
export PORT=${PORT:-8501}
export STREAMLIT_SERVER_ADDRESS="0.0.0.0"
export STREAMLIT_SERVER_PORT=$PORT

# Start Streamlit
streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
