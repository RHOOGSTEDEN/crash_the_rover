#!/usr/bin/env python
import sys
import rospy

import numpy as np

from tf2_msgs.msg import TFMessage
import tf
import time
from geometry_msgs.msg import Twist

import math
from numpy.linalg import inv

from artag_location.msg import AT_Message



def callback():

	listener = tf.TransformListener()
	# br = tf.TransformBroadcaster() #Broadcaster
	# rate_br = rospy.Rate(10.0) #Rate for Broadcaster
	rate =  rospy.Rate(0.07)

	while not rospy.is_shutdown():

			# listener.waitForTransform('ar_marker_3','ar_marker_2',rospy.Time(0),rospy.Duration(4.0))
			# (trans,rot) = listener.lookupTransform('ar_marker_3', 'ar_marker_2', rospy.Time(0))

			# br.sendTransform((trans[0]*1.2, trans[1]*1.2, 0.0),(0.0, 0.0, 0.0, 1.0),rospy.Time(0),"uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu_frame","ar_marker_3")

			# rate_br.sleep()

			publish(0,0,"n")
                # try:
			text1 = raw_input("If you want relative congiuration, press <y>:")
			if text1 == 'y':
				print("Waiting for turtlebot to get behind to position a...")
				listener.waitForTransform('ar_marker_0','a_frame',rospy.Time(0),rospy.Duration(4.0))
				(trans,rot) = listener.lookupTransform('ar_marker_0', 'a_frame', rospy.Time(0))
				print trans[0]
				print trans[1]
			# print "translation:  %s" %(trans)
			# print "rotation: %s" % (rot

				# publish(trans[0],trans[1],'n')
				publish(trans[0],trans[1],"n")

				rate.sleep()

				listener.waitForTransform('ar_marker_0','a1_frame',rospy.Time(0),rospy.Duration(4.0))
				(trans,rot) = listener.lookupTransform('ar_marker_0', 'a1_frame', rospy.Time(0))
				print trans[0]
				print trans[1]
			# print "translation:  %s" %(trans)
			# print "rotation: %s" % (rot

				# publish(trans[0],trans[1],'n')
				publish(trans[0],trans[1],"n")

				rate.sleep()

				listener.waitForTransform('ar_marker_0','a2_frame',rospy.Time(0),rospy.Duration(4.0))
				(trans,rot) = listener.lookupTransform('ar_marker_0', 'a2_frame', rospy.Time(0))
				print trans[0]
				print trans[1]
			# print "translation:  %s" %(trans)
			# print "rotation: %s" % (rot

				# publish(trans[0],trans[1],'n')
				publish(trans[0],trans[1],"n")

				rate.sleep()

				
				# print("Following a circular path...")
				# listener.waitForTransform('ar_marker_0','u_frame',rospy.Time(0),rospy.Duration(4.0))
				# (trans,rot) = listener.lookupTransform('ar_marker_0', 'u_frame', rospy.Time(0))
				# distance = math.sqrt(trans[0]*trans[0] + trans[1]*trans[1])

				# print ("Before following A, Distance: %s") % distance


				# while distance > 0.05:
				# 	listener.waitForTransform('ar_marker_0','a_frame',rospy.Time(0),rospy.Duration(4.0))
				# 	(trans,rot) = listener.lookupTransform('ar_marker_0', 'a_frame', rospy.Time(0))
				# 	print math.sqrt(trans[0]*trans[0] + trans[1]*trans[1])
				# 	publish(trans[0],trans[1],'y')

				# 	listener.waitForTransform('ar_marker_0','u_frame',rospy.Time(0),rospy.Duration(4.0))
				# 	(trans,rot) = listener.lookupTransform('ar_marker_0', 'u_frame', rospy.Time(0))
				# 	distance = math.sqrt(trans[0]*trans[0] + trans[1]*trans[1])

				# 	print ("following circular path: %s") % distance

					# rospy.Rate(0.01).sleep()


                # except:
                #         continue

				# try:
				# 	listener.waitForTransform('ar_marker_0','u_frame',rospy.Time(0),rospy.Duration(4.0))
				# 	(trans,rot) = listener.lookupTransform('ar_marker_0', 'u_frame', rospy.Time(0))
				# 	distance = math.sqrt(trans[0]*trans[0] + trans[1]*trans[1])
				# 	print "Distance is : %s" % (distance)
				# 	while distance > 0.06:
				# 		print("Getting behind the object...")
				# 		print trans[0]
				# 		print trans[1]
				# 		publish(trans[0]*1.2,trans[1]*1.2,'n')
				# 		rospy.Rate(0.1).sleep()

				# 		try:
				# 			listener.waitForTransform('ar_marker_0','u_frame',rospy.Time(0),rospy.Duration(4.0))
				# 			(trans,rot) = listener.lookupTransform('ar_marker_0', 'u_frame', rospy.Time(0))
				# 			distance = math.sqrt(trans[0]*trans[0] + trans[1]*trans[1])
				# 		except:
				# 			break
				# except:
				# 	pass
				# listener.waitForTransform('ar_marker_0','u_frame',rospy.Time(0),rospy.Duration(4.0))
				# (trans,rot) = listener.lookupTransform('ar_marker_0', 'u_frame', rospy.Time(0))
				# print trans[0]
				# print trans[1]

				# publish(trans[0],trans[1],"n")

				# rate.sleep()

				# listener.waitForTransform('ar_marker_0','ar_marker_2',rospy.Time(0),rospy.Duration(4.0))
				# (trans,rot) = listener.lookupTransform('ar_marker_0', 'ar_marker_2', rospy.Time(0))
				# print trans[0]
				# print trans[1]
			# print "translation:  %s" %(trans)
			# print "rotation: %s" % (rot

				# publish(trans[0],trans[1],'n')
				# publish(trans[0],trans[1],"n")

				# rate.sleep()

				print("Getting behind the object...")
				listener.waitForTransform('ar_marker_0','u_frame',rospy.Time(0),rospy.Duration(4.0))
				(trans,rot) = listener.lookupTransform('ar_marker_0', 'u_frame', rospy.Time(0))
				print trans[0]
				print trans[1]
				publish(trans[0]*1,trans[1]*1,'n')

				rate.sleep()

				print("The turtlebot is now behind the object")
				print("Now computing configuration of the target with respect to turtlebot...")
				listener.waitForTransform('ar_marker_0','ar_marker_3',rospy.Time(0),rospy.Duration(4.0))
				(trans,rot) = listener.lookupTransform('ar_marker_0', 'ar_marker_3', rospy.Time(0))

				print("Waiting for turtlebot to reach the destination...")
				print trans[0]
				print trans[1]
				publish(trans[0]*1.2,trans[1]*1.2,'n')

				rate.sleep()


			####



            # Working Code:
			# 	try:
			# 		listener.waitForTransform('ar_marker_0','ar_marker_2',rospy.Time(0),rospy.Duration(4.0))
			# 		(trans,rot) = listener.lookupTransform('ar_marker_0', 'ar_marker_2', rospy.Time(0))
			# 		print("Adjusting position...")
			# 		print trans[0]
			# 		print trans[1]
			# 		publish(trans[0]*3,trans[1]*3)
			# 		rospy.Rate(0.03).sleep()
			# 	except:
			# 		print("Now computing configuration of the target with respect to turtlebot:")
			# 		listener.waitForTransform('ar_marker_0','ar_marker_3',rospy.Time(0),rospy.Duration(4.0))
			# 		(trans,rot) = listener.lookupTransform('ar_marker_0', 'ar_marker_3', rospy.Time(0))
			# # print "translation:  %s" %(trans)
			# # print "rotation: %s" % (rot)
			# 		print trans[0]
			# 		print trans[1]

			# 		publish(trans[0],trans[1])

			# 		rospy.Rate(0.03).sleep()
			# 	try:
			# 		print("Now computing configuration of the target with respect to turtlebot:")
			# 		listener.waitForTransform('ar_marker_0','ar_marker_3',rospy.Time(0),rospy.Duration(4.0))
			# 		(trans,rot) = listener.lookupTransform('ar_marker_0', 'ar_marker_3', rospy.Time(0))
			# # print "translation:  %s" %(trans)
			# # print "rotation: %s" % (rot)
			# 		print trans[0]
			# 		print trans[1]

			# 		publish(trans[0],trans[1])
			# 	except:
			# 		continue

def publish(tran_x, tran_y,reached):
	pub = rospy.Publisher('user_messages', AT_Message, queue_size=10)

	
    # Construct a string that we want to publish
    # (In Python, the "%" operator functions similarly
    #  to sprintf in C or MATLAB)
	message = AT_Message()
	message.tran_x = tran_x
	message.tran_y = tran_y
	message.reached = reached

	    # Publish our string to the 'chatter_talk' topic
	pub.publish(message)

if __name__ == '__main__':
	rospy.init_node('artag_lcoation', anonymous=False)
	#t_end = time.time() + 5
	#while time.time() < t_end:
	#print time.time()
	#callback()
	#rospy.Timer(rospy.Duration(5)

	rospy.Timer(rospy.Duration(2.0), callback())

