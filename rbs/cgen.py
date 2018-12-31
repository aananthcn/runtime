import json
import subprocess
import os


# vsomeip:
# ../../../cgen/commonapi_someip_generator/commonapi-someip-generator-linux-x86_64 -ll verbose ./fidl/average.fdepl

# common-api:
# ../../../cgen/commonapi-generator/commonapi-generator-linux-x86_64 -sk ./fidl/average.fidl

def cgen_fidl_package(conf, env, pkg):
    print("\n$$ Code generation from fidl scripts check for %s" % pkg)
    pkgd = env["PWD"] + "/" + conf["packages"]["path"]+"/"+pkg
    outd = env["OUT_DIR"]
    fidld = pkgd+"/fidl"

    if not os.path.exists(fidld):
        print("... not required!! Let us mark it as done!")
        return True

    files = os.listdir(fidld)
    fidl_files = []
    fdepl_files = []
    for file in files:
        if file.endswith(".fidl"):
            fidl_files.append(file)
        if file.endswith(".fdepl"):
            fdepl_files.append(file)

    dest_dir = pkgd + "/src-gen/"
    capi_gentool = env["PWD"] + "/" + conf["path"] + "/" + conf["capi"]
    capi_genopts = "-sk"

    for file in fidl_files:
        fidlf = fidld + "/" + file
        print("\nGenerating CAPI code for: \"%s\"" % (fidlf))
        try:
            cmd = capi_gentool + " " + capi_genopts + " -d " + dest_dir + " " + fidlf
            outstr = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, env=env, cwd=pkgd, check=True)
            print(outstr.stdout.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print("\n\nLOG:\n" + e.stdout.decode('utf-8'))
            return False


    capi_vsomeip_gentool = env["PWD"] + "/" + conf["path"] + "/" + conf["vsomeip"]
    capi_vsomeip_genopts = "-ll verbose"

    for file in fdepl_files:
        fdeplf = fidld + "/" + file
        print("\nGenerating vSomeIP-CAPI code for: \"%s\"" % (fdeplf))
        try:
            cmd = capi_vsomeip_gentool + " " + capi_vsomeip_genopts + " -d " + dest_dir + " " + fdeplf
            outstr = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, env=env, cwd=pkgd, check=True)
            print(outstr.stdout.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print("\n\nLOG:\n" + e.stdout.decode('utf-8'))
            return False

    return True