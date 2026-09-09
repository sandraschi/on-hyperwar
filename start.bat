@echo off
rem On Hyperwar - local book server (double-click friendly).
rem Builds site/ then serves it on http://localhost:10988/
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (
    echo Python launcher 'py' not found. Install Python 3 from https://www.python.org/downloads/
    pause
    exit /b 1
)
where just >nul 2>nul
if errorlevel 1 (
    echo 'just' not found. Install via: winget install Casey.Just
    pause
    exit /b 1
)
call just serve
pause
