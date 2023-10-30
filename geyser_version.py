import os, subprocess, re

CWD = os.getcwd()
os.chdir(os.path.dirname(__file__))
os.chdir('test-Standalone')

JAVA_HOME = os.getenv('JAVA_HOME')
if JAVA_HOME == None:
    JAVA_PATH = 'java'
else:
    JAVA_PATH = os.path.join(JAVA_HOME,'bin/java')

try:
    geyser_version = re.search(
        "\\S+ \\(git-\\S+\\) [^\\n]+" ,
        subprocess.run(
            [JAVA_PATH ,'-Duser.language=en','-Duser.region=US','-Xmx256M','-jar','Geyser-roolback-for-mojang-login-Standalone.jar','nogui'],
            #encoding = 'ascii',
            input = b'geyser version\ngeyser stop',
            capture_output = True
        ).stdout.decode('ascii','ignore')
    ).group()
except:
    geyser_version = None

print(geyser_version)
os.chdir(CWD)
