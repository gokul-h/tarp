#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class RobotLidarNode:

    def __init__(self):
        # Initialize the node with rospy
        rospy.init_node('robot_lidar_node', anonymous=False)

        # Create a publisher to control the robot's speed
        self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

        # Create a subscriber to get the robot's lidar data
        rospy.Subscriber('scan', LaserScan, self.scan_callback)

        # Create a Twist message to publish
        self.twist_msg = Twist()

        # Create a timer object that will sleep long enough to result in
        # a 10Hz publishing rate
        r = rospy.Rate(10)

        # Loop until the node is killed with Ctrl-C
        while not rospy.is_shutdown():
            # Publish the Twist message
            self.cmd_vel_pub.publish(self.twist_msg)
            # Sleep for the remainder of the cycle, or until the node is killed
            r.sleep()

    def scan_callback(self, msg):
        # Check if the robot is close to an obstacle
        if min(msg.ranges) < 0.5:
            # If so, turn left
            self.twist_msg.angular.z = 0.5
            self.twist_msg.linear.x = 0.0
        else:
            # Otherwise, continue forward
            self.twist_msg.angular.z = 0.0
            self.twist_msg.linear.x = 0.5

# Main function
if __name__ == '__main__':
    # Start the node
    robot_lidar_node = RobotLidarNode()
    # Keep it spinning to keep the node alive
    rospy.spin()