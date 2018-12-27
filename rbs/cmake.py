import subprocess


def get_cmake_config_list(conf, env, domain):
    cfg_list = []
    out_dir = env["OUT_DIR"]
    inst_arg = "-DCMAKE_INSTALL_PREFIX:PATH="+out_dir
    if domain == "Linux":
        cfg_list = ["cmake", inst_arg, ".."]
    elif domain == "QNX":
        c_arg = "-DCMAKE_C_COMPILER="+conf["toolchain"][domain]["prefix"]+"gcc"
        cpp_arg = "-DCMAKE_CXX_COMPILER="+conf["toolchain"][domain]["prefix"]+"g++"
        find_arg = "-DCMAKE_FIND_ROOT_PATH="+out_dir
        cfg_list = ["cmake", inst_arg, c_arg, cpp_arg, find_arg, ".."]
        print(cfg_list)
    else:
        print("RBS Error: invalid domain - get_cmake_config_list()!")
        exit(-1)

    return cfg_list



def config_package(conf, env, pkg):
    print("Configuring %s" % pkg)
    pkgd = conf["packages"]["path"]+"/"+pkg
    domain = env["DOMAIN"]
    cfg_list = get_cmake_config_list(conf, env, domain)
    build_dir = env["PWD"]+"/"+pkgd+"/build-"+domain
    subprocess.run(["mkdir", "-p", build_dir], stdout=subprocess.PIPE, env=env)
    outstr = subprocess.run(cfg_list, stdout=subprocess.PIPE, env=env, cwd=build_dir).stdout.decode('utf-8')
    print(outstr)


def compile_package(conf, env, pkg):
    print("Compiling %s" % (pkg))
    pkgd = conf["packages"]["path"]+"/"+pkg
    build_dir = env["PWD"]+"/"+pkgd+"/build-"+env["DOMAIN"]
    outstr = subprocess.run(["make", "-C", build_dir], stdout=subprocess.PIPE, env=env).stdout.decode('utf-8')
    print(outstr)


def install_package(conf, env, pkg):
    print("Installing %s" % (pkg))
    pkgd = conf["packages"]["path"]+"/"+pkg


def run_package(conf, env, pkg, cmd):
    print("Running %s with command %s" % (pkg, cmd))
    pkgd = conf["packages"]["path"]+"/"+pkg


