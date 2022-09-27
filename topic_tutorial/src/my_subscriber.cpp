#include "ros/ros.h"
#include "std_msgs/String.h"

void msgCallback(const std_msgs::String::ConstPtr& msg){
    ROS_INFO("msg : %s", msg -> data.c_str());
}

int main(int argc, char** argv){
    ros::init(argc,argv,"my_subcriber");
    ros::NodeHandle nh;

    ros::Subscriber sub = nh.subscribe("my_topic",100,msgCallback);

    ros::spin();

    return 0;
}