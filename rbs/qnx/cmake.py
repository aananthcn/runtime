import subprocess


def get_cmake_config_list(conf, env, domain):
    out_dir = env["OUT_DIR"]
    inst_arg = "-DCMAKE_INSTALL_PREFIX="+out_dir
    find_arg = "-DCMAKE_FIND_ROOT_PATH="+out_dir
    tool_arg = "-DCMAKE_TOOLCHAIN_FILE="+env["PWD"]+"/config/cmake/qnx7.0.0_x86_64.cmake"

    # cmake -DCMAKE_INSTALL_PREFIX=./out/QNX -DCMAKE_FIND_ROOT_PATH=./out/QNX -DCMAKE_TOOLCHAIN_FILE=./config/cmake/qnx7.0.0_x86_64.cmake ..
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
        outstr = subprocess.run(cfg_list, stdout=subprocess.PIPE, check=True, env=env, cwd=build_dir).stdout.decode('utf-8')
    except subprocess.CalledProcessError:
        print(outstr)
        return False

    return True


def compile_package(conf, env, pkg):
    print("\n$$ Compiling %s" % (pkg))
    pkgd = conf["packages"]["path"]+"/"+pkg
    build_dir = env["PWD"]+"/"+pkgd+"/build-"+env["DOMAIN"]

    try:
        outstr = subprocess.run(["make", "-j8", "-C", build_dir], check=True, stdout=subprocess.PIPE, env=env).stdout.decode('utf-8')
    except subprocess.CalledProcessError:
        print(outstr)
        return False

    return True


def install_package(conf, env, pkg):
    print("\n$$ Installing %s" % (pkg))
    pkgd = conf["packages"]["path"]+"/"+pkg
    build_dir = env["PWD"]+"/"+pkgd+"/build-"+env["DOMAIN"]

    try:
        outstr = subprocess.run(["make", "install"], cwd= build_dir, check=True, stdout=subprocess.PIPE, env=env).stdout.decode('utf-8')
    except subprocess.CalledProcessError:
        print(outstr)
        return False

    return True

def run_package(conf, env, pkg, cmd):
    print("\n$$ Running %s with command %s" % (pkg, cmd))
    pkgd = conf["packages"]["path"]+"/"+pkg


