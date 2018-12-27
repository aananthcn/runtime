import subprocess


def config_package(conf, env, pkg):
    print("Configuring %s" % pkg)
    print("...done!")


def compile_package(conf, env, pkg):
    print("Compiling %s" % (pkg))
    pkgd = conf["packages"]["path"]+"/"+pkg
    outstr = subprocess.run(["make", "-C", pkgd], stdout=subprocess.PIPE, env=env).stdout.decode('utf-8')
    print(outstr)



def install_package(conf, env, pkg):
    print("Installing %s" % (pkg))
    pkgd = conf["packages"]["path"]+"/"+pkg
    outstr = subprocess.run(["make", "install", "-C", pkgd], stdout=subprocess.PIPE, env=env).stdout.decode('utf-8')
    print(outstr)



def run_package(conf, env, pkg, cmd):
    print("Running %s with command %s" % (pkg, cmd))
    pkgd = conf["packages"]["path"]+"/"+pkg
    outstr = subprocess.run(["make", cmd, "-C", pkgd], stdout=subprocess.PIPE, env=env).stdout.decode('utf-8')
    print(outstr)


