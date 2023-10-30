print('Geyser-roolback-for-mojang-login-builder')

started_gradlew = False

import os, sys, shutil, stat, glob, time

start_time = time.time()

def print_timer():
    t = time.time() - start_time
    out = ['builder timer:']
    need_append = False

    d = int(t // 86400)
    if d:
        need_append = True
        out.append(f"{d}d")

    h = int((t // 3600) % 24)
    if h: need_append = True
    if need_append: out.append(f'{h}h')

    m = int((t // 60) % 60)
    if m: need_append = True
    if need_append: out.append(f'{m}m')

    out.append(f'{round( t % 60 ,3 )}s')

    print(' '.join(out) ,end='\n\n')


def exists_remove(path):
    if os.path.exists(path):
        def readonly_handler(func, path, execinfo):
            os.chmod(path, stat.S_IWRITE)
            func(path)
        if os.path.isdir(path):
            shutil.rmtree(path, onerror=readonly_handler)
        else:
            try:
                os.remove(path)
            except PermissionError:
                readonly_handler(os.remove, path)
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
    if WIN32:
        command += ' <nul'
    print('$>', command)
    e = os.system(command)
    if e != 0 and if_error_exit:
        exit(e)
    return e


try:
    os.chdir(os.path.dirname(__file__))

    e = os.system('git log -n 1 --pretty=format:git-%h')
    if e == 9009 :
        print('\nGit not found\n')
        exit(e)
    del e

    JAVA_HOME = os.getenv('JAVA_HOME')
    if JAVA_HOME == None:
        print('\nJAVA_HOME not found\n')
        exit(1)

    WIN32 = sys.platform == "win32"

    if WIN32:
        os.system('title Geyser-roolback-for-mojang-login-builder')



    ignore_clone_geyser = False

    for i in sys.argv:
        if i == 'ignore-clone-geyser':
            ignore_clone_geyser = True

    if not ignore_clone_geyser:
        print('\n# Clone Geyser')
        if os.path.exists("build/Geyser-roolback-for-mojang-login/"):
            os.chdir("build/Geyser-roolback-for-mojang-login")
            cmd('gradlew -stop', False)
            os.chdir('../../')
            exists_remove("build/")
        cmd('git clone https://github.com/GeyserMC/Geyser build/Geyser-roolback-for-mojang-login')



    print('\n# Build Geyser')

    os.chdir("build/Geyser-roolback-for-mojang-login")
    if not ignore_clone_geyser:
        cmd('git revert 7983448ce637656db1fca95eb65344a8c6d90de3 --no-edit')
        cmd('git submodule update --init --recursive')

    cmd('git remote set-url origin --push https://github.com/bddjr/Geyser-roolback-for-mojang-login', False)
    cmd('git remote set-url origin --push --add https://gitee.com/bddjr/Geyser-roolback-for-mojang-login', False)

    started_gradlew = True
    cmd('gradlew build')
    cmd('gradlew -stop')
    started_gradlew = False



    print('\n# Copy jar to dist/jar/')

    os.chdir('../../')

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
            if not os.path.exists("test-Standalone/start.bat"):
                with open("test-Standalone/start.bat", 'x') as f:
                    f.write(
'''"{}" -Xmx256M -jar Geyser-roolback-for-mojang-login-Standalone.jar nogui
pause
'''.format( os.path.join(JAVA_HOME,'bin/java') )
                    )



    print('\n# Get Geyser version')

    from geyser_version import geyser_version


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
        f.write(f_cache)



    print("\n# Completed.\nExported to dist folder.")
    print_timer()

except KeyboardInterrupt:
    print('\n^C (builder.py)')
    if started_gradlew:
        cmd('gradlew -stop', False)
    print_timer()
    exit(-1073741510)
