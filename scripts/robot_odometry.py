#!/usr/bin/env python3

import rospy
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

# Robot's initial position
x_pos = 0
y_pos = 0

# Robot's current position
current_x = 0
current_y = 0

# Robot's goal position
goal_x = 10
goal_y = 5

# Robot's speed
linear_speed = 0.5
angular_speed = 0.5

# Function to update robot's current position
def update_position(data):
    global current_x, current_y
    current_x = data.pose.pose.position.x
    current_y = data.pose.pose.position.y

# Function to calculate the distance between two points
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))

# Function to calculate the angle between two points
def calculate_angle(x1, y1, x2, y2):
    return math.atan2(y2-y1, x2-x1)

# Initialize the node
rospy.init_node('robot_odometry')

# Create a publisher for the robot's velocity
velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

# Create a subscriber for the robot's odometry
odom_subscriber = rospy.Subscriber('/odom', Odometry, update_position)

# Set the rate of the loop
rate = rospy.Rate(10)

# Main loop
while not rospy.is_shutdown():
    # Calculate the distance and angle between the robot's current and goal positions
    distance = calculate_distance(current_x, current_y, goal_x, goal_y)
    angle = calculate_angle(current_x, current_y, goal_x, goal_y)

    # Create a Twist message
    twist_msg = Twist()

    # Set the linear velocity and angular velocity
    twist_msg.linear.x = linear_speed
    twist_msg.angular.z = angular_speed

    # If the robot is within 0.1 of the goal, stop the robot
    if distance < 0.1:
        twist_msg.linear.x = 0
        twist_msg.angular.z = 0
        velocity_publisher.publish(twist_msg)
        break

    # Publish the Twist message
    velocity_publisher.publish(twist_msg)

    # Sleep for the rate
    rate.sleep()

# Print message when finished
print("Robot has autonomously traveled across the room.")