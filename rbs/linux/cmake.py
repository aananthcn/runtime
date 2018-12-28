import subprocess


def get_cmake_config_list(conf, env, domain):
    out_dir = env["OUT_DIR"]
    inst_arg = "-DCMAKE_INSTALL_PREFIX:PATH="+out_dir

    cfg_list = ["cmake", inst_arg, ".."]
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
    build_dir = env["PWD"]+"/"+pkgd+"/build-"+env["DOMAIN"]
    outstr = subprocess.run(["make", cmd], cwd=build_dir, stdout=subprocess.PIPE, env=env).stdout.decode('utf-8')
    print(outstr)


