import subprocess
import rbsutils

from inspect import getframeinfo, stack

def config_package(conf, env, pkg):
    print("\n$$ Configuring %s" % pkg)
    pkgd = conf["packages"]["path"]+"/"+pkg
    outd = env["OUT_DIR"]
    cmd = "./bootstrap.sh --prefix=" + outd

    try:
        print(cmd)
        outstr = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, env=env, cwd=pkgd, check=True)
        logdata = outstr.stdout.decode('utf-8')
        rbsutils.log_data(env, pkg, "config", logdata)
        print(logdata)

    except subprocess.CalledProcessError as e:
        logdata = "\n\nLOG:\n" + e.stdout.decode('utf-8')
        rbsutils.log_data(env, pkg, "config", logdata)
        print(logdata)
        return False

    return True


def get_compile_cmd_str(env):
    cmd = ""
    if env["ARCH"] == "x86_64":
        cmd = './b2 -j8 install -d2+2 link=shared address-model=64 architecture=x86 threadapi=pthread '\
            'abi=aapcs binary-format=elf toolset=gcc cxxflags="-shared -std=gnu++11 -lang-c++ -fexceptions" '\
            'linkflags="-std=gnu++11 -fexceptions" --without-python --without-context --without-coroutine'

    else:
        debug_info = getframeinfo(stack()[1][0])
        print("RBS Error: Unsupported architecture %s in %s:%s" % (env["ARCH"], debug_info.filename, debug_info.lineno))
        exit(-1)

    return cmd


def compile_package(conf, env, pkg):
    print("\n$$ Compiling %s" % (pkg))
    pkgd = conf["packages"]["path"]+"/"+pkg
    cmd = get_compile_cmd_str(env)

    try:
        #outstr = subprocess.run('./b2 -j8 install -d2+2 link=shared address-model=64 architecture=x86 threadapi=pthread '
        #                        + 'abi=aapcs binary-format=elf toolset=gcc cxxflags="-shared -std=gnu++11 -lang-c++ -fexceptions" '
        #                        + 'linkflags="-std=gnu++11 -fexceptions" --without-python --without-context --without-coroutine',
        #                        shell=True, check=True, env=env, cwd=pkgd, stdout=subprocess.PIPE)

        print(cmd)
        outstr = subprocess.run(cmd, shell=True, check=True, env=env, cwd=pkgd, stdout=subprocess.PIPE)
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
    print("\n$$ Installation done! (This is part of compilation for boost type packages!)")
    return True


def run_package(conf, env, pkg, cmd):
    print("\n$$ Running %s with command %s" % (pkg, cmd))
    pkgd = conf["packages"]["path"]+"/"+pkg
    outstr = subprocess.run(["./b2", cmd], stdout=subprocess.PIPE, env=env, cwd=pkgd)
    print(outstr.stdout.decode('utf-8'))


