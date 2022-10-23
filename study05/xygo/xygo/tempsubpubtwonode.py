import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, sqrt, atan, pi, atan2
theta = 0.0
class Xytostraights(Node):
    def __init__(self):
        super().__init__('xytostraight')
        self.pose_sub = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.listener_callback,
            10)
        self.msg2 = Twist()
        self.pose_des = Pose()

    def listener_callback(self, msg):
        self.dis_x = msg.x-self.pose_des.x
        self.dis_y = msg.y-self.pose_des.y
        global theta 
        theta = atan2(self.dis_x, self.dis_y)
        self.msg2.angular.z = theta
        self.msg2.linear.x = 1.0
        self.get_logger().info('x="%s" y="%s" th="%s"' % (msg.x, msg.y, msg.theta))

    def inputGoal(self, x, y):
        self.pose_des.x = float(x)
        self.pose_des.y = float(y)

class Xytostraightp(Node):
    def __init__(self):
        super().__init__('xytostraight')
        qos_profile = QoSProfile(depth=10)
        self.twist_publisher = self.create_publisher(Twist, '/cmd_vel', qos_profile)
        self.timer = self.create_timer(0.1, self.publish_twist_msg)
        self.msg2 = Twist()
        self.pose = Pose()
        global theta
        self.msg2.angular.z = theta
        self.msg2.linear.x = 1.0

    def publish_twist_msg(self):
        self.twist_publisher.publish(self.msg2)

def main(args=None):
    rclpy.init(args=args)
    node1 = Xytostraights()
    node2 = Xytostraightp()
    try:
        x= input('input x : \n')
        y= input('input y : \n')
        node1.inputGoal(x, y)
        rclpy.spin()
    except KeyboardInterrupt:
        node.get_logger().info('keyboard Interrupt (SIGNT)')
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
