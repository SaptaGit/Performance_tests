#include "ros/ros.h"
#include "std_msgs/String.h"

int main(int argc, char **argv)
{
  
  ros::init(argc, argv, "talker");
  ros::NodeHandle n;
  
  //Private Node Handle for the Prameter
  ros::NodeHandle private_node_handle_("~");
  private_node_handle_.param("rate", rate, int(40));

  ros::Publisher chatter_pub = n.advertise<performance_test::SuperAwsome>("chatter", 1000);
  ros::Rate loop_rate(rate);

  int count = 0;
  while (ros::ok())
  {
    performance_test::SuperAwsome msg;
	msg.message = "Test Data from C++..."
    chatter_pub.publish(msg);
    ros::spinOnce();
    loop_rate.sleep();
    ++count;
  }
  
  return 0;
}