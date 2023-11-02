OK = "OK"

print('\n# Copy jar to dist/jar/')


import os, glob, shutil, sys


__name_for_import__ = ''
if __name__ == "__main__":
    from file_tools import *
else:
    rfind = __name__.rfind(".")
    if rfind > 0:
        try:
            __name_for_import__ = __name__[ : rfind+1 ]
        except: pass
    del rfind

    exec(f"from {__name_for_import__}file_tools import *")


JAVA_HOME = os.getenv('JAVA_HOME')
if JAVA_HOME == None:
    JAVA_PATH = 'java'
else:
    JAVA_PATH = os.path.join(JAVA_HOME,'bin','java')


WIN32 = sys.platform == "win32"



CWD = os.getcwd()
cd_absdir(__file__)
cd('..')


make_clear_dir("dist/")
os.mkdir("dist/jar")
exists_remove("test-Standalone/Geyser-roolback-for-mojang-login-Standalone.jar")


for i in glob.glob("build/Geyser-roolback-for-mojang-login/bootstrap/*/build/libs/Geyser-*"):
    name_ends = i[i.rfind('-') : ]
    out_name = "dist/jar/Geyser-roolback-for-mojang-login" + name_ends
    print(out_name)
    shutil.copy(i, out_name)
    if name_ends == "-Standalone.jar":
        not_exists_mkdir("test-Standalone/")
        shutil.copy(i, "test-Standalone/Geyser-roolback-for-mojang-login-Standalone.jar")
        geyser_start_command = f'"{JAVA_PATH}" -Xmx256M -jar Geyser-roolback-for-mojang-login-Standalone.jar nogui'
        if WIN32:
            if not os.path.exists("test-Standalone/start.bat"):
                with open("test-Standalone/start.bat", 'x') as f:
                    f.write(geyser_start_command + '\npause\n')
        elif not os.path.exists("test-Standalone/start.sh"):
            with open("test-Standalone/start.sh", 'x') as f:
                f.write(geyser_start_command + '\n')


if __name__ == "__main__":
    from geyser_version import geyser_version
else:
    exec(f"from {__name_for_import__}geyser_version import geyser_version")

print('\n# Export dist/release.md')

with open("dist/release.md", 'w') as f:
    f_cache = (
'''Please use [JDK-17](https://www.oracle.com/java/technologies/downloads/#java17) to run it.

Use [Geyser-roolback-for-mojang-login-builder](https://github.com/bddjr/Geyser-roolback-for-mojang-login-builder) to build.
'''
    )
    if geyser_version != None:
        f_cache = (
f'''```
{geyser_version}
```

{f_cache}'''
    )
    print(f'\n{f_cache}\n')
    f.write(f_cache)


cd(CWD)
