# STOCKPULSE AI Launch Script (PowerShell)
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not $ScriptDir) { $ScriptDir = (Get-Location).Path }
Set-Location $ScriptDir

$env:PATH = "C:\Users\konga\.local\bin;" + $env:PATH
Write-Host "===================================================" -ForegroundColor Green
Write-Host "    STOCKPULSE AI - Starting Intelligence Platform" -ForegroundColor Cyan
Write-Host "===================================================" -ForegroundColor Green

$pythonExe = Join-Path $ScriptDir "backend_venv\Scripts\python.exe"
if (-not (Test-Path $pythonExe)) {
    $pythonExe = "python"
}

# 1. Start FastAPI Backend in background or dedicated window
Write-Host "`n[1/2] Starting Backend API on http://127.0.0.1:8000..." -ForegroundColor Yellow
Start-Process -FilePath "cmd.exe" -ArgumentList "/k cd /d `"$ScriptDir`" && `"$pythonExe`" backend\run.py"

Start-Sleep -Seconds 2

# 2. Start Frontend Dev Server
$frontendDir = Join-Path $ScriptDir "frontend"
Write-Host "[2/2] Starting Vite Frontend on http://localhost:5173..." -ForegroundColor Yellow
Start-Process -FilePath "cmd.exe" -ArgumentList "/k cd /d `"$frontendDir`" && set PATH=C:\Users\konga\.local\bin;%PATH% && npm run dev"

Write-Host "`nServices Initialized Successfully!" -ForegroundColor Green
Write-Host "Frontend Dashboard: http://localhost:5173" -ForegroundColor White
Write-Host "Interactive API Docs: http://127.0.0.1:8000/docs" -ForegroundColor White
Write-Host "Default Demo Login: investor@stockpulse.ai / stockpulse2026`n" -ForegroundColor DarkGray
