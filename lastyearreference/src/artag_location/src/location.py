#!/usr/bin/env python
import sys
import rospy
# import roslib; roslib.load_manifest('kinematics')

from moveit_msgs.msg import OrientationConstraint, Constraints
from geometry_msgs.msg import PoseStamped
import numpy as np

import roslib
import rospy

from tf2_msgs.msg import TFMessage
import tf
import time
import numpy

import math
from numpy.linalg import inv

from artag_location.msg import AT_Message


def quaternion_to_euler_angle(w, x, y, z):
	ysqr = y * y
	
	t0 = +2.0 * (w * x + y * z)
	t1 = +1.0 - 2.0 * (x * x + ysqr)
	X = math.degrees(math.atan2(t0, t1))
	
	t2 = +2.0 * (w * y - z * x)
	t2 = +1.0 if t2 > +1.0 else t2
	t2 = -1.0 if t2 < -1.0 else t2
	Y = math.degrees(math.asin(t2))
	
	t3 = +2.0 * (w * z + x * y)
	t4 = +1.0 - 2.0 * (ysqr + z * z)
	Z = math.degrees(math.atan2(t3, t4))
	
	return X, Y, Z

def quaternion_matrix(quaternion):
    """Return homogeneous rotation matrix from quaternion.

    >>> M = quaternion_matrix([0.99810947, 0.06146124, 0, 0])
    >>> numpy.allclose(M, rotation_matrix(0.123, [1, 0, 0]))
    True
    >>> M = quaternion_matrix([1, 0, 0, 0])
    >>> numpy.allclose(M, numpy.identity(4))
    True
    >>> M = quaternion_matrix([0, 1, 0, 0])
    >>> numpy.allclose(M, numpy.diag([1, -1, -1, 1]))
    True

    """
    _EPS = numpy.finfo(float).eps * 4.0
    q = numpy.array(quaternion, dtype=numpy.float64, copy=True)
    n = numpy.dot(q, q)
    if n < _EPS:
        return numpy.identity(4)
    q *= math.sqrt(2.0 / n)
    q = numpy.outer(q, q)
    return numpy.array([
        [1.0-q[2, 2]-q[3, 3],     q[1, 2]-q[3, 0],     q[1, 3]+q[2, 0], 0.0],
        [    q[1, 2]+q[3, 0], 1.0-q[1, 1]-q[3, 3],     q[2, 3]-q[1, 0], 0.0],
        [    q[1, 3]-q[2, 0],     q[2, 3]+q[1, 0], 1.0-q[1, 1]-q[2, 2], 0.0],
        [                0.0,                 0.0,                 0.0, 1.0]])

def callback(msg):
	x = msg.transforms[0].transform.translation.x
	y = msg.transforms[0].transform.translation.y
	z = msg.transforms[0].transform.translation.z
	# ar_id_turtlebot = '0'
	# ar_id_target = '0'
	global msg1
	global msg2
	# msg1 = 0
	# msg2 = 0
	ar_id = msg.transforms[0].child_frame_id
	if ar_id == 'ar_marker_2':
		global ar_id_turtlebot
		# global msg1
		ar_id_turtlebot = ar_id
		msg1 = msg
		# print msg1
		# print("15")
	elif ar_id == 'ar_marker_0': 
		global ar_id_target
		# global msg2
		ar_id_target = ar_id
		msg2 = msg
		# print msg2
		# print("13")
	# else:
	# 	print ("%s",ar_id)

	listener = tf.TransformListener()
	now = rospy.Time.now()


	
	try:
		# listener.waitForTransform(ar_id_turtlebot,ar_id_target, now, rospy.Duration(4.0))
		# if ar_id_turtlebot == 'ar_marker_15' and ar_id_target == 'ar_marker_13':
		
			(trans1, rot1) = listener.lookupTransform(ar_id_target,ar_id_turtlebot, rospy.Time(0))
			trans1_mat = tf.transformations.translation_matrix(trans1)
			rot1_mat   = tf.transformations.quaternion_matrix(rot1)
			mat1 = numpy.dot(trans1_mat, rot1_mat)
			print mat1
	except:
		pass


	# if ar_id == 'ar_marker_12':
	# 	print("artag_id : %s" % (ar_id))
	# 	print("x is %s, y is %s  " % (x, y))
		
# def g_transform():
# 	msg1 = callback()
# 	print msg1

def main():
	rospy.init_node('artag_lcoation')
	rospy.Subscriber("/tf", TFMessage, callback)
	# try:
	# 	print msg1
	# 	x = msg1.transforms[0].transform.rotation.x
	# 	y = msg1.transforms[0].transform.rotation.y
	# 	z = msg1.transforms[0].transform.rotation.z
	# 	w = msg1.transforms[0].transform.rotation.w
	# 	(angle_x, angle_y, angle_z) = quaternion_to_euler_angle(w,x,y,z)
	# 	print angle_x, angle_y, angle_z

	# except:
	# 	pass


	# rospy.spin()
	



	# print msg1
	# print msg1
	# ar_id_turtlebot = msg1.transforms[0].child_frame_id
	# ar_id_target = msg2.transforms[0].child_frame_id
	listener = tf.TransformListener()
	# usbcam = 'usb_cam'
	# (trans1, rot1) = listener.lookupTransform('ar_id_0', 'ar_id_2', rospy.Time(0))
	# trans1_mat = tf.transformations.translation_matrix(trans1)
	# rot1_mat   = tf.transformations.quaternion_matrix(rot1)
	# mat1 = numpy.dot(trans1_mat, rot1_mat)
	# print mat1

def publish(tran_x, tran_y):
	pub = rospy.Publisher('user_messages', AT_Message, queue_size=10)

	
    # Construct a string that we want to publish
    # (In Python, the "%" operator functions similarly
    #  to sprintf in C or MATLAB)

	text1 = raw_input("If you want relative congiuration, press <y>:")


	if text1 == 'y':
		message = AT_Message()
		message.tran_x = tran_x
		message.tran_y = tran_y

	    # Publish our string to the 'chatter_talk' topic
		pub.publish(message)
    



if __name__ == '__main__':
	# timeout = time.time() + 3   # 3 second from now
	# while time.time() < timeout:
	#     main()
	#     print ("000")

	# else:
	# 	print msg1
	# 	quit()

	t_end = time.time() + 5
	while time.time() < t_end:
    		print time.time()
    		main()

	else:
		x1 = msg1.transforms[0].transform.rotation.x
		y1 = msg1.transforms[0].transform.rotation.y
		z1 = msg1.transforms[0].transform.rotation.z
		w1 = msg1.transforms[0].transform.rotation.w
		(angle_x1, angle_y1, angle_z1) = quaternion_to_euler_angle(w1,x1,y1,z1)
		print ("Euler Angle from Quaternion (turtlebot): %s, %s, %s ") % (angle_x1, angle_y1, angle_z1)
		x2 = msg2.transforms[0].transform.rotation.x
		y2 = msg2.transforms[0].transform.rotation.y
		z2 = msg2.transforms[0].transform.rotation.z
		w2 = msg2.transforms[0].transform.rotation.w
		(angle_x2, angle_y2, angle_z2) = quaternion_to_euler_angle(w2,x2,y2,z2)
		print ("Euler Angle from Quaternion (AR tag): %s, %s, %s ") % (angle_x2, angle_y2, angle_z2)

		g_TC = np.array([[np.cos(np.deg2rad(angle_z1))*np.cos(np.deg2rad(angle_y1)), np.sin(np.deg2rad(angle_z1))*np.cos(np.deg2rad(angle_y1)), -np.sin(np.deg2rad(angle_y1)), msg1.transforms[0].transform.translation.x],
						[np.cos(np.deg2rad(angle_z1))*np.sin(np.deg2rad(angle_y1))*np.sin(np.deg2rad(angle_x1)) - np.sin(np.deg2rad(angle_z1))*np.cos(np.deg2rad(angle_x1)), np.sin(np.deg2rad(angle_z1))*np.sin(np.deg2rad(angle_y1))*np.sin(np.deg2rad(angle_x1)) + np.cos(np.deg2rad(angle_z1))*np.cos(np.deg2rad(angle_x1)), np.cos(np.deg2rad(angle_y1))*np.sin(np.deg2rad(angle_x1)), msg1.transforms[0].transform.translation.y],
						[np.cos(np.deg2rad(angle_z1))*np.sin(np.deg2rad(angle_y1))*np.cos(np.deg2rad(angle_x1)) + np.sin(np.deg2rad(angle_z1))*np.sin(np.deg2rad(angle_x1)), np.sin(np.deg2rad(angle_z1))*np.sin(np.deg2rad(angle_y1))*np.cos(np.deg2rad(angle_x1)) - np.cos(np.deg2rad(angle_z1))*np.sin(np.deg2rad(angle_x1)), np.cos(np.deg2rad(angle_y1))*np.cos(np.deg2rad(angle_x1)), msg1.transforms[0].transform.translation.z],
						[0,0,0,1]],float)
		# print g1

		g_AC = np.array([[np.cos(np.deg2rad(angle_z2))*np.cos(np.deg2rad(angle_y2)), np.sin(np.deg2rad(angle_z2))*np.cos(np.deg2rad(angle_y2)), -np.sin(np.deg2rad(angle_y2)), msg2.transforms[0].transform.translation.x],
						[np.cos(np.deg2rad(angle_z2))*np.sin(np.deg2rad(angle_y2))*np.sin(np.deg2rad(angle_x2)) - np.sin(np.deg2rad(angle_z2))*np.cos(np.deg2rad(angle_x2)), np.sin(np.deg2rad(angle_z2))*np.sin(np.deg2rad(angle_y2))*np.sin(np.deg2rad(angle_x2)) + np.cos(np.deg2rad(angle_z2))*np.cos(np.deg2rad(angle_x2)), np.cos(np.deg2rad(angle_y2))*np.sin(np.deg2rad(angle_x2)), msg2.transforms[0].transform.translation.y],
						[np.cos(np.deg2rad(angle_z2))*np.sin(np.deg2rad(angle_y2))*np.cos(np.deg2rad(angle_x2)) + np.sin(np.deg2rad(angle_z2))*np.sin(np.deg2rad(angle_x2)), np.sin(np.deg2rad(angle_z2))*np.sin(np.deg2rad(angle_y2))*np.cos(np.deg2rad(angle_x2)) - np.cos(np.deg2rad(angle_z2))*np.sin(np.deg2rad(angle_x2)), np.cos(np.deg2rad(angle_y2))*np.cos(np.deg2rad(angle_x2)), msg2.transforms[0].transform.translation.z],
						[0,0,0,1]],float)
		# print g2

		rot_matrix_T = quaternion_matrix(np.array([x1,y1,z1,w1]))
		trans_matrix_T = np.array([[0,0,0,msg1.transforms[0].transform.translation.x],
								[0,0,0,msg1.transforms[0].transform.translation.y],
								[0,0,0,msg1.transforms[0].transform.translation.z],
								[0,0,0,0]]);

		g_T = rot_matrix_T + trans_matrix_T

		rot_matrix_A = quaternion_matrix(np.array([x2,y2,z2,w2]))
		trans_matrix_A = np.array([[0,0,0,msg2.transforms[0].transform.translation.x],
								[0,0,0,msg2.transforms[0].transform.translation.y],
								[0,0,0,msg2.transforms[0].transform.translation.z],
								[0,0,0,0]]);

		g_A = rot_matrix_A + trans_matrix_A

		# g_AT_2 = np.dot(g_A, inv(g_T))
		# print g_AT_2

		g_AT = np.dot(g_AC, inv(g_TC))
		print("")
		print("Homogeneous Matrix of AR tag frame relative to Turtlebot frame")
		print g_AT

		tran_x = g_AT[0,3]
		tran_y = g_AT[1,3]

		print ("")

		print ("Relative Configuration of ar_marker_2 with respect to ar_marker_0")
		print ("x distance: %s") % tran_x
		print ("y distance: %s") % tran_y

		publish(tran_x, tran_y)





