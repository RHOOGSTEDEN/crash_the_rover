#!/usr/bin/env python
import sys
import rospy

import numpy as np

from tf2_msgs.msg import TFMessage
import tf
import time

import math
from numpy.linalg import inv

from artag_location.msg import AT_Message

def callback():

	listener = tf.TransformListener()
	br = tf.TransformBroadcaster() #Broadcaster
	rate_br = rospy.Rate(20.0) #Rate for Broadcaster

	while not rospy.is_shutdown():

			br.sendTransform((x*1.5, y*1.5, 0.0),(0.0, 0.0, 0.0, 1.0),rospy.Time.now(),"u_frame","ar_marker_3")

			rate_br.sleep()


if __name__ == '__main__':
	rospy.init_node('u_broadcaster', anonymous=False)

	listener = tf.TransformListener()
	br = tf.TransformBroadcaster() 
	#t_end = time.time() + 5
	#while time.time() < t_end:
	#print time.time()
	#callback()
	#rospy.Timer(rospy.Duration(5)
	listener.waitForTransform('ar_marker_3','ar_marker_2',rospy.Time(0),rospy.Duration(4.0))
	(trans,rot) = listener.lookupTransform('ar_marker_3', 'ar_marker_2', rospy.Time(0))

	global x
	x = trans[0]
	global y
	y = trans[1]

	rospy.Timer(rospy.Duration(2.0), callback())