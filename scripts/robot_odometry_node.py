import rospy
from nav_msgs.msg import Odometry

def robot_odometry_node():
    rospy.init_node('robot_odometry_node')
    pub = rospy.Publisher('odom', Odometry, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        odom_msg = Odometry()
        odom_msg.header.stamp = rospy.Time.now()
        odom_msg.header.frame_id = 'odom'
        odom_msg.pose.pose.position.x = 0.0  # start position
        odom_msg.pose.pose.position.y = 0.0
        odom_msg.pose.pose.position.z = 0.0
        odom_msg.pose.pose.orientation.x = 0.0
        odom_msg.pose.pose.orientation.y = 0.0
        odom_msg.pose.pose.orientation.z = 0.0
        odom_msg.pose.pose.orientation.w = 1.0
        pub.publish(odom_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        robot_odometry_node()
    except rospy.ROSInterruptException:
        pass