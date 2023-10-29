import os, subprocess, re

os.chdir('test-Standalone')

try:
    geyser_version = re.search(
        "\\S+ \\(git-\\S+\\) [^\\n]+" ,
        subprocess.run(
            ['java','-Duser.language=en','-Duser.region=US','-Xmx256M','-jar','Geyser-roolback-for-mojang-login-Standalone.jar','nogui'],
            encoding = 'ascii',
            input = 'geyser version\ngeyser stop',
            stdout = subprocess.PIPE,
        ).stdout
    ).group()

except:
    geyser_version = None

print(geyser_version)
