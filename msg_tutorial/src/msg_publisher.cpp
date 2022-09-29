#include <ros/ros.h>

#include <msg_tutorial/Mymsg.h>

int main(int argc, char** argv)
{
    ros::init(argc, argv, "msg_publisher");
    ros::NodeHandle nh;

    ros::Publisher pub = nh.advertise<msg_tutorial::Mymsg>("hallung", 20);
    ros::Rate loop_rate(2);
    
    msg_tutorial::Mymsg msg;
    int cnt = 0;

    while (ros::ok())
    {   
        msg.stamp = ros::Time::now(); //현재 시간을 msg의 stamp에 담는다.
        msg.data = cnt;
        ROS_INFO("send msg : %d",msg.stamp.sec);
        ROS_INFO("send msg : %d",msg.stamp.nsec);
        ROS_INFO("send msg : %d",msg.data);
        pub.publish(msg);
        cnt++;
        loop_rate.sleep();
    }
    
    return 0;
}