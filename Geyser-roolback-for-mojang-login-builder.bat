title Geyser-roolback-for-mojang-login-builder
git clone https://github.com/bddjr/Geyser-roolback-for-mojang-login-release-replicator
git clone https://github.com/GeyserMC/Geyser Geyser-roolback-for-mojang-login
cd Geyser-roolback-for-mojang-login
git remote set-url origin https://github.com/bddjr/Geyser-roolback-for-mojang-login
git revert 7983448ce637656db1fca95eb65344a8c6d90de3
git submodule update --init --recursive
cmd /c gradlew build
cd ../Geyser-roolback-for-mojang-login-release-replicator
python run_copy.py
explorer dist
pause
