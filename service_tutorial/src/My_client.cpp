#include <ros/ros.h>
#include "service_tutorial/AddTwoints.h"
#include <cstdlib>

int main(int argc, char * argv[])
{
    ros::init(argc, argv, "My_client");
    
    //오류입력처리 init 으로 rosrun 을 받는데 노드이름 ,a, b 양식으로 받게함
    if(argc !=3)    {
        ROS_INFO("command: rosrun service_tutorial My_client arg1 arg2");
        ROS_INFO("arg1, arg2 : int32 number");
        return 1;
    }
    ros::NodeHandle nh;
    ros::ServiceClient my_client;
    my_client = nh.serviceClient<service_tutorial::AddTwoints>("service_channel_1");
    
    service_tutorial::AddTwoints srv;

    srv.request.a = atoi(argv[1]);
    srv.request.b = atoi(argv[2]);
    
    if (my_client.call(srv))
    {
        ROS_INFO("send srv.request.a=%d,srv.request.b=%d", srv.request.a , srv.request.b );
        ROS_INFO("receive srv: srv.respones.result=%d", srv.response.result );
    }else
    {
        ROS_ERROR("Failed to call service");
        return 1;
    };
    
    
    ros::spin();
    
    return 0;
}
