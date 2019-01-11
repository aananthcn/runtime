import subprocess
import rbsutils


def config_package(conf, env, pkg):
    print("\n$$ Configuring %s" % pkg)
    return True


def compile_package(conf, env, pkg):
    print("\n$$ Compiling %s" % (pkg))
    pkgd = conf["packages"]["path"]+"/"+pkg

    try:
        outstr = subprocess.run(["make", "-C", pkgd], stdout=subprocess.PIPE, env=env)
        logdata = outstr.stdout.decode('utf-8')
        rbsutils.log_data(env, pkg, "compile", logdata)
        print(logdata)
        if "Error" in outstr and "***" in outstr:
            return False
    except subprocess.CalledProcessError as e:
        print("\n\nLOG:\n" + e.stdout.decode('utf-8'))
        return False

    return True



def install_package(conf, env, pkg):
    print("\n$$ Installing %s" % (pkg))
    pkgd = conf["packages"]["path"]+"/"+pkg

    try:
        outstr = subprocess.run(["make", "install", "-C", pkgd], stdout=subprocess.PIPE, env=env)
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
    outstr = subprocess.run(["make", cmd, "-C", pkgd], stdout=subprocess.PIPE, env=env)
    print(outstr.stdout.decode('utf-8'))


