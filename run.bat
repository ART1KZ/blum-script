@echo off
:menu
cls

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
