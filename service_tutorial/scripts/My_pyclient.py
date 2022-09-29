#!/usr/bin/python
# -*- coding: utf-8 -*-
import rospy
from service_tutorial.srv import AddTwoints
import sys

def addClient( a,b ):
    rospy.wait_for_service('service_channel_1');
    try:
        my_client = rospy.ServiceProxy("service_channel_1",AddTwoints);
        res = my_client(a,b);
        return res.result;
    except rospy.ServiceException as e:
        rospy.logerr("service call failed: %s",e);

if __name__ == "__main__":
    rospy.init_node("My_pyclient");

    if len(sys.argv) != 3 :
        rospy.loginfo("command: rosrun service_tutorial My_pyclient a b");
        rospy.loginfo("a,b: int32 number");
        sys.exit(1);
    a = int(sys.argv[1]);
    b = int(sys.argv[2]);
    result = addClient(a,b);
    rospy.loginfo("request: a=%d, b=%d", a, b);
    rospy.loginfo("response: result =%d",result);
    
    
