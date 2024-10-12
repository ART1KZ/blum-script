@echo off
:menu
cls

echo Hi, this is a script for blum! The author of the script is https://funpay.com/users/3305353/. Below is the menu
@echo.

echo =================== Menu =====================================
echo 1. Run script with freezes
echo 2. Run script without freezes
echo 3. Exit
echo ==============================================================
set /p choice=Enter a number (1-3): 

if "%choice%"=="1" goto script1
if "%choice%"=="2" goto script2
if "%choice%"=="3" goto exit
echo Invalid choice
goto menu


:script1
python freezes.py
goto menu

:script2
python no-freezes.py
goto menu

:exit
exit
