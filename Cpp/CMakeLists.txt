# Sample CMake file for OpenCV projects

CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

PROJECT(project_name)

# Do we really need this?
#SET(OpenCV_DIR /path/to/your/opencv/installation)

FIND_PACKAGE(OpenCV REQUIRED)

ADD_EXECUTABLE(executable_name main.cpp)

TARGET_LINK_LIBRARIES(executable_name ${OpenCV_LIBS})
