cmake_minimum_required(VERSION 3.24)

project(mylib
    LANGUAGES C
)

include(GNUInstallDirs)

add_library(mylib)

target_sources(mylib
    PUBLIC
        FILE_SET HEADERS
        BASE_DIRS ..
)

add_subdirectory(include)
add_subdirectory(src)

install(
    TARGETS mylib
    RUNTIME  DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE  DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY  DESTINATION ${CMAKE_INSTALL_LIBDIR}
    FILE_SET HEADERS
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEIR}
)
