########################################################################################
## Copyright 2023 Braden Hitchcock - MIT License  https://opensource.org/licenses/MIT ##
########################################################################################
cmake_minimum_required(VERSION 3.22)

enable_language(CXX)
project(${CONAN_PKG_NAME})

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)
set(CMAKE_EXPORT_COMPILE_COMMANDS TRUE)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/bin")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/lib")
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/lib")

add_subdirectory(src/hc/project)

install(DIRECTORY include/ DESTINATION include)

if(NOT HC_DISABLE_TESTS)
    enable_testing()
    add_subdirectory(test/unit)
    if(NOT HC_DISABLE_COMPONENT_TESTS)
        add_subdirectory(test/component)
    endif()
endif()
