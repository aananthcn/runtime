#! /bin/sh

# VSOMEIP_CONFIGURATION=/opt/etc/vsomeip/hellosys-server.json \
#   /opt/bin/vsomeipd &


RT_ROOT=/opt
ETC_DIR=${RT_ROOT}/etc
BIN_DIR=${RT_ROOT}/bin
LIB_DIR=${RT_ROOT}/lib


VSOMEIP_CONFIGURATION=${ETC_DIR}/vsomeip/hellosys-server.json LD_LIBRARY_PATH=${LIB_DIR}  \
  VSOMEIP_APPLICATION_NAME=hellosys-server ${BIN_DIR}/hellosys-server
