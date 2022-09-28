#include "ros/ros.h"
#include "std_msgs/Int32.h"

void msgcallback(const std_msgs::Int32::ConstPtr& msg)
{
    ROS_INFO("count : %d", msg->data);
}

int main(int argc, char** argv)
{
    ros::init(argc,argv,"second_sub");
    ros::NodeHandle nh;
    ros::Subscriber sub;
    sub = nh.subscribe("my_count", 100, msgcallback);
    ros::spin();
    
    return 0;
}
