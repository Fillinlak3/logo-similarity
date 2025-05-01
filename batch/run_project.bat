@echo off
echo Running Logo Similarity Project (py v3.10)...

cd ..
call logosim_env\Scripts\activate.bat

call logosim_env\Scripts\python.exe -m logosim.main

pause
