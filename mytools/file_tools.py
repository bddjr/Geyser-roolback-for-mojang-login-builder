import os, stat, shutil

def exists_remove(path):
    print('$rm', path)
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
    print('$mkdir', path)
    os.mkdir(path)

def not_exists_mkdir(path):
    if not os.path.exists(path):
        print('$mkdir', path)
        os.mkdir(path)
        return True
    return False

def cd(p):
    print('$cd', p)
    os.chdir(p)

def cd_absdir(p):
    cd(os.path.abspath(os.path.dirname(p)))
