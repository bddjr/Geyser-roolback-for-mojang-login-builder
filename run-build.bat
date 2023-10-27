if exist Geyser-roolback-for-mojang-login\ rmdir /S /Q Geyser-roolback-for-mojang-login\
if exist Geyser-roolback-for-mojang-login\ goto PAUSE

git clone https://github.com/GeyserMC/Geyser Geyser-roolback-for-mojang-login
if %errorlevel% neq 0 goto PAUSE



cd Geyser-roolback-for-mojang-login

git revert 7983448ce637656db1fca95eb65344a8c6d90de3 --no-edit
if %errorlevel% neq 0 goto PAUSE

git submodule update --init --recursive
if %errorlevel% neq 0 goto PAUSE

git remote set-url origin --push https://github.com/bddjr/Geyser-roolback-for-mojang-login
git remote set-url origin --push --add https://gitee.com/bddjr/Geyser-roolback-for-mojang-login

cmd /c gradlew build
if %errorlevel% neq 0 goto PAUSE



cd ..

python run-copy.py
if %errorlevel% neq 0 goto PAUSE

cd ..
explorer dist\

:PAUSE
pause
