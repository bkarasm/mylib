cmake_minimum_required(VERSION 3.24)

project(mylib-test-package
    LANGUAGES C
)

find_package(mylib REQUIRED)

add_executable(mylib-test-package
    main.c
)

target_link_libraries(mylib-test-package
    PRIVATE
        mylib::mylib
)
