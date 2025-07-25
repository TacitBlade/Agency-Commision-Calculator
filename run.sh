#!/bin/bash

echo "🚀 Starting Bigo Live Agency Commission Calculator..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run ./setup.sh first."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Set environment variables
export STREAMLIT_SERVER_ADDRESS="0.0.0.0"
export STREAMLIT_SERVER_PORT="${PORT:-8501}"

# Run the application
echo "🌐 Application will be available at: http://localhost:${STREAMLIT_SERVER_PORT:-8501}"
streamlit run streamlit_app.py --server.port=${STREAMLIT_SERVER_PORT:-8501} --server.address=0.0.0.0
