#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def robot_navigation_node():
    rospy.init_node('robot_navigation', anonymous=True)
    cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        twist_msg = Twist()
        twist_msg.linear.x = 0.3
        twist_msg.angular.z = 0.2

        cmd_vel_pub.publish(twist_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        robot_navigation_node()
    except rospy.ROSInterruptException:
        pass