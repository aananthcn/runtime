import os
import subprocess


def get_sstate_dir(env):
    return env["TMP_DIR"]+"/sstate/"+env["ARCH"]+"/"


def sstate_check(env, pkg, func):
    outdir = env["OUT_DIR"]+"/.sstate-chk" #folder to check if someone deletes the out folder
    sstdir = get_sstate_dir(env)
    domain = env["DOMAIN"]

    # if out directory is deleted, then delete sstate cache
    if os.path.exists(outdir) == False:
        subprocess.run(["rm", "-rf", sstdir])
        subprocess.run(["mkdir", "-p", outdir, sstdir])
        # return False as we have deleted the cache
        return False

    # out directory is present, so check if cache file exists
    cachefile = sstdir+"/"+domain+"/"+pkg+"/"+func
    return os.path.exists(cachefile)


def sstate_done(env, pkg, func):
    sstdir = get_sstate_dir(env)
    domain = env["DOMAIN"]
    cached = sstdir+"/"+domain+"/"+pkg
    cachef = sstdir+"/"+domain+"/"+pkg+"/"+func
    subprocess.run(["mkdir", "-p", cached])
    subprocess.run(["touch", cachef])


def log_data(env, pkg, func, data):
    filepath = env["LOG_DIR"] + env["DOMAIN"] + "/"
    if not os.path.exists(filepath):
        subprocess.run(["mkdir", "-p", filepath])
    filename = filepath + "/" + pkg + "-" + func + ".log"
    file = open(filename, 'w')
    file.write(data)
    file.close()


def print_banner(str):
    column = len(str) + 10
    print("#" * column)
    print("##   %s   ##" % (str))
    print("#" * column)
