cmake_minimum_required(VERSION 2.8)

if(${CMAKE_SYSTEM_NAME} MATCHES "QNX")
    set(OS "QNX")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -D${OS} ${OS_CXX_FLAGS} -g ${OPTIMIZE} -std=gnu++11 ${NO_DEPRECATED} ${EXPORTSYMBOLS}")
else()
    set(OS "LINUX")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread -std=gnu++11")
endif(${CMAKE_SYSTEM_NAME} MATCHES "QNX")

set(CMAKE_BUILD_TYPE Debug)
set(INSTALL_LIB_DIR ${CMAKE_INSTALL_PREFIX}/lib)
set(INSTALL_BIN_DIR ${CMAKE_INSTALL_PREFIX}/bin)
message(STATUS "CMAKE_INSTALL_PREFIX = ${CMAKE_INSTALL_PREFIX}")

include_directories(
     src-gen
     src-gen/v1/hellosys
     ${CMAKE_INSTALL_PREFIX}/include
     ${CMAKE_INSTALL_PREFIX}/include/CommonAPI-3.1
)

link_directories(
    ${CMAKE_INSTALL_PREFIX}/lib
)

add_executable(hellosys-client
    src/AverageClient.cpp
    src-gen/v1/hellosys/AverageSomeIPProxy.cpp
    src-gen/v1/hellosys/AverageSomeIPDeployment.cpp
)
target_link_libraries(hellosys-client CommonAPI CommonAPI-SomeIP vsomeip)

add_executable(hellosys-server
    src/AverageService.cpp
    src/AverageStubImpl.cpp
    src-gen/v1/hellosys/AverageSomeIPStubAdapter.cpp
    src-gen/v1/hellosys/AverageStubDefault.cpp
    src-gen/v1/hellosys/AverageSomeIPDeployment.cpp
)
target_link_libraries(hellosys-server CommonAPI CommonAPI-SomeIP vsomeip)

install(TARGETS hellosys-client hellosys-server
    LIBRARY DESTINATION ${INSTALL_LIB_DIR}
    RUNTIME DESTINATION ${INSTALL_BIN_DIR}
)