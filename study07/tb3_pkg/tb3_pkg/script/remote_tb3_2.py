import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from tb3_pkg.get_char import Getchar

class TwistPublisher(Node):
    def __init__(self):
        super().__init__('twist_publisher')
        qos_profile = QoSProfile(depth=10)
        self.twist_publisher = self.create_publisher(Twist, '/cmd_vel', qos_profile)
        self.timer = self.create_timer(0.1, self.publish_twist_msg)
        self.count = 0
        self.key = Getchar()
        self.msg = Twist()

    def publish_twist_msg(self):
        ch = self.key.getch()
        if ch == 'w':
            self.msg.linear.x = 1.0
            self.msg.angular.z = 0.0
        elif ch == 's':
            self.msg.linear.x = -1.0
            self.msg.angular.z = 0.0
        elif ch == 'a':
            self.msg.linear.x = 0.0
            self.msg.angular.z = 1.0
        elif ch == 'd':
            self.msg.linear.x = 0.0
            self.msg.angular.z = -1.0
        elif ch == 'z':
            self.msg.linear.x = -2.0 + self.count * 4
            self.msg.angular.z = -2.5 + self.count
            self.count += 0.1
            if self.count>2:
                self.count = 0
        else :
            self.msg.linear.x = 0.0
            self.msg.angular.z = 0.0
        self.twist_publisher.publish(self.msg)
        # self.get_logger().info('Published message: {0}'.format(msg.data))
        # self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = TwistPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('keyboard Interrupt (SIGNT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
