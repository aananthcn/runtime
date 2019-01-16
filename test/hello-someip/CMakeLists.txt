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
     ${CMAKE_INSTALL_PREFIX}/include
)


link_directories(
    ${CMAKE_INSTALL_PREFIX}/lib
)

find_library(SOMEIP_LIBRARY
    NAMES vsomeip libvsomeip
    HINTS "${CMAKE_INSTALL_PREFIX}/lib"
)
message(STATUS "SOMEIP Library = ${SOMEIP_LIBRARY}")

add_executable(hellosomeip-client
    src/request-client.cpp
)
target_link_libraries(hellosomeip-client ${SOMEIP_LIBRARY})


add_executable(hellosomeip-server
    src/response-server.cpp
)
target_link_libraries(hellosomeip-server ${SOMEIP_LIBRARY})


install(TARGETS hellosomeip-client hellosomeip-server
    LIBRARY DESTINATION ${INSTALL_LIB_DIR}
    RUNTIME DESTINATION ${INSTALL_BIN_DIR}
)