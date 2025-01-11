@echo off
:menu
cls

echo Hi, this is a script for blum! Below is the main menu.
@echo.

echo =================== Menu =====================================
echo 1. Run script without freezes
echo 2. Run script with freezes
echo 3. Exit
echo ==============================================================
set /p choice=Enter a number (1-3): 

if "%choice%"=="1" goto no-freezes
if "%choice%"=="2" goto freezes
if "%choice%"=="3" goto exit
echo Invalid choice
goto menu

:no-freezes
cd script
python no-freezes.py
goto menu

:freezes
cd script
python freezes.py
goto menu


:exit
exit
