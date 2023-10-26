if exist Geyser-roolback-for-mojang-login\ rmdir /S /Q Geyser-roolback-for-mojang-login\
if exist Geyser-roolback-for-mojang-login\ exit

git clone https://github.com/GeyserMC/Geyser Geyser-roolback-for-mojang-login
if %errorlevel% neq 0 exit



cd Geyser-roolback-for-mojang-login

git revert 7983448ce637656db1fca95eb65344a8c6d90de3 --no-edit
if %errorlevel% neq 0 exit

git submodule update --init --recursive
if %errorlevel% neq 0 exit

git remote set-url origin https://github.com/bddjr/Geyser-roolback-for-mojang-login

cmd /c gradlew build
if %errorlevel% neq 0 exit



cd ..

python run-copy.py
if %errorlevel% neq 0 exit

cd ..
explorer dist\
