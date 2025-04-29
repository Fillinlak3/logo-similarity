@echo off
echo Installing project dependencies...
call ..\logosim_env\Scripts\activate
pip install -r ..\requirements.txt
pause