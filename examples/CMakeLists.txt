# examples/CMakeLists.txt
# One demo per .cpp. Add more by copying the two lines below.
add_executable(example_hello hello.cpp)
target_link_libraries(example_hello PRIVATE fmt::fmt)
