import rospy
from performance_test.msg import AwsomeMsg

def callback(msg):
    rospy.loginfo("Received Msg %s" % (msg.message))

def listener():
    rospy.init_node('pylistner', anonymous=True)
    rospy.Subscriber("chatter", AwsomeMsg, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()