#!/usr/bin/python
#-*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher("my_topic",String,queue_size=100);
    rospy.init_node("py_publisher"); #여기서 핸들 해줌
    loop_rate = rospy.Rate(10);
    msg = String();
    msg.data = "하이";

    while not rospy.is_shutdown():
        pub.publish(msg);
        loop_rate.sleep();

if __name__ == "__main__":
    try:
        talker();
    except rospy.ROSInitException: 
        pass;
