#!/usr/bin/python
# -*- coding: utf-8 -*-
import rospy
from service_tutorial.srv import AddTwoints,AddTwointsResponse

def add(req):
    result = req.a + req.b;
    rospy.loginfo('a=%d,b=%d', req.a , req.b );
    rospy.loginfo("response: result = %d", result);
    
    return AddTwointsResponse(result);

def mainServer():
    rospy.init_node("My_pyservice");
    rospy.Service("service_channel_1",AddTwoints, add);
    rospy.loginfo('service server ready');
    rospy.spin();
    
if __name__ == '__main__':
    mainServer();
