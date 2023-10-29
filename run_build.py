OK = "OK"

import shutil, os, glob

def exists_remove(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
        return True
    return False

def make_clear_dir(path):
    exists_remove(path)
    os.mkdir(path)

def not_exists_mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)
        return True
    return False

def cmd(command, if_error_exit=True):
    print('>', command)
    e = os.system(command)
    if e != 0 and if_error_exit:
        exit(e)
    return e



print('# Clone Geyser')
exists_remove("Geyser-roolback-for-mojang-login/")
cmd('git clone https://github.com/GeyserMC/Geyser Geyser-roolback-for-mojang-login')

os.chdir("Geyser-roolback-for-mojang-login")
cmd('git revert 7983448ce637656db1fca95eb65344a8c6d90de3 --no-edit')
cmd('git submodule update --init --recursive')

cmd('git remote set-url origin --push https://github.com/bddjr/Geyser-roolback-for-mojang-login', False)
cmd('git remote set-url origin --push https://github.com/bddjr/Geyser-roolback-for-mojang-login', False)

cmd('gradlew build')



print('# Copy jar to dist')

os.chdir('../../')

make_clear_dir("dist/")
make_clear_dir("dist/jar/")
exists_remove("test-Standalone/Geyser-roolback-for-mojang-login-Standalone.jar")


for i in glob.glob("build/Geyser-roolback-for-mojang-login/bootstrap/*/build/libs/Geyser-*"):
    name_ends = i[i.rfind('-') : ]
    out_name = "dist/jar/Geyser-roolback-for-mojang-login" + name_ends
    print(out_name)
    shutil.copy(i, out_name)
    if name_ends == "-Standalone.jar":
        not_exists_mkdir("test-Standalone/")
        shutil.copy(i, "test-Standalone/Geyser-roolback-for-mojang-login-Standalone.jar")
        if not os.path.exists("test-Standalone/start.bat"):
            with open("test-Standalone/start.bat", 'x') as f:
                f.write(
'''java -Xmx256M -jar Geyser-roolback-for-mojang-login-Standalone.jar nogui
pause
'''
                )



print('# get Geyser version')

os.chdir('build')
from geyser_version import geyser_version

print('# dist/release.md')

with open("../dist/release.md", 'w') as f:
    f.write(
'''```
{}
```

Please use [JDK-17](https://www.oracle.com/java/technologies/downloads/#java17) to run it.

Use [Geyser-roolback-for-mojang-login-builder](https://github.com/bddjr/Geyser-roolback-for-mojang-login-builder) to build.
'''.format(geyser_version)
    )



print("# Completed.")
