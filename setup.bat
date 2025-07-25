@echo off
echo 🎯 Setting up Bigo Live Agency Commission Calculator...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.11 or higher.
    pause
    exit /b 1
)

REM Show Python version
echo ✅ Python version:
python --version

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔄 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements
echo 📥 Installing requirements...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Create .streamlit directory if it doesn't exist
if not exist ".streamlit" mkdir .streamlit

echo ✅ Setup complete!
echo.
echo To run the application:
echo 1. Run: run.bat
echo.
pause
