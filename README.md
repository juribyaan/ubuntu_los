# ubuntu_los
명령어만들기
gedit .bashrc

cm roscore
rosrun 파일 노드

패키지 설치
sudo apt install ros-melodic-teleop-twist-keyboard

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

http://wiki.ros.org/roscpp_tutorials/Tutorials/WritingPublisherSubscriber

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

거북이 실행 키보드

rosservice list
    rosservice call /reset
    rosservice call /spawn
    rosservice call /clear

우분투 arduino 세팅
    https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/all


o x o x x x x o F
o o o x x o o o x
o x o x o o x o x
o o o o o x x o o
x x x x o o x x x
o o o o x o o o o
x o x o o o x o x
o o o o x o o o x
P x x o o x x o x

가상환경
sudo apt-get install python3-venv
python -m venv venv
source ./venv/bin/activate

패키지 설정 공유
pip freeze

pip freeze > requirements.txt

pip install -r requirements.txt

#설치

//우분투
$ sudo apt-get update

//만약 pip3이 설치되어 있지 않으면 아래 명령으로 설치
$ sudo apt install python3-pip

// matplotlib 에 대비하여 tk 모듈 설치
$ sudo apt-get install python3-tk

//우분투, 터미널에 입력
//전역에서 사용되는 pip를 미리 업그레이드
$ sudo -H pip3 install --upgrade --ignore-installed pip setuptools

//$ sudo pip3 install --upgrade pip

$ python3 -m venv venv
$ source ./venv/bin/activate

//버전 및 설치 확인 (pip의 경로가 가상환경 경로와 일치해야함)
(가상환경) $ pip -V
(가상환경) $ pip install –upgrade pip



//윈도우

//가상환경 설정
$ python -m venv venv
//활성화
$ .\venv\Scripts\Activate.ps1

//pip 업그레이드
(가상환경) $ pip install –upgrade pip

//버전 및 설치 확인 (pip의 경로가 가상환경 경로와 일치해야함)
(가상환경) $ pip -V


//opencv 및 관련 패키지 설치

// 이하 가상환경 안에서
// opencv 설치 (파이썬 3.10 이상)
$ pip install opencv-contrib-python

// 파이썬 3.6 이하
$ pip install opencv-contrib-python==3.4.1.15

// matplotlib 설치
$ pip install matplotlib
