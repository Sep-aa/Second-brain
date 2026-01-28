@echo off

call .venv\Scripts\activate.bat
echo .venv\Scripts\activate.bat
pause
echo.

cd /d "%~dp0..\second_brain"
python manage.py runserver
pause