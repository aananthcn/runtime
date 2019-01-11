set(CMAKE_SYSTEM_NAME QNX)

set(arch gcc_ntoarmv7le_gpp)

SET(CMAKE_CXX_STANDARD 11)
SET(CMAKE_C_COMPILER qcc)
SET(CMAKE_C_COMPILER_TARGET ${arch})
SET(CMAKE_CXX_COMPILER QCC)
SET(CMAKE_CXX_COMPILER_TARGET ${arch})
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -V${arch} -Wall -Wextra -Wformat -Wformat-security -fexceptions -fstrict-aliasing -fstack-protector -fasynchronous-unwind-tables -fno-omit-frame-pointer -Werror ")


SET(Boost_COMPILER -qcc)
SET(Boost_USE_STATIC_LIBS       	ON)
SET(Boost_USE_MULTITHREADED    	  	ON)
SET(Boost_USE_STATIC_RUNTIME    	OFF)
SET(Boost_USE_SHARED_LIBS       	OFF)


SET(QNX_TARGET $ENV{QNX_TARGET})

include_directories("include" "${QNX_TARGET}/usr/include")

ADD_DEFINITIONS(-D_XOPEN_SOURCE=600)
ADD_DEFINITIONS(-D_POSIX_C_SOURCE=200112L)
ADD_DEFINITIONS(-D__EXT_POSIX1_200112=1)
ADD_DEFINITIONS(-D__EXT_QNX=1)
