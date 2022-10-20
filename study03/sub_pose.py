import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from turtlesim_msgs.msg import Pose

class Turtle_PoseSubscriber(Node):
    def __init__(self):
        super().__init__('turtle_pose_sub')
        self.subscription = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.listener_callback,
            10)
        self.subscription
    def listener_callback(self, msg):
        self.get_logger().info('x="%s" y="%s" th="%s"' % (msg.x, msg.y, msg.theta))

def main(args=None):
    rclpy.init(args=args)
    turtle_pose_subscriber = Turtle_PoseSubscriber()
    rclpy.spin(turtle_pose_subscriber)
    turtle_pose_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
