#!/usr/bin/python
#-*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Int32

def m_c_b(msg):
    rospy.loginfo("msg : %d",msg.data);

def my_listener():
    rospy.init_node("py_second_sub");
    rospy.Subscriber("my_count", Int32, m_c_b ,queue_size=100);
    rospy.spin();

if __name__ == "__main__":
    my_listener();

    