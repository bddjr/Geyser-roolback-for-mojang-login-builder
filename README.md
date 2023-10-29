# Geyser-roolback-for-mojang-login-builder
Restore mojang login related files.  

> git revert [7983448ce637656db1fca95eb65344a8c6d90de3](https://github.com/GeyserMC/Geyser/commit/7983448ce637656db1fca95eb65344a8c6d90de3)  

***
## run

### Windows
1.  Install  
> [Git for Windows](https://gitforwindows.org/)  
> [JDK-17](https://www.oracle.com/java/technologies/downloads/#jdk17-windows)  
> [Python 3](https://www.python.org/downloads/windows/)  

2.  JAVA_HOME (default path)
```
setx /M JAVA_HOME "C:\Program Files\Java\jdk-17"
```

3.  git clone
```
git clone https://github.com/bddjr/Geyser-roolback-for-mojang-login-builder
```

4.  Change Directory
```
cd Geyser-roolback-for-mojang-login-builder
```

5.  build
```
python builder.py
```

### Linux
1.  Install
> [Git](https://git-scm.com/)  
> [JDK-17](https://www.oracle.com/java/technologies/downloads/#jdk17-linux)  
> [Python 3](https://www.python.org/)  

2.  JAVA_HOME
> (to be continued...)  

3.  git clone
```
git clone https://github.com/bddjr/Geyser-roolback-for-mojang-login-builder
```

4.  Change Directory
```
cd Geyser-roolback-for-mojang-login-builder
```

5.  build
```
python3 builder.py
```
