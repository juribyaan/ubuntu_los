#!/usr/bin/python
# -*- coding: utf-8 -*-
import rospy
from msg_tutorial.msg import Mymsg

def msgcallback(msg):
    rospy.loginfo('receive msg : %d',msg.stamp.secs);
    rospy.loginfo('receive msg : %d',msg.stamp.nsecs);
    rospy.loginfo('receive msg : %d',msg.data);



def msg_listener():
    rospy.init_node("py_m_s");
    rospy.Subscriber("hallung", Mymsg, msgcallback,queue_size=30);
    rospy.spin();
    
if __name__ == "__main__":
    msg_listener();