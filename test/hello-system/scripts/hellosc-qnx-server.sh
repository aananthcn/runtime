#! /bin/sh

# VSOMEIP_CONFIGURATION=/opt/etc/vsomeip/hello-sc_server.json \
#   /opt/bin/vsomeipd &

VSOMEIP_CONFIGURATION=/opt/etc/vsomeip/hellosc-server.json \
  VSOMEIP_APPLICATION_NAME=hellosc-server /opt/bin/hellosc-server
