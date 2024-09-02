@echo off
:menu
chcp 65001
cls

echo Привет, это скрипт для блума! Автор скрипта - https://funpay.com/users/3305353/. Ниже представлено меню
@echo.
echo Hi, this is a script for blum! The author of the script is https://funpay.com/users/3305353/. Below is the menu
@echo.

echo =================== Menu =====================================
echo 1. Запустить скрипт с заморозками / Run script with freezes
echo 2. Запустить скрипт без заморозок / Run script without freezes
echo 3. Выход / Exit
echo ==============================================================
set /p choice=Введите число / Enter a number (1-3): 

if "%choice%"=="1" goto script1
if "%choice%"=="2" goto script2
if "%choice%"=="3" goto exit
echo Вы ввели неверное числоInvalid choice
goto menu

:script1
cd blum-script
python freezes.py
goto menu

:script2
cd blum-script
python no-freezes.py
goto menu

:exit
exit