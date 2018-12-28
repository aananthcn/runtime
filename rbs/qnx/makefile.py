import subprocess


def config_package(conf, env, pkg):
    print("\n$$ Configuring %s" % pkg)
    return True


def compile_package(conf, env, pkg):
    print("\n$$ Compiling %s" % (pkg))
    pkgd = conf["packages"]["path"]+"/"+pkg

    try:
        outstr = subprocess.run(["make", "-C", pkgd], stdout=subprocess.PIPE, env=env).stdout.decode('utf-8')
    except subprocess.CalledProcessError:
        print(outstr)
        return False

    return True



def install_package(conf, env, pkg):
    print("\n$$ Installing %s" % (pkg))
    pkgd = conf["packages"]["path"]+"/"+pkg

    try:
        outstr = subprocess.run(["make", "install", "-C", pkgd], stdout=subprocess.PIPE, env=env).stdout.decode('utf-8')
    except subprocess.CalledProcessError:
        print(outstr)
        return False

    return True



def run_package(conf, env, pkg, cmd):
    print("\n$$ Running %s with command %s" % (pkg, cmd))
    pkgd = conf["packages"]["path"]+"/"+pkg
    outstr = subprocess.run(["make", cmd, "-C", pkgd], stdout=subprocess.PIPE, env=env).stdout.decode('utf-8')
    print(outstr)


