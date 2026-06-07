@echo off
title LinguaX Translator
echo ================================================
echo   LinguaX - Universal Language Translator
echo ================================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b
)

echo [1/2] Installing dependencies...
pip install -r requirements.txt --quiet

echo [2/2] Launching LinguaX...
echo.
python app.py

pause