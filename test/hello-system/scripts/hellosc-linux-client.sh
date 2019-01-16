#! /bin/sh

# VSOMEIP_CONFIGURATION=/home/aananth/projects/runtime/config/vsomeip/hello-sc_client.json \
#   /home/aananth/projects/runtime/tmp/out/Linux/x86_64/bin/vsomeipd &

#sleep 1
#echo "vsomeipd is launched!!"


export VSOMEIP_CONFIGURATION=/home/aananth/projects/runtime/config-target/Linux/vsomeip/hellosc-client.json
sudo LD_LIBRARY_PATH=/home/aananth/projects/runtime/tmp/out/Linux/x86_64/lib/  \
  VSOMEIP_APPLICATION_NAME=hellosc-client /home/aananth/projects/runtime/tmp/out/Linux/x86_64/bin/hellosc-client