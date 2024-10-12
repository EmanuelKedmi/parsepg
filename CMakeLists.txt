cmake_minimum_required(VERSION 3.12)
project(ppgbin)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add source files
set(SOURCES
    src/ppgbin.cpp
)

# Add header files
set(HEADERS
    include/ppgbin.h
)

# Add source file for tester executable
set(TESTER_SOURCE
    src/tester.cpp
)


# Create static library
add_library(ppgbin_static STATIC ${SOURCES} ${HEADERS})
target_include_directories(ppgbin_static PUBLIC include)
set_target_properties(ppgbin_static PROPERTIES OUTPUT_NAME "ppgbin")
# set_target_properties(ppgbin_static PROPERTIES
#     ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib
# )
# Create shared library
add_library(ppgbin_shared SHARED ${SOURCES} ${HEADERS})
target_compile_definitions(ppgbin_shared PUBLIC PPGBIN_EXPORTS)
target_include_directories(ppgbin_shared PUBLIC include)
set_target_properties(ppgbin_shared PROPERTIES OUTPUT_NAME "ppgbin")
# set_target_properties(ppgbin_shared PROPERTIES
#     LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib
# )


# Create tester executable
add_executable(tester ${TESTER_SOURCE})
target_include_directories(tester PUBLIC include)
# Link the tester executable with ppgbin_static library
target_link_libraries(tester PUBLIC ppgbin_static ppgbin_shared)