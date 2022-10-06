#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from std_srvs.srv import Empty

class TurtleClear():
    def __init__(self):
        self.clear_client = rospy.ServiceProxy("clear",Empty);
    def call(self):
        try:
            self.clear_client();
        except rospy.ServiceException as e:
            rospy.logerr("Failed : ");

if __name__ == "__main__":
    rospy.init_node("turtle_clear");
    turtle_clear = TurtleClear();
    turtle_clear.call();