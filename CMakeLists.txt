cmake_minimum_required(VERSION 2.8.3)
project(performance_tests)

find_package(catkin REQUIRED COMPONENTS dynamic_reconfigure message_generation roscpp rospy std_msgs)

add_message_files(
  FILES
  SuperAwsome.msg
)

generate_messages(
  DEPENDENCIES
  performance_tests
)

generate_dynamic_reconfigure_options(
  cfg/performanceTests.cfg
)

catkin_package(
  CATKIN_DEPENDS dynamic_reconfigure message_runtime roscpp rospy std_msgs
)

include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(listener src/listener.cpp)
add_executable(talker src/talker.cpp)
add_executable(pytalker src/pytalker.py)
add_executable(pylistner src/pylistner.py)


install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
  FILES_MATCHING PATTERN "*.h"
)

install(TARGETS listener talker
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
