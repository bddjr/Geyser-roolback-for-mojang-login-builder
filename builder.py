if __name__ != "__main__":
    raise 'Running as a module is not supported.'

print(
'''Geyser-roolback-for-mojang-login-builder
Github repository: https://github.com/bddjr/Geyser-roolback-for-mojang-login-builder
''')

import os, sys, time
from mytools.file_tools import *

JAVA_HOME = os.getenv('JAVA_HOME')
if JAVA_HOME == None:
    print('\nJAVA_HOME not found\n')
    exit(1)

WIN32 = sys.platform == "win32"
if WIN32:
    os.system('title Geyser-roolback-for-mojang-login-builder', False)
    gradlew_name = 'gradlew'
else:
    gradlew_name = './gradlew'



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
    cd(os.path.abspath(os.path.dirname(__file__)))

    # version
    e = cmd('git log -n 1 --pretty=format:git-%h', False)
    if e == 9009 :
        print('\nGit not found\n')
        exit(e)
    del e


    # command args
    ignore_clone_geyser = False
    clash_proxy_mode = False
    gradlew_args = ''
    git_clone_args = ''

    for i in sys.argv:
        if i == 'ignore-clone':
            ignore_clone_geyser = True
        elif i == 'clash-proxy':
            clash_proxy_mode = True
            gradlew_args = '-DsocksProxyHost=127.0.0.1 -DsocksProxyPort=7890'
            git_clone_args = '-c http.proxy=socks5://127.0.0.1:7890'



    if not ignore_clone_geyser:
        print('\n# Clone Geyser')
        if os.path.exists("build/Geyser-roolback-for-mojang-login/"):
            cd("build/Geyser-roolback-for-mojang-login")
            cmd(f'{gradlew_name} -stop', False)
            cd('../../')
            exists_remove("build/")
        cmd(f'git clone {git_clone_args} https://github.com/GeyserMC/Geyser build/Geyser-roolback-for-mojang-login')



    print('\n# Build Geyser')

    cd("build/Geyser-roolback-for-mojang-login")
    if not ignore_clone_geyser:
        cmd('git config --unset user.name', False)
        if cmd('git config user.name', False) != 0 :
            cmd('git config user.name anonymous')

        cmd('git config --unset user.email', False)
        if cmd('git config user.email', False) != 0 :
            cmd('git config user.email "anonymous@example.com"')

        cmd('git revert 7983448ce637656db1fca95eb65344a8c6d90de3 --no-edit')
        cmd('git config --unset user.name', False)
        cmd('git config --unset user.email', False)

        if clash_proxy_mode:
            cmd('git config http.proxy socks5://127.0.0.1:7890')
            cmd('git config https.proxy socks5://127.0.0.1:7890')
        else:
            cmd('git config --unset http.proxy', False)
            cmd('git config --unset https.proxy', False)

        cmd('git submodule update --init --recursive')
        if clash_proxy_mode:
            cmd('git config --unset http.proxy', False)
            cmd('git config --unset https.proxy', False)

    if 0 == cmd('git remote set-url origin --push https://github.com/bddjr/Geyser-roolback-for-mojang-login', False):
        cmd('git remote set-url origin --push --add https://gitee.com/bddjr/Geyser-roolback-for-mojang-login', False)

    cmd(f'{gradlew_name} {gradlew_args} build')
    cmd(f'{gradlew_name} -stop')

    cd('../../')

    from mytools.dist import OK


    print("\n# Completed.\nExported to dist folder.")
    print_timer()

except KeyboardInterrupt:
  while True:
    try:
        print('''
^C (builder.py)
Stoping builder, please wait a moment!'''
        )
        cd(os.path.abspath(os.path.dirname(__file__)))
        cd("build/Geyser-roolback-for-mojang-login")
        cmd('git config --unset user.email', False)
        cmd('git config --unset user.name', False)
        cmd('git config --unset http.proxy', False)
        cmd('git config --unset https.proxy', False)
        cmd(f'{gradlew_name} -stop', False)

        print_timer()
        exit(-1073741510)
    except KeyboardInterrupt:
        pass
