import subprocess


def config_package(conf, env, pkg):
    print("Configuring %s" % pkg)
    pkgd = conf["packages"]["path"]+"/"+pkg
    outd = env["OUT_DIR"]
    outstr = subprocess.run(["./bootstrap.sh", "--prefix="+outd], stdout=subprocess.PIPE, env=env, cwd=pkgd)
    print(outstr)


def compile_package(conf, env, pkg):
    print("Compiling %s" % (pkg))
    pkgd = conf["packages"]["path"]+"/"+pkg
    if env["DOMAIN"] == "QNX":
        print("\nNote: file '/opt/qnx700/host/linux/x86_64/etc/qcc/gcc/5.4.0/default' " +
              "should be configured with the right compiler (qcc -V flag)!!\n")
    outstr = subprocess.run('./b2 -j8 install -d2+2 link=shared address-model=64 architecture=x86 threadapi=pthread '
                            + 'abi=aapcs binary-format=elf toolset=qcc cxxflags="-Vgcc_ntox86_64_gpp -shared -std=gnu++0x -lang-c++ -fexceptions" '
                            + 'linkflags="-Vgcc_ntox86_64_gpp -std=gnu++0x -fexceptions" archiveflags="-Vgcc_ntox86_64_gpp" target-os=qnxnto '
                            + '--without-python --without-context --without-coroutine',
                            shell=True, check=True, env=env, cwd=pkgd, stdout=subprocess.PIPE).stdout.decode('utf-8')
    print(outstr)


def install_package(conf, env, pkg):
    print("Installation done! (This is part of compilation for boost type packages!)")


def run_package(conf, env, pkg, cmd):
    print("Running %s with command %s" % (pkg, cmd))
    pkgd = conf["packages"]["path"]+"/"+pkg
    outstr = subprocess.run(["./b2", cmd], stdout=subprocess.PIPE, env=env, cwd=pkgd).stdout.decode('utf-8')
    print(outstr)


