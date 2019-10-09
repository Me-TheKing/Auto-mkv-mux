@echo off

for %%a in (%*) do pyuic5 -x %%a -o %%~na.py 
pause