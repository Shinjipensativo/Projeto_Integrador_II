@echo off
title AcessoLab
cd /d "%~dp0src\web"

where python >nul 2>nul
if %errorlevel%==0 (
    python -m pip install -r requirements.txt
    python app.py
) else (
    py -m pip install -r requirements.txt
    py app.py
)

pause
