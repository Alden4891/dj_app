@echo off
setlocal

rem Check if MySQL server is running
tasklist /FI "IMAGENAME eq mysqld.exe" 2>NUL | find /I /N "mysqld.exe">NUL
if "%ERRORLEVEL%"=="1" (
    echo MySQL server is not running. Starting MySQL server...
    start "" "C:\xampp\mysql\bin\mysqld.exe" --console
) else (
    echo MySQL server is already running.
)

rem Activate the virtual environment
call venv\Scripts\activate

python manage.py makemigrations
python manage.py migrate

rem Deactivate the virtual environment
deactivate

pause