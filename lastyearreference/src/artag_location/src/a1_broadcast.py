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

		listener.waitForTransform('ar_marker_3','ar_marker_2',rospy.Time(0),rospy.Duration(4.0))
		(trans_OD,rot) = listener.lookupTransform('ar_marker_3', 'ar_marker_2', rospy.Time(0))

		dist_UO = math.sqrt(trans_OD[0]*0.5*trans_OD[0]*0.5 + trans_OD[1]*0.5*trans_OD[1]*0.5)

		listener.waitForTransform('ar_marker_2','ar_marker_0',rospy.Time(0),rospy.Duration(4.0))
		(trans_TO,rot) = listener.lookupTransform('ar_marker_2', 'ar_marker_0', rospy.Time(0))

		dist_TO = math.sqrt(trans_TO[0]*trans_TO[0] + trans_TO[1]*trans_TO[1])

		listener.waitForTransform('ar_marker_2','a_frame',rospy.Time(0),rospy.Duration(4.0))
		(trans,rot) = listener.lookupTransform('ar_marker_2', 'a_frame', rospy.Time(0))

		theta_AO = math.atan2(trans[1],trans[0])
		y = trans[1]
		x = trans[0]

		listener.waitForTransform('ar_marker_2','u_frame',rospy.Time(0),rospy.Duration(4.0))
		(trans,rot) = listener.lookupTransform('ar_marker_2', 'u_frame', rospy.Time(0))

		theta_UO = math.atan2(trans[1],trans[0])

		delta_theta = abs(theta_AO - theta_UO)

		
		br.sendTransform((dist_UO*math.cos(math.atan2(y,x)+delta_theta/3), dist_UO*math.sin(math.atan2(y,x)+delta_theta/3), 0.0),(0.0, 0.0, 0.0, 1.0),rospy.Time.now(),"a1_frame","ar_marker_2")

		rate_br.sleep()

			# current_time = time.time()
			# t = current_time - start_time
			# print "time: %s" % t
			# listener.waitForTransform('ar_marker_3','ar_marker_2',rospy.Time(0),rospy.Duration(4.0))
			# (trans_OD,rot) = listener.lookupTransform('ar_marker_3', 'ar_marker_2', rospy.Time(0))

			# dist_UO = math.sqrt(trans_OD[0]*0.7*trans_OD[0]*0.7 + trans_OD[1]*0.7*trans_OD[1]*0.7)

			# listener.waitForTransform('ar_marker_2','ar_marker_0',rospy.Time(0),rospy.Duration(4.0))
			# (trans_TO,rot) = listener.lookupTransform('ar_marker_2', 'ar_marker_0', rospy.Time(0))

			# dist_TO = math.sqrt(trans_TO[0]*trans_TO[0] + trans_TO[1]*trans_TO[1])


			# br.sendTransform((dist_UO*math.cos(math.atan2(y,x)+t*math.pi/20), dist_UO*math.sin(math.atan2(y,x)+t*math.pi/20), 0.0),(0.0, 0.0, 0.0, 1.0),rospy.Time.now(),"a_frame","ar_marker_2")

			# rate_br.sleep()


if __name__ == '__main__':

	rospy.init_node('a1_broadcaster', anonymous=False)

	rospy.Timer(rospy.Duration(2.0), callback())
	