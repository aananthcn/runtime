#! /bin/sh

RT_ROOT=/opt
ETC_DIR=${RT_ROOT}/etc
BIN_DIR=${RT_ROOT}/bin
LIB_DIR=${RT_ROOT}/lib


VSOMEIP_CONFIGURATION=${ETC_DIR}/vsomeip/hellosomeip-server.json LD_LIBRARY_PATH=${LIB_DIR}  \
  VSOMEIP_APPLICATION_NAME=hellosomeip-server ${BIN_DIR}/hellosomeip-server
