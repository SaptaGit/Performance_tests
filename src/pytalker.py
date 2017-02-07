#!/usr/bin/env python
# license removed for brevity
import rospy
from performance_test.msg import AwsomeMsg

def talker():
    pub = rospy.Publisher('chatter', AwsomeMsg, queue_size=10)
    rospy.init_node('pytalker', anonymous=True)
    rate = rospy.Rate(rospy.get_param("/rate")) 
	msg = AwsomeMsg()
    msg.message = "Test Data from Python..."
	
    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass