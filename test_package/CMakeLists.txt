########################################################################################
## Copyright 2023 Braden Hitchcock - MIT License  https://opensource.org/licenses/MIT ##
########################################################################################
cmake_minimum_required(VERSION 3.22)

enable_language(CXX)
project(PackageTest)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

find_package(hc_project CONFIG REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example hc_project::hc_project)
