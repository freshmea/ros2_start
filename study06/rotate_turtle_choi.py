import rclpy,sys
from rclpy.node import Node
from rclpy.qos import QoSProfile
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import degrees, radians, sqrt, sin, cos, pi


class Rotate_Turtle(Node):

    def __init__(self):
        self.pose = Pose()
        self.tw = Twist()
        self.cnt_sec = 0
        self.target = 0.0
        super().__init__('sub_turtle_pose')
        qos_profile = QoSProfile(depth=10)
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', qos_profile)
        self.subscription = self.create_subscription(
            Pose, '/turtle1/pose', self.get_pose, qos_profile )
        self.timer    = self.create_timer(0.1, self.count_sec)
        self.subscription  # prevent unused variable warning

    def get_pose(self, msg):
        self.pose = msg
        
    def get_target(self, angle):
        target = angle + self.pose.theta
        if abs(target) < radians(180):
            return target
        else:
            if target > 0:    
                return target - radians(360)
            else:
                return target + radians(360)
    def count_sec(self):
        self.cnt_sec = self.cnt_sec + 0.1

        
def main(args=None):
    rclpy.init(args=args)
    node= Rotate_Turtle()
    target = 0.0
    try:
        for i in range(10):
            rclpy.spin_once(node, timeout_sec=0.1)
        input_on = True
        while rclpy.ok():
            if input_on:
                angle = radians(int(input("input target angle(deg): ")))
                target = node.get_target(angle)
                input_on = False
            rclpy.spin_once(node, timeout_sec=0.01)
            print(f'pose theta : {degrees(node.pose.theta)}, {degrees(target)}')
            if angle > 0:
                # target 의 값을 범위 안에 설정.
                if target < -180:
                    target += radians(360)
                if target > 180:
                    target -= radians(360)
                # 부호가 같고 theta 가 target 보다 커질때 까지 증가.
                if node.pose.theta < target or node.pose.theta * target <0:
                    node.tw.angular.z = 1.5
                else:
                    node.tw.angular.z = 0.0
                    input_on = True
                    # sys.exit(1)
                node.pub.publish(node.tw)
            else:
                # target 의 값을 범위 안에 설정.
                if target > 180:
                    target -= radians(360)
                if target < -180:
                    target += radians(360)
                # 부호가 같고 theta 가 target 보다 커질때 까지 증가.
                if node.pose.theta > target or node.pose.theta * target <0:
                    node.tw.angular.z = -1.5
                else:
                    node.tw.angular.z = 0.0      
                    input_on = True
                    # sys.exit(1)
                node.pub.publish(node.tw)      
            ### ==============================================================================
        sys.exit(1)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt(SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()
        
if __name__ == '__main__':
    main()
