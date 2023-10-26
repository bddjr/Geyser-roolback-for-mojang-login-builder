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


make_clear_dir("../dist/")
exists_remove("../test-Standalone/Geyser-roolback-for-mojang-login-Standalone.jar")


for i in glob.glob("Geyser-roolback-for-mojang-login/bootstrap/*/build/libs/Geyser-*"):
    name_ends = i[i.rfind('-') : ]
    out_name = "../dist/Geyser-roolback-for-mojang-login" + name_ends
    print(out_name)
    shutil.copy(i, out_name)
    if name_ends == "-Standalone.jar":
        not_exists_mkdir("../test-Standalone/")
        shutil.copy(i, "../test-Standalone/Geyser-roolback-for-mojang-login-Standalone.jar")
        if not os.path.exists("../test-Standalone/start.bat"):
            f = open("../test-Standalone/start.bat", 'x')
            f.write(
'''java -Xmx256M -jar Geyser-roolback-for-mojang-login-Standalone.jar
pause
'''
            )
            f.close()
            del f


print("OK!")
