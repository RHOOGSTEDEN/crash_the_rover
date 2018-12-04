#!/usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
import tf2_ros
import sys
from geometry_msgs.msg import Twist
from tf.transformations import *
import numpy as np


class ARFinder():

    def __init__(self, bot_frame, ar_frame, move_base):
        self.ar_frame = ar_frame
        self.bot_frame = bot_frame
        self.move_base = move_base
    

    def scanAR(self):
        timeStart = rospy.Time.now()
        timeNow = timeStart
        tfBuffer = tf2_ros.Buffer()
        tfListener = tf2_ros.TransformListener(tfBuffer)
        while(timeNow.to_sec() -timeStart.to_sec() < 5):
            canTrans = tfBuffer.can_transform(self.bot_frame, self.ar_frame, rospy.Time(0))
            if (canTrans):
                return True
            timeNow = rospy.Time.now()
        return False

    def spin(self):
        # pub = rospy.Publisher("/mobile_base/commands/velocity" , Twist, queue_size=10)
        # # D-Constants 
        # control_command = Twist()
        # control_command.linear.x = next_x  
        # control_command.linear.y = 0
        # control_command.linear.z = 0
        # control_command.angular.x = 0
        # control_command.angular.y = 0
        # control_command.angular.z = next_theta
        # pub.publish(control_command)
        q_rot = quaternion_from_euler(0, 0, 2*np.pi / 3)
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'base_link'
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = 0
        goal.target_pose.pose.orientation.w = q_rot[3]
        self.move_base.send_goal(goal)
        self.move_base.wait_for_result(rospy.Duration(60))

    #def forward():



    def findAR(self):
        count = 0
        while(count< 3):
            self.spin()
            if(self.scanAR()):
                return True
            else:
                count = count + 1
        return False

                
