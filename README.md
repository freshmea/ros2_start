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
* turtlebot3 기체 구동.
* 핫스팟 설정 https://github.com/greattoe/ros_tutorial_kr/blob/master/ros1_tutorial/turtlebot3/tb3_1_set_hotspot_on_1804.md
* sd 카드에 SBC 셋업 
* https://emanual.robotis.com/docs/en/platform/turtlebot3/sbc_setup/#sbc-setup
* 터틀봇3 텔레오피 키보드로 작동 확인
- - -
# day7
- - -
* 라즈베리 카메라 설치.
* 라즈베리 카메라 연결 . https://rudalskim.tistory.com/275 -- 실패.
* 디바이스 세팅 https://jdu-stuff.tistory.com/50
	* git clone --branch ros2 https://github.com/ros-perception/vision_opencv.git 안됨. branch 를 foxy 로 함.
* turtlebot3 topic 확인하고 type 이 무잇인지 확인.
* 새로운 패키지 만듬.
	* ros2 pkg create tb3 --build-type ament_python --dependencies rclpy geometry_msgs
	* 
* 라즈베리 카메라 설치 
	* https://chuckmails.medium.com/enable-pi-camera-with-raspberry-pi4-ubuntu-20-10-327208312f6e 라즈파이 설정 사용하기.
* ar_track 실행하기
	* sudo apt install ros-foxy-tf-transformations 실행해서 설치. 
	* sudo pip3 install transforms3d 설치
* ar_track 의 mv_tb3, test_mv_tb3, pub_tb3_pose2d, straight_by_pose2d 코드 변경. 
- - -
# day8
- - -
* vnc 설정 https://ghostweb.tistory.com/804
* 라즈피캠 카메라 작동 확인 완료!!
	* https://github.com/christianrauch/raspicam2_node 라즈피캠 지시대로 설치.
	* 카메라 디바이스 설치. (https://chuckmails.medium.com/enable-pi-camera-with-raspberry-pi4-ubuntu-20-10-327208312f6e)
	* raspicam dev/video0 가 생기지 않는다면 https://www.codetd.com/en/article/12943496 여기에서 추천해주는 순서대로 실행.
	* boot/firmware/
	* rivz2 로 영상 확인. 
	* /boot/firmware/config.txt 맨 아래 다음 추가.
	* start_x =1 
	* gpu_mem = 128
	* sudo usermod -a -V video ubuntu
	* 실행 명령.
	* ros2 run raspicam2 raspicam2_node --ros-args --params-file `ros2 pkg prefix raspicam2`/share/raspicam2/cfg/params.yaml
* 노트북 usb_cam 확인. 
* sudo apt install ros-foxy-usb-cam
* source /opt/ros/foxy/setup.bash
* ros2 run usb_cam usb_cam_node_exe ---> qrt 에서 확인.
* ros2 launch usb_cam demo_launch.py
* https://github.com/JMU-ROBOTICS-VIVA/ros2_aruco AR 마커 설치.
* 터틀봇3 안에서 raspicam_node2/cfg/params.cfg : compressed -> raw 로 바꿈.
* id --> 등록된 사용자그룹
* 터틀봇3 의 카메라가 잘 되지 않아서 https://github.com/clydemcqueen/opencv_cam 이것을 빌드함.
* https://github.com/ptrmu/ros2_shared 이것도 같이 빌드함 리콰이어됨.
- - -
# day9
- - -
* raspicam2_node 가 발행하는 image topic 중 camera/image/compressed 의 type 이 두개이다. 
* ros2 topic echo /ar_pose_marker 분석.
* ros2 run image_transport republish raw --ros-args --remap in:=/camera/image/compressed --remap out:=/image_raw --> image 를 다시 변경. 
* ar_track sub_marker_pose 변경. 
* camera가 발행하는 topic 들과 압축된 topic compressed 그것들 사이의 변경 방법을 정리할 필요가 있다. 
* ros2 run py_pubsub listener image trasffer 를 만듬.
- - -
# day10
- - -
* launch 파일에 camera node 같이 동작하게 만들기.(turtlebot3/src의 launch 폴더의 robot.launch.py 파일을 고침.  )
* raspicam dev/video0 가 생기지 않는다면 https://www.codetd.com/en/article/12943496
 여기에서 추천해주는 순서대로 실행. 
* move_tb3.py 수정. 라디안과 디그리 혼선 잡고. 멈추지 않는 현상 해결. 
- - -
# day11
- - -
* ar_track_mark2 시연.
* 마커를 찾고 직각 삼각형 경로로 이동하기. 
* 아이디어 회의: 공장 관리->
	* 지도 그리기.
	* 충전 포트 에서 출발. 다시 충전 포트로 돌아 오기. 정해진 시간마다 반복하기.
	* 정해진 위치에서 사진 찍기. 관리자에게 메세지(카톡 API 사용) 보내기.
	* 
	* 버튼 누르기
	* 
* 집안환경-
	* 충전 포트 로 충전하기.
	* 웰컴 투 홈. 메세지.
	* 불켜져 있는지 확인하고 끄기.
	* 가스 점검.
	* 침입자 확인.
	* 사람인식해서 로그 저장.
	* 리모컨 찾아오기. 
	* 정해진 시간에 약 가지고 오기. 
	* 빨래감을 빨래바구니에 넣기. 
	* 정해진 위치에 물건 놓기.
	* 
- - -
# day12
- - -
* action 연습.
* arithmetic action server client.
* 레이저 데이터가 나오지 않아서 원인을 찾음. 
* 첫번째 세팅할 때 레이저세팅이 잘못 됨. git clone -b ros2-devel https://github.com/ROBOTIS-GIT/ld08_driver.git LSD-01 또는 02 설정을 확인. 
* rviz2 내비게이션 에서 send-goal  명령어가 무엇인지 확인. 
* followwaypoints 를 만듬.
- - -
# day13
- - -
* SCADA ICT 스마트팩토리 소개자료. - 기업 소개.
* 스마트 팩토리, 분석.
* 현대모비스 울산공장 3D- 유니티. 현장(공장) 에서 요구하는 작업을 구현. 메타팩토리-디지털트윈
* 현장에서 사용하는 로봇의 운영 시스템은 어떤것을 쓰는가?
* 웹 대시보드는 어떤 프로그램은로 만듬?
* nqtp? 다양한 정보의 시그널을 받는 서버?.. 서버를 어떤 프로그램으로 운영하나?
* 자동 데이터 구축- 서버 구축 - 실시간 모니터링 - 데이터 선정 - 생산 관리 시스템(MES)
* 3~ 6개월 사이로 프로젝트 진행. - 프로젝트의 매출 규모나 순수익은?
* 
* 스마트HACCP 스마트팩토리와 연관이 큼. 