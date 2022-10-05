#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
from yh_check.msg import yhCheck

class Mycheck:
    def __init__(self):
        self.sub_distance = rospy.Subscriber("check_distance", yhCheck, self.distanceCallback);
        self.sub_camera = rospy.Sybscriber("check_distance",yhCheck,self.cameraCallback);
        self.distance = true;
        self.camera = true;

    def distanceCallback(self,msg):
        self.distance = msg.data;
        if self.distance and self.camera:
            rospy.loginfo("oK");

    def cameraCallback(self,msg):
        self.camera = msg.data;
        if self.distance and self.camera:
            rospy.loginfo("Ok");

if __name__ == "__main__":
    rospy.init_node("yh_check");
    my_check = Mycheck();
    rospy.spin();