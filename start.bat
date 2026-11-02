@echo off
cd /d "%~dp0"
title StockPulse AI Launcher
echo ===================================================
echo     STOCKPULSE AI - Starting Services
echo ===================================================
echo.

set PATH=C:\Users\konga\.local\bin;%PATH%

:: Determine Python executable
set PYTHON_EXE=backend_venv\Scripts\python.exe
if not exist "%PYTHON_EXE%" (
    set PYTHON_EXE=python
)

:: Start Backend
echo [1/2] Starting FastAPI Backend on http://127.0.0.1:8000...
start "StockPulse AI - Backend (Port 8000)" cmd /k "cd /d ""%~dp0"" && "%PYTHON_EXE%" backend\run.py"

:: Wait 2 seconds
timeout /t 2 /nobreak > nul

:: Start Frontend
echo [2/2] Starting Vite React Frontend on http://localhost:5173...
start "StockPulse AI - Frontend (Port 5173)" cmd /k "cd /d ""%~dp0\frontend"" && set PATH=C:\Users\konga\.local\bin;%%PATH%% && npm run dev"

echo.
echo ===================================================
echo   STOCKPULSE AI is up and running!
echo   Frontend Dashboard: http://localhost:5173
echo   Interactive API Docs: http://127.0.0.1:8000/docs
echo   Verified Demo User: investor@stockpulse.ai / stockpulse2026
echo ===================================================
echo.
pause
