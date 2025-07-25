@echo off
echo 🚀 Starting Bigo Live Agency Commission Calculator...

REM Check if virtual environment exists
if not exist "venv" (
    echo ❌ Virtual environment not found. Please run setup.bat first.
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Set environment variables
if not defined PORT set PORT=8501
set STREAMLIT_SERVER_ADDRESS=0.0.0.0
set STREAMLIT_SERVER_PORT=%PORT%

REM Run the application
echo 🌐 Application will be available at: http://localhost:%PORT%
streamlit run streamlit_app.py --server.port=%PORT% --server.address=0.0.0.0
