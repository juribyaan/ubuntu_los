#include <ros/ros.h>
#include <std_msgs/Float32.h>

void msgCallback(const std_msgs::Float32::ConstPtr& msg){
    ROS_INFO("%f", msg -> data);
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "yh_connet_sub");
    ros::NodeHandle nh;
    ros::Subscriber sub =nh.subscribe("yh_connet_float", 10,msgCallback);
    ros::spin();

    return 0;
}
