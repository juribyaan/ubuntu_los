#include <ros/ros.h>
#include <yh_check/yhCheck.h>

int main(int argc, char** argv){
    ros::init(argc,argv,"yh_check_camera");
    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<yh_check::yhCheck>("check_distance");
    ros::Rate loop_rate(2.5);
    yh_check::yhCheck

}