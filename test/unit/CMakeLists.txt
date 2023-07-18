########################################################################################
## Copyright 2023 Braden Hitchcock - MIT License  https://opensource.org/licenses/MIT ##
########################################################################################

find_package(GTest 1.13.0 REQUIRED)
include(GoogleTest)

set(TEST test_project)
add_executable(${TEST} TestProject.cpp)
target_link_libraries(${TEST} PRIVATE
    ${PROJECT_NAME}
    GTest::gtest_main
)
gtest_discover_tests(${TEST})
