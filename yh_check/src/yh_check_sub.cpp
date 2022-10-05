#include <ros/ros.h>
#include <yh_check/yhCheck.h>

bool distance = true;
bool camera = true;

class Mysub{
    private:
    ros::NodeHandle nh;
    ros::Subscriber sub_distance;
    ros::Subscriber sub_camera;
    bool distance = true;
    bool camera = true;
    
    public:
    Mysub(void){
        sub_distance = nh.subscribe("check_distance",10, &Mysub::distanceCallback, this);
        sub_camera = nh.subscribe("check_distance",10 , &Mysub::camearaCallback, this);

    };

};

void distanceCallnack(const yh_check::yhCheck::ConstPtr& msg){
    distance = msg ->data;
    if(distance && camera){
        ROS_INFO("OK");
    };
};

void cameraCallback(const yh_check::yhCheck::ConstPtr& msg){
    camera = msg -> data;
    if(distance && camera){
        ROS_INFO("OK");
    };
};

int main(int argc , char ** argv){
    ros::init(argc,argv,"yh_check_sub");
    ros::NodeHandle nh;
    ros::Subcrliber sub_distance = nh.subscribe("check_distance",10,distanceCallback);
    ros::subscriber sub_camera = nh.subscribe("check_distance",10,cameraCallback);
    ros::spin();

    return 0 ;
};