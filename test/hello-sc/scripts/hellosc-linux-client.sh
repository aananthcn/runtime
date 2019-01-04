#! /bin/sh

# VSOMEIP_CONFIGURATION=/home/aananth/projects/runtime/config/vsomeip/hello-sc_client.json \
#   /home/aananth/projects/runtime/out/Linux/bin/vsomeipd &

#sleep 1
#echo "vsomeipd is launched!!"


VSOMEIP_CONFIGURATION=/home/aananth/projects/runtime/config-target/Linux/vsomeip/hellosc_linux_client.json \
  VSOMEIP_APPLICATION_NAME=hellosc-client-average \
  /home/aananth/projects/runtime/out/Linux/bin/hellosc-client-average
