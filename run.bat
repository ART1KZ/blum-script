@echo off
:menu
cls

echo Hi, this is a script for blum! The author of the script is https://funpay.com/users/3305353/. Below is the menu
@echo.

echo =================== Menu =====================================
echo 1. Run script
echo 2. Exit
echo ==============================================================
set /p choice=Enter a number (1-2): 

if "%choice%"=="1" goto script
if "%choice%"=="2" goto exit
echo Invalid choice
goto menu


:script
cd script
python script.py
goto menu

:exit
exit
