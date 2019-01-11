import os
import subprocess


def common_folder_paths(pwd):
    tmp_dir = pwd + "/tmp"
    log_dir = tmp_dir + "/log/"
    outbase = tmp_dir + "/out/"

    return outbase, tmp_dir, log_dir


def get_cmake_build_base(env):
    cmakeb_dir = env["TMP_DIR"]+"/cmake-build/"
    return cmakeb_dir


def get_sstate_base_dir(env):
    sstate_dir = env["TMP_DIR"]+"/sstate/"
    return sstate_dir


def sstate_prebuild_check():
    env = os.environ.copy()
    outbase, tmp_dir, log_dir = common_folder_paths(env["PWD"])
    env["TMP_DIR"] = tmp_dir
    env["LOG_DIR"] = log_dir

    # create common folders if not exists
    subprocess.run(["mkdir", "-p", outbase, tmp_dir, log_dir])

    #folder to check if someone deletes the out folder
    outckdir = outbase + "/.sstate-chk/"

    # if out directory is deleted, then delete sstate cache & cmake build dirs
    if not os.path.exists(outckdir):
        sstbsdir = get_sstate_base_dir(env)
        cmkbsdir = get_cmake_build_base(env)
        subprocess.run(["rm", "-rf", sstbsdir, cmkbsdir])
        subprocess.run(["mkdir", "-p", outckdir, sstbsdir, cmkbsdir])


def get_sstate_cache_info(env, sstbase, pkg, func):
    domain = env["DOMAIN"]
    cache_dir = sstbase+"/"+domain+"/"+pkg
    cachefile = sstbase+"/"+domain+"/"+pkg+"/"+func
    return cache_dir, cachefile


def sstate_check(env, pkg, func):
    sstbsdir = get_sstate_base_dir(env)
    cached, cachef = get_sstate_cache_info(env, sstbsdir, pkg, func)
    return os.path.exists(cachef)


def sstate_done(env, pkg, func):
    cached, cachef = get_sstate_cache_info(env, get_sstate_base_dir(env), pkg, func)
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
