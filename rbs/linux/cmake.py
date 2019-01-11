import subprocess
import rbsutils


def get_cmake_build_dir(env, pkg):
    return rbsutils.get_cmake_build_base(env)+env["DOMAIN"]+"/"+pkg


def get_config_cmd(env, pkgd):
    out_dir = env["OUT_DIR"]
    inst_arg = "-DCMAKE_INSTALL_PREFIX="+out_dir
    find_arg = "-DCMAKE_FIND_ROOT_PATH="+out_dir

    cmd = "cmake "+inst_arg+" "+find_arg+" "+pkgd
    return cmd



def config_package(conf, env, pkg):
    print("\n$$ Configuring %s" % pkg)
    pkgd = env["PWD"]+"/"+conf["packages"]["path"]+"/"+pkg
    env["LD_LIBRARY_PATH"] = env["OUT_DIR"]+"/lib"

    cmd = get_config_cmd(env, pkgd)
    build_dir = get_cmake_build_dir(env, pkg)
    subprocess.run(["mkdir", "-p", build_dir], stdout=subprocess.PIPE, env=env)

    try:
        print(cmd)
        outstr = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, check=True, env=env, cwd=build_dir)
        logdata = outstr.stdout.decode('utf-8')
        rbsutils.log_data(env, pkg, "config", logdata)
        print(logdata)

    except subprocess.CalledProcessError as e:
        logdata = "\n\nLOG:\n" + e.stdout.decode('utf-8')
        rbsutils.log_data(env, pkg, "config", logdata)
        print(logdata)
        return False

    return True


def compile_package(conf, env, pkg):
    print("\n$$ Compiling %s" % (pkg))
    build_dir = get_cmake_build_dir(env, pkg)
    cmd = "make -j8 VERBOSE=1 -C " + build_dir

    try:
        print(cmd)
        outstr = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, env=env)
        logdata = outstr.stdout.decode('utf-8')
        rbsutils.log_data(env, pkg, "compile", logdata)
        print(logdata)

    except subprocess.CalledProcessError as e:
        logdata = "\n\nLOG:\n" + e.stdout.decode('utf-8')
        rbsutils.log_data(env, pkg, "compile", logdata)
        print(logdata)
        return False

    return True


def install_package(conf, env, pkg):
    print("\n$$ Installing %s" % (pkg))
    build_dir = get_cmake_build_dir(env, pkg)
    cmd = "make install -C " + build_dir

    try:
        print(cmd)
        outstr = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, env=env)
        logdata = outstr.stdout.decode('utf-8')
        rbsutils.log_data(env, pkg, "install", logdata)
        print(logdata)

    except subprocess.CalledProcessError as e:
        logdata = "\n\nLOG:\n" + e.stdout.decode('utf-8')
        rbsutils.log_data(env, pkg, "install", logdata)
        print(logdata)
        return False

    return True


def run_package(conf, env, pkg, cmd):
    print("\n$$ Running %s with command %s" % (pkg, cmd))
    pkgd = conf["packages"]["path"]+"/"+pkg
    build_dir = env["PWD"]+"/"+pkgd+"/build-"+env["DOMAIN"]
    outstr = subprocess.run(["make", cmd], cwd=build_dir, stdout=subprocess.PIPE, env=env)
    print(outstr.stdout.decode('utf-8'))


