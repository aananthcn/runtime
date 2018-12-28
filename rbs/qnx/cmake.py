import subprocess


def get_cmake_config_list(conf, env, domain):
    out_dir = env["OUT_DIR"]
    inst_arg = "-DCMAKE_INSTALL_PREFIX="+out_dir
    find_arg = "-DCMAKE_FIND_ROOT_PATH="+out_dir
    tool_arg = "-DCMAKE_TOOLCHAIN_FILE="+env["PWD"]+"/config/cmake/qnx7.0.0_x86_64.cmake"

    # cmake -DCMAKE_INSTALL_PREFIX:PATH=/home/aananth/projects/runtime/out/QNX -DCMAKE_FIND_ROOT_PATH=/home/aananth/projects/runtime/out/QNX -DCMAKE_TOOLCHAIN_FILE=/home/aananth/projects/runtime/config/cmake/qnx7.0.0_x86_64.cmake ..
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
    outstr = subprocess.run(cfg_list, stdout=subprocess.PIPE, env=env, cwd=build_dir).stdout.decode('utf-8')
    print(outstr)


def compile_package(conf, env, pkg):
    print("\n$$ Compiling %s" % (pkg))
    pkgd = conf["packages"]["path"]+"/"+pkg
    build_dir = env["PWD"]+"/"+pkgd+"/build-"+env["DOMAIN"]
    outstr = subprocess.run(["make", "-j8", "-C", build_dir], stdout=subprocess.PIPE, env=env).stdout.decode('utf-8')
    print(outstr)


def install_package(conf, env, pkg):
    print("\n$$ Installing %s" % (pkg))
    pkgd = conf["packages"]["path"]+"/"+pkg


def run_package(conf, env, pkg, cmd):
    print("\n$$ Running %s with command %s" % (pkg, cmd))
    pkgd = conf["packages"]["path"]+"/"+pkg


