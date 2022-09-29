#include <ros/ros.h>
#include <service_tutorial/AddTwoints.h>

bool add(service_tutorial::AddTwoints::Request& req,
            service_tutorial::AddTwoints::Response& res){
                res.result = req.a + req.b;
                ROS_INFO("request: a=%d, b=%d",req.a,req.b);
                ROS_INFO("response: result=%d",res.result);

                return true;
            };

int main(int argc, char *argv[])
{
    ros::init(argc, argv, "My_service");
    ros::NodeHandle nh;
    
    ros::ServiceServer my_server;
    my_server = nh.advertiseService("service_channel_1", add);
    
    ROS_INFO("Service server ready");
    ros::spin();

    return 0;
}
