import subprocess
import rbsutils


# TODO: Please use the following function for all build directories for cmake based project!!
# rational: This will help engineers to rebuild from scratch if something needs to be changed
def get_cmake_build_dir(env, pkg, domain):
    build_dir = env["TMP_DIR"]+"/cmake-build/"+domain+"/"+pkg+"/"+"/build"
    return build_dir


def get_cmake_config_list(conf, env, domain):
    out_dir = env["OUT_DIR"]
    inst_arg = "-DCMAKE_INSTALL_PREFIX="+out_dir
    find_arg = "-DCMAKE_FIND_ROOT_PATH="+out_dir
    tool_arg = "-DCMAKE_TOOLCHAIN_FILE="+env["PWD"]+"/config/cmake/qnx7.0.0_"+env["ARCH"]+".cmake"

    cfg_list = ["cmake", inst_arg, find_arg, tool_arg, ".."]
    print(cfg_list)
    return cfg_list



def config_package(conf, env, pkg):
    print("\n$$ Configuring %s" % pkg)
    pkgd = conf["packages"]["path"]+"/"+pkg
    domain = env["DOMAIN"]

    cfg_list = get_cmake_config_list(conf, env, domain)
    build_dir = env["PWD"]+"/"+pkgd+"/build-"+domain
    subprocess.run(["mkdir", "-p", build_dir], stdout=subprocess.PIPE, env=env)

    try:
        outstr = subprocess.run(cfg_list, stdout=subprocess.PIPE, check=True, env=env, cwd=build_dir)
        logdata = outstr.stdout.decode('utf-8')
        rbsutils.log_data(env, pkg, "config", logdata)
        print(logdata)
        print(outstr.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        return False

    return True


def compile_package(conf, env, pkg):
    print("\n$$ Compiling %s" % (pkg))
    pkgd = conf["packages"]["path"]+"/"+pkg
    build_dir = env["PWD"]+"/"+pkgd+"/build-"+env["DOMAIN"]

    try:
        outstr = subprocess.run(["make", "-j8", "VERBOSE=1", "-C", build_dir], check=True, stdout=subprocess.PIPE, env=env)
        logdata = outstr.stdout.decode('utf-8')
        rbsutils.log_data(env, pkg, "compile", logdata)
        print(logdata)
    except subprocess.CalledProcessError as e:
        print("\n\nLOG:\n" + e.stdout.decode('utf-8'))
        return False

    return True


def install_package(conf, env, pkg):
    print("\n$$ Installing %s" % (pkg))
    pkgd = conf["packages"]["path"]+"/"+pkg
    build_dir = env["PWD"]+"/"+pkgd+"/build-"+env["DOMAIN"]

    try:
        outstr = subprocess.run(["make", "install"], cwd= build_dir, check=True, stdout=subprocess.PIPE, env=env)
        logdata = outstr.stdout.decode('utf-8')
        rbsutils.log_data(env, pkg, "install", logdata)
        print(logdata)
    except subprocess.CalledProcessError as e:
        print("\n\nLOG:\n" + e.stdout.decode('utf-8'))
        return False

    return True


def run_package(conf, env, pkg, cmd):
    print("\n$$ Running %s with command %s" % (pkg, cmd))
    pkgd = conf["packages"]["path"]+"/"+pkg
    build_dir = env["PWD"]+"/"+pkgd+"/build-"+env["DOMAIN"]
    outstr = subprocess.run(["make", cmd], cwd=build_dir, stdout=subprocess.PIPE, env=env)
    print(outstr.stdout.decode('utf-8'))
