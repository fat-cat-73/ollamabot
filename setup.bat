@echo off
setlocal

set python=python

:: Create virtual environment
%python% -m venv venv

:: Activate virtual environment
call venv\Scripts\activate

:: Upgrade pip
%python% -m pip install --upgrade pip

:: Install dependencies
%python% -m pip install -r requirements.txt

echo Setup complete. You can now run the 'start.bat' file.
pause
