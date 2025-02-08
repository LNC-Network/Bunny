@echo off
setlocal

:: Check if Python is installed
python --version >nul 2>&1 || py --version >nul 2>&1 || python3 --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not installed
    exit /b 1
)

:: Install dependencies
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install requirements
    exit /b 1
)

:: Build with PyInstaller
pyinstaller --onefile src/main.py
if %errorlevel% neq 0 (
    echo Failed to build
    exit /b 1
)

echo Build successful!

:: Delete the "build" folder
if exist build (
    rmdir /s /q build
    if %errorlevel% neq 0 (
        echo Failed to clear build folder
        exit /b 1
    )
)

exit /b 0

