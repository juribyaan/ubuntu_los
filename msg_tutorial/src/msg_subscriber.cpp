#include <ros/ros.h>

#include <msg_tutorial/Mymsg.h>

void msgCallback(const msg_tutorial::Mymsg::ConstPtr& msg)
{
    ROS_INFO("receive msg : %d", msg->stamp.sec);
    ROS_INFO("receive msg : %d", msg->stamp.nsec);
    ROS_INFO("receive msg : %d", msg->data);
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "msg_subscriber");
    ros::NodeHandle nh;
    ros::Subscriber sub;
    sub = nh.subscribe("hallung", 30, msgCallback);
    ros::spin();
        
    return 0;
}
