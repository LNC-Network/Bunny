@echo off
setlocal enabledelayedexpansion

:: Run build script
call build.bat
if %errorlevel% neq 0 (
    echo Build process failed.
    exit /b 1
)

:: Ask user for installation directory
echo Choose installation directory:
echo 1. Install for current user (%USERPROFILE%\AppData\Local\Programs\MyApp)
echo 2. Install for all users (C:\Program Files\MyApp) [Admin required]
set /p choice="Enter 1 or 2: "

if "%choice%"=="1" (
    set install_dir=%USERPROFILE%\AppData\Local\Programs\MyApp
) else if "%choice%"=="2" (
    set install_dir=C:\Program Files\MyApp
    echo Admin rights required for system installation.
    powershell -Command "Start-Process cmd -ArgumentList '/c %~f0' -Verb RunAs"
    exit /b 0
) else (
    echo Invalid choice, defaulting to user installation.
    set install_dir=%USERPROFILE%\AppData\Local\Programs\MyApp
)

mkdir "%install_dir%" 2>nul
if %errorlevel% neq 0 (
    echo Failed to create install directory.
    exit /b 1
)

:: Move built executable
move /y "dist\main.exe" "%install_dir%\main.exe"
if %errorlevel% neq 0 (
    echo Failed to move executable.
    exit /b 1
)

:: Add to PATH (avoid overwriting PATH)
for /f "tokens=2*" %%a in ('reg query "HKCU\Environment" /v Path 2^>nul') do set OLD_PATH=%%b
set NEW_PATH=!OLD_PATH!;%install_dir%
reg add "HKCU\Environment" /v Path /t REG_EXPAND_SZ /d "!NEW_PATH!" /f >nul 2>&1

echo Installation complete! Restart your terminal and run "main".
exit /b 0
