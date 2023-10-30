import os, subprocess, re

CWD = os.getcwd()
os.chdir(os.path.dirname(__file__))
os.chdir('test-Standalone')

JAVA_HOME = os.getenv('JAVA_HOME')
if JAVA_HOME == None:
    JAVA_PATH = 'java'
else:
    JAVA_PATH = os.path.join(JAVA_HOME,'bin/java')

java_command = ['java' if JAVA_HOME==None else os.path.join(JAVA_HOME,'bin/java') ,'-Duser.language=en','-Duser.region=US','-Xmx256M','-jar','Geyser-roolback-for-mojang-login-Standalone.jar','nogui']

try:
    print('$>', *java_command)
    run = subprocess.run(
        java_command,
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
os.chdir(CWD)
