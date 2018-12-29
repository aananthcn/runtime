import subprocess


def config_package(conf, env, pkg):
    print("\n$$ Configuring %s" % pkg)
    pkgd = conf["packages"]["path"]+"/"+pkg
    outd = env["OUT_DIR"]

    try:
        outstr = subprocess.run(["./bootstrap.sh", "--prefix="+outd],
                                stdout=subprocess.PIPE, env=env, cwd=pkgd, check=True)
        print(outstr.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("\n\nLOG:\n" + e.stdout.decode('utf-8'))
        return False

    return True


def compile_package(conf, env, pkg):
    print("\n$$ Compiling %s" % (pkg))
    pkgd = conf["packages"]["path"]+"/"+pkg

    try:
        outstr = subprocess.run('./b2 -j8 install -d2+2 link=static address-model=64 architecture=x86 threadapi=pthread '
                                + 'abi=aapcs binary-format=elf toolset=gcc cxxflags="-shared -std=gnu++11 -lang-c++ -fexceptions" '
                                + 'linkflags="-std=gnu++11 -fexceptions" --without-python --without-context --without-coroutine',
                                shell=True, check=True, env=env, cwd=pkgd, stdout=subprocess.PIPE)
        print(outstr.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("\n\nLOG:\n" + e.stdout.decode('utf-8'))
        return False

    return True



def install_package(conf, env, pkg):
    print("\n$$ Installation done! (This is part of compilation for boost type packages!)")
    return True


def run_package(conf, env, pkg, cmd):
    print("\n$$ Running %s with command %s" % (pkg, cmd))
    pkgd = conf["packages"]["path"]+"/"+pkg
    outstr = subprocess.run(["./b2", cmd], stdout=subprocess.PIPE, env=env, cwd=pkgd)
    print(outstr.stdout.decode('utf-8'))


