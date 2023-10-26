title Geyser-roolback-for-mojang-login-builder
cd /d %~dp0

rmdir /S /Q build\

git clone -b build https://github.com/bddjr/Geyser-roolback-for-mojang-login-builder build
if %errorlevel% neq 0 goto PAUSE

cd build
run-build.bat

:PAUSE
pause
