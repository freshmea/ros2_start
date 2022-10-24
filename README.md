# ros2_start
start learning with ROS2 system 
- - -
# day 1
- - -
* 윈도우 지우고 전체 시스템을 우분투 20.04설치
* 필요한 프로그램 설치 (터미네이터, 서브라임, 파이참 )
* firefox 지우기 및 chrome 기본 설정.
* 한글모드 설정.
* https://cafe.naver.com/openrt/24070 오로카 홈페이지 참조.
* 안내에 따라서 ROS2 설치 https://cafe.naver.com/openrt/25288
* topic을 퍼블리싱 해서 turtlesim 움직이기.
- - -
# day2
- - -
* /opt/ros/foxy/setup.sh 와 ~/.bashrc 에 추가된 내용 확인.
* turtlesim 움직이기. 
* node 를 만들어서 turtlesim 움직이기. (topic)
* QoS 생략(quality of service)
* ROS programming with python3 Twist message 를 이용해서 메세지 보내기.
* topic 명령어 ros2 topic list (rt), ros2 topic info, ros2 topic echo, ros2 topic bw, ros2 topic hz, ros2 topic delay, ros2 topic pub, ros2 bag record, ros2 bag info, ros2 bag play.
- - -
# day3
- - -
* robotis 의 Gazebo simulation
* gazebo 빛 requisite 설치 https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/
* service 명령어 ros2 service list, ros2 service type, ros2 service find, ros2 service call, 
* gazebo simulation 실행.
* build -> . ~/turtlebot3_ws/install/local_setup.bash
* action 이란? 목표상태를 정하고 상태머신을 구동하여 실행.Goal Feedback Result.
* 목표(goal), 피드백, 결과값을 토픽과 서비스 방식을 혼합하여 사용. 
* action 명령어 ros2 action list -t, ros2 action info, ros2 action send_goal
* 파라미터 는 각 노드가 가진 변수. 값을 얻고 쓰는게 쉽게 접근 가능.
* parameter 명령어. ros2 param list, ros2 param describe, ros2 param get, ros2 param set, ros2 param dump, ros2 param delete
* ros2 launch turtlebot3_navigation2 navigation2.launch.py
* ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
* ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
* ros2 run turtlebot3_teleop teleop_keyboard
* 네가지 명령어로 네비게이션 실행.
- - - 
# day4
- - -
* 최종 프로젝트 팀 정하기. 
* turtle subscriber 만들기. 
* colcon build --symlink-install --package-select py_pybsub 특정 패키지만 빌드
* 14장 인터페이스 만들기. - Todo
* 시간 설정 하기(system time, ros time, steady time)- Todo
* 토픽 서비스 액션 파일 만들기. - Todo
* 런치 파일 만들고 (namespace , remapping, 파이썬으로 만들기)- Todo
* freeRTOS 설정해서 라즈베리파이 나노와 DDS 통신하기. 
* http://wiki.ros.org/rviz

- - -
# day5
- - -
* 인터페이스 만들기.
* 패키지 설치 ros2 pkg create topic_service_action_rclpy_example --build-type ament_python --dependencies rclpy std_msgs
* 목적 각도에 맞게 거북이 움직이기.
* topic_service_action excute and analyze. 
- - -
# day6
- - -
* script 폴더 설정.
* main 함수 쪽으로 몇가지 함수 이동.
* https://github.com/greattoe/ros2tutorial/blob/main/turtlesim/2_subscribe_turtle_pose.md
* 
