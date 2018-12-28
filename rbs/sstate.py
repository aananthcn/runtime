import os
import subprocess


def sstate_check(env, pkg, func):
    outdir = env["PWD"]+"/out/"+"/sstate-chk" #folder to check if someone deletes the out folder
    sstdir = env["TMP_DIR"]+"/sstate"
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
    sstdir = env["TMP_DIR"]+"/sstate"
    domain = env["DOMAIN"]
    cached = sstdir+"/"+domain+"/"+pkg
    cachef = sstdir+"/"+domain+"/"+pkg+"/"+func
    subprocess.run(["mkdir", "-p", cached])
    subprocess.run(["touch", cachef])
