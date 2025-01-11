@echo off
:menu
cls

echo Hi, this is a script for blum! Below is the main menu.
@echo.

echo =================== Menu =====================================
<<<<<<< HEAD
echo 1. Run script without freezes
echo 2. Run script with freezes
echo 3. Exit
=======
echo 1. Run script
echo 2. Exit
>>>>>>> b767d33c979e18e1c6078af84d8573506628926f
echo ==============================================================
set /p choice=Enter a number (1-2): 

<<<<<<< HEAD
if "%choice%"=="1" goto no-freezes
if "%choice%"=="2" goto freezes
if "%choice%"=="3" goto exit
echo Invalid choice
goto menu

:no-freezes
cd script
python no-freezes.py
=======
if "%choice%"=="1" goto script
if "%choice%"=="2" goto exit
echo Invalid choice
goto menu


:script
cd script
python script.py
>>>>>>> b767d33c979e18e1c6078af84d8573506628926f
goto menu

:freezes
cd script
python freezes.py
goto menu


:exit
exit
