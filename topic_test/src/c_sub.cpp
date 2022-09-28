#include <ros/ros.h>
#include <std_msgs/Int64.h>

void c_s_MCB(const std_msgs::Int64::ConstPtr& msg)
{
    ROS_INFO("0~100 : %d", msg->data);
};

int main(int argc, char** argv)
{
    ros::init(argc, argv, "c_sub");
    ros::NodeHandle nh;
    ros::Subscriber sub;
    sub = nh.subscribe("test", 100 , c_s_MCB);
    ros::spin();
    
    return 0;
}