cmake_minimum_required(VERSION 2.8)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread -std=gnu++11")
set(INSTALL_LIB_DIR ${CMAKE_INSTALL_PREFIX}/lib)
set(INSTALL_BIN_DIR ${CMAKE_INSTALL_PREFIX}/bin)
message(STATUS "CMAKE_INSTALL_PREFIX = ${CMAKE_INSTALL_PREFIX}")

include_directories(
     src-gen
     src-gen/v1/hellosc
     ${CMAKE_INSTALL_PREFIX}/include
     ${CMAKE_INSTALL_PREFIX}/include/CommonAPI-3.1
)

link_directories(
    ${CMAKE_INSTALL_PREFIX}/lib
)

add_executable(hellosc-client-average
    src/AverageClient.cpp
    src-gen/v1/hellosc/AverageSomeIPProxy.cpp
    src-gen/v1/hellosc/AverageSomeIPDeployment.cpp
)
target_link_libraries(hellosc-client-average CommonAPI CommonAPI-SomeIP vsomeip)

add_executable(hellosc-service-average
    src/AverageService.cpp
    src/AverageStubImpl.cpp
    src-gen/v1/hellosc/AverageSomeIPStubAdapter.cpp
    src-gen/v1/hellosc/AverageStubDefault.cpp
    src-gen/v1/hellosc/AverageSomeIPDeployment.cpp
)
target_link_libraries(hellosc-service-average CommonAPI CommonAPI-SomeIP vsomeip)

install(TARGETS hellosc-client-average hellosc-service-average
    LIBRARY DESTINATION ${INSTALL_LIB_DIR}
    RUNTIME DESTINATION ${INSTALL_BIN_DIR}
)