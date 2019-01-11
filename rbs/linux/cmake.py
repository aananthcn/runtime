import subprocess
import rbsutils


# TODO: Please use the following function for all build directories for cmake based project!!
# rational: This will help engineers to rebuild from scratch if something needs to be changed
def get_cmake_build_dir(env, pkg, domain):
    build_dir = env["TMP_DIR"]+"/cmake-build/"+domain+"/"+pkg+"/"+"/build"
    return build_dir


def get_config_cmd(env):
    out_dir = env["OUT_DIR"]
    inst_arg = "-DCMAKE_INSTALL_PREFIX="+out_dir
    find_arg = "-DCMAKE_FIND_ROOT_PATH="+out_dir

    cmd = "cmake "+inst_arg+" "+find_arg+" .."
    return cmd



def config_package(conf, env, pkg):
    print("\n$$ Configuring %s" % pkg)
    pkgd = conf["packages"]["path"]+"/"+pkg
    domain = env["DOMAIN"]
    env["LD_LIBRARY_PATH"] = env["OUT_DIR"]+"/lib"

    cmd = get_config_cmd(env)
    build_dir = env["PWD"]+"/"+pkgd+"/build-"+domain
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
    pkgd = conf["packages"]["path"]+"/"+pkg
    build_dir = env["PWD"]+"/"+pkgd+"/build-"+env["DOMAIN"]
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
    pkgd = conf["packages"]["path"]+"/"+pkg
    build_dir = env["PWD"]+"/"+pkgd+"/build-"+env["DOMAIN"]
    cmd = "make install"

    try:
        print(cmd)
        outstr = subprocess.run(cmd, shell=True, cwd=build_dir, check=True, stdout=subprocess.PIPE, env=env)
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


