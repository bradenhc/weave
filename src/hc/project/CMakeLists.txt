########################################################################################
## Copyright 2023 Braden Hitchcock - MIT License  https://opensource.org/licenses/MIT ##
########################################################################################

set(_HC_LIB_TYPE SHARED)
if(NOT HC_SHARED)
    set(_HC_LIB_TYPE STATIC)
endif()
add_library(${PROJECT_NAME} ${_HC_LIB_TYPE}
    hello.cpp
)

target_include_directories(${PROJECT_NAME} PUBLIC
    $<INSTALL_INTERFACE:include>
    $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
)

install(TARGETS ${PROJECT_NAME})
