#include "ros/ros.h"
#include "std_msgs/String.h"

int main(int argc, char** argv){

    //노드 이름 초기화
    ros::init(argc,argv,"my_publisher");
    //ros 시스템과 통신을 위한 노드 핸들선언
    ros::NodeHandle nh; 

    //퍼블리셔 선언
    //패키지()의 메시지파일()을 이용한 퍼블리셔()를 만든다
    //토픽은 ()이며 퍼블리셔큐(queue) 사이즈는 ()이다.
    ros::Publisher pub = nh.advertise<std_msgs::String>("my_topic",100);
    
    //loop주기를 10Hz로 설정
    ros::Rate loop_rate(10);

    std_msgs::String msg;
    msg.data="Hello";

    while(ros::ok()){
        pub.publish(msg);
        loop_rate.sleep();
    }

    return 0;
};

//cm 하고 roscore 켜주고 퍼블리셔 스크라이버 구동