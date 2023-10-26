title Geyser-roolback-for-mojang-login-builder
cd /d %~dp0

if exist build\ rmdir /S /Q build\
if exist build\ goto PAUSE

git clone -b build https://github.com/bddjr/Geyser-roolback-for-mojang-login-builder build
if %errorlevel% neq 0 goto PAUSE

cd build
run-build.bat
exit

:PAUSE
pause
