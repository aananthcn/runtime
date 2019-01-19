#! /bin/sh


RT_ROOT=/home/aananth/projects/runtime
ETC_DIR=${RT_ROOT}/config-target/Linux/etc
BIN_DIR=${RT_ROOT}/out/Linux/x86_64/bin
LIB_DIR=${RT_ROOT}/out/Linux/x86_64/lib


VSOMEIP_CONFIGURATION=${ETC_DIR}/vsomeip/hellosys-client.json LD_LIBRARY_PATH=${LIB_DIR}  \
  VSOMEIP_APPLICATION_NAME=hellosys-client ${BIN_DIR}/hellosys-client
