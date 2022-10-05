# ubuntu_los
cm roscore
rosrun 파일 노드

현재위치에 패키지 생성 명령어 catkin_create_pkg 이름 의존성1 의존성2
ex. catkin_create_pkg topic_2 roscpp rospy std_msgs
ros 통신 그림으로 확인 rqt_graph

topic_2 패키지 second_pub,sub.cpp / py_second_pub,sub.py
topic_test 과제 패키지

init(a,a,"노드파일이름")
nh.~~~("토픽 등 이름 설정",위에 작동 함수)

파이썬
#!/usr/bin/python
# -*- coding: utf-8 -*-

chmod +x * 권한

topic_tutorial
topic_2
topic_test
-0929
[msg_tutorial](./msg_tutorial/)
    msg_tutorial 패키지 만들고 msg에 Mymsg.msg 만들고 노드 만들고 실행해봄

srv 파일
--- 로 나눠서 윗부분은 request 할때
            아랫부분은 response 로 구분해놓음.
            *message는 다 보내므로 구분 x

rospy.ServiceProxy 서비스 생성
