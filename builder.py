if __name__ != "__main__":
    raise 'Running as a module is not supported.'

print('Geyser-roolback-for-mojang-login-builder')

started_gradlew = False

import os, sys, time
from mytools.file_tools import *

JAVA_HOME = os.getenv('JAVA_HOME')
if JAVA_HOME == None:
    print('\nJAVA_HOME not found\n')
    exit(1)

WIN32 = sys.platform == "win32"
if WIN32:
    os.system('title Geyser-roolback-for-mojang-login-builder')



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



def cmd(command, if_error_exit=True):
    if WIN32:
        command += ' <nul' # ^C Y
    print('$>', command)
    e = os.system(command)
    if e != 0 and if_error_exit:
        exit(e)
    return e


try:
    os.chdir(os.path.dirname(__file__))

    # version
    e = os.system('git log -n 1 --pretty=format:git-%h')
    if e == 9009 :
        print('\nGit not found\n')
        exit(e)
    del e


    # command args
    ignore_clone_geyser = False
    gradlew_args = ''

    for i in sys.argv:
        if i == 'ignore-clone':
            ignore_clone_geyser = True
        elif i == 'gradlew-proxy':
            gradlew_args = '-DsocksProxyHost=127.0.0.1 -DsocksProxyPort=7890'
        elif i.startswith('-DsocksProxy'):
            gradlew_args += i + ' '



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
    cmd(f'gradlew {gradlew_args} build')
    cmd('gradlew -stop')
    started_gradlew = False

    os.chdir('../../')

    from mytools.dist import OK


    print("\n# Completed.\nExported to dist folder.")
    print_timer()

except KeyboardInterrupt:
    print('\n^C (builder.py)')
    if started_gradlew:
        cmd('gradlew -stop', False)
    print_timer()
    exit(-1073741510)
