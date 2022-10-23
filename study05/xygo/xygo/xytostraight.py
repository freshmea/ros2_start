import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, sqrt, atan, pi, atan2
import sys

class Xytostraight(Node):
    def __init__(self):
        super().__init__('xytostraight')
        self.pose_sub = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.listener_callback,
            10)
        qos_profile = QoSProfile(depth=10)        
        self.twist_publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', qos_profile)
        self.timer = self.create_timer(0.1, self.publish_twist_msg)
        self.msg2 = Twist()
        self.pose = Pose()
        self.pose_des = Pose()
        self.set_theta = 0
        self.dis_x = 5
        self.dis_y = 5

    def publish_twist_msg(self):
        self.twist_publisher.publish(self.msg2)

    def listener_callback(self, msg):
        # 상대거리 계산. 
        self.dis_x = self.pose_des.x-msg.x
        self.dis_y = self.pose_des.y-msg.y
        # 목적 각도 계산.
        theta = -atan2(self.dis_x, self.dis_y)+3.141592/2
        if theta >3.141592:
            theta = theta-3.141592*2
        # 180 와 -180 근처의 값이면 -90도 범위를 변경.
        if theta >2:
            theta -= 3.141592/2
            msg.theta -= 3.141592/2

        # 현재 각도와 목적 각도 를 비교 하고 방향 전환 
        if theta-msg.theta >0:
            self.msg2.angular.z = 1.0
        else :
            self.msg2.angular.z = -1.0

        # 속도 설정.
        self.msg2.linear.x = 2.0
        if abs(self.dis_x)<0.3 and abs(self.dis_y)<0.3:
            self.msg2.linear.x = 0.1
        if abs(self.dis_x)<0.1 and abs(self.dis_y)<0.1:
            self.msg2.linear.x = 0.0
            sys.exit(0)
            print('endendend')

        self.get_logger().info('x="%s" y="%s" th="%s"' % (msg.x, msg.y, msg.theta))
        self.get_logger().info('x="%s" target_th="%s"z="%s"'%(self.msg2.linear.x, theta, self.msg2.angular.z))
        

    def inputGoal(self, x, y):
        # 위치 입력.
        self.pose_des.x = float(x)
        self.pose_des.y = float(y)
        print(self.pose_des.x, self.pose_des.y)

def main(args=None):
    rclpy.init(args=args)
    node = Xytostraight()
    try:
        x= input('input x : \n')
        y= input('input y : \n')
        node.inputGoal(x, y)
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('keyboard Interrupt (SIGNT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
