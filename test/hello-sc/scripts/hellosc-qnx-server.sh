#! /bin/sh

# VSOMEIP_CONFIGURATION=/usr/aananth/QNX/etc/vsomeip/hello-sc_server.json \
#   /usr/aananth/QNX/bin/vsomeipd &

VSOMEIP_CONFIGURATION=/usr/aananth/QNX/etc/vsomeip/hellosc_qnx_server.json \
  VSOMEIP_APPLICATION_NAME=hellosc-service-average \
  /usr/aananth/QNX/bin/hellosc-service-average
