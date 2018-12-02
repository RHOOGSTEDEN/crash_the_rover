# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "artag_location: 1 messages, 0 services")

set(MSG_I_FLAGS "-Iartag_location:/home/cc/ee106a/fa17/class/ee106a-aau/ros_workspaces/final_project/src/artag_location/msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(artag_location_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/cc/ee106a/fa17/class/ee106a-aau/ros_workspaces/final_project/src/artag_location/msg/AT_Message.msg" NAME_WE)
add_custom_target(_artag_location_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "artag_location" "/home/cc/ee106a/fa17/class/ee106a-aau/ros_workspaces/final_project/src/artag_location/msg/AT_Message.msg" ""
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(artag_location
  "/home/cc/ee106a/fa17/class/ee106a-aau/ros_workspaces/final_project/src/artag_location/msg/AT_Message.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/artag_location
)

### Generating Services

### Generating Module File
_generate_module_cpp(artag_location
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/artag_location
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(artag_location_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(artag_location_generate_messages artag_location_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fa17/class/ee106a-aau/ros_workspaces/final_project/src/artag_location/msg/AT_Message.msg" NAME_WE)
add_dependencies(artag_location_generate_messages_cpp _artag_location_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(artag_location_gencpp)
add_dependencies(artag_location_gencpp artag_location_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS artag_location_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(artag_location
  "/home/cc/ee106a/fa17/class/ee106a-aau/ros_workspaces/final_project/src/artag_location/msg/AT_Message.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/artag_location
)

### Generating Services

### Generating Module File
_generate_module_lisp(artag_location
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/artag_location
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(artag_location_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(artag_location_generate_messages artag_location_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fa17/class/ee106a-aau/ros_workspaces/final_project/src/artag_location/msg/AT_Message.msg" NAME_WE)
add_dependencies(artag_location_generate_messages_lisp _artag_location_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(artag_location_genlisp)
add_dependencies(artag_location_genlisp artag_location_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS artag_location_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(artag_location
  "/home/cc/ee106a/fa17/class/ee106a-aau/ros_workspaces/final_project/src/artag_location/msg/AT_Message.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/artag_location
)

### Generating Services

### Generating Module File
_generate_module_py(artag_location
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/artag_location
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(artag_location_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(artag_location_generate_messages artag_location_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fa17/class/ee106a-aau/ros_workspaces/final_project/src/artag_location/msg/AT_Message.msg" NAME_WE)
add_dependencies(artag_location_generate_messages_py _artag_location_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(artag_location_genpy)
add_dependencies(artag_location_genpy artag_location_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS artag_location_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/artag_location)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/artag_location
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(artag_location_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/artag_location)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/artag_location
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(artag_location_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/artag_location)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/artag_location\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/artag_location
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(artag_location_generate_messages_py std_msgs_generate_messages_py)
endif()
