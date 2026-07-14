@echo off
REM Quick start script for NEXUS AI (Windows)

echo.
echo 🚀 NEXUS AI - Quick Start (Windows)
echo ===================================
echo.

cd backend

if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -q -r requirements.txt

echo.
echo ✅ Backend starting...
echo.

uvicorn app.main:app --reload --port 8000
