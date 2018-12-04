import rospy
import numpy as np
import control_2 as ctl
from geometry_msgs.msg import Twist

def pickUp(String base, String ar):
	ctl.controller(base, ar)
	return 0

def dropOff(String base, String ar):
	ctl.controller(base, ar)
	return 0

def goHome(String base, String home):
	ctl.controller(base, home)
	return 0

def requestNew():
	return 0


# This is Python's sytax for a main() method, which is run by default
# when exectued in the shell
if __name__ == '__main__':
  # Check if the node has received a signal to shut down
  # If not, run the talker method

  #Run this program as a new node in the ROS computation graph 
  #called /turtlebot_controller.
  rospy.init_node('turtlebot_controller', anonymous=True)

  try:
  	base = sys.argv[1]
  	home = sys.argv[2]
  	while not rospy.is_shutdown():
  		command = raw_input('Enter command: ').split
  		instruction = command[0]
  		destination = command[1]


  except rospy.ROSInterruptException:
    pass