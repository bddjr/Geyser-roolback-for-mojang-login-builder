print('\n# Get Geyser version')

import os, subprocess, re

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

CWD = os.getcwd()
cd_absdir(__file__)
cd('../test-Standalone')

JAVA_HOME = os.getenv('JAVA_HOME')
if JAVA_HOME == None:
    JAVA_PATH = 'java'
else:
    JAVA_PATH = os.path.join(JAVA_HOME,'bin','java')

java_command = [JAVA_PATH,'-Duser.language=en','-Duser.region=US','-Xmx256M','-jar','Geyser-roolback-for-mojang-login-Standalone.jar','nogui']

try:
    print(f'$> "{java_command[0]}"', ' '.join(java_command[1:]))
    run = subprocess.run(
        java_command ,
        #encoding = 'ascii',
        input = b'geyser version\ngeyser stop',
        capture_output = True
    ).stdout.decode('ascii','ignore')
    print(run)
    geyser_version = re.search(
        "\\S+ \\(git-\\S+\\) [^\\n]+" ,
        run
    ).group()
except KeyboardInterrupt as e:
    raise e
except:
    geyser_version = None

print()
print(geyser_version)
cd(CWD)
