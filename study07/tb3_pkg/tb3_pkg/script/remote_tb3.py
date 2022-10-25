import rclpy, sys
from rclpy.node import Node
from rclpy.qos import QoSProfile

from geometry_msgs.msg import Twist
from tb3_pkg.getchar import Getchar

MAX_LINEAR_SPEED = 0.22
MAX_ANGULAR_SPEED = 2.84

msg = """           forward
              +---+
              | w |
          +---+---+---+
turn left | a | s | d | turn left
          +---+---+---+
             backward
### space for stop\n
"""

class RemoteTurtle(Node):
    def __init__(self):
        self.cnt_sec = 0
        super().__init__('remote_tb3')
        qos_profile = QoSProfile(depth=10)
        #self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', qos_profile)
        self.timer    = self.create_timer(1, self.count_sec)
        #self.subscription  # prevent unused variable warning

    def get_pose(self, msg):
        self.pose = msg
        #self.get_logger().info('x = "%s", y="%s", theta="%s"' %(self.pose.x, self.pose.y, self.pose.theta))

    def count_sec(self):
        self.cnt_sec = self.cnt_sec + 1
        #print(self.cnt_sec)


def main(args=None):
    rclpy.init(args=args)
    node= RemoteTurtle()
    pub = node.create_publisher(Twist, '/cmd_vel', 10)
    tw = Twist()
    kb = Getchar()
    key = ' '
    count = 0
    lin_x = 0.0
    ang_z = 0.0
    print(msg)
    try:
            while rclpy.ok():
                if kb.chk_stdin():
                    key = kb.getch()
                else :
                    key = ''

                if key == 'w':
                    print("forward")
                    count += 1
                    if lin_x < MAX_LINEAR_SPEED:
                        lin_x += 0.01
                    tw.linear.x  =  tw.angular.z =  0.0
                    tw.linear.x  =  lin_x
                elif key == 's':
                    print("backward")
                    count = count + 1
                    if lin_x > -MAX_LINEAR_SPEED:
                        lin_x -= 0.01
                    tw.linear.x  =  tw.angular.z =  0.0
                    tw.linear.x  =  lin_x
                elif key == 'a':
                    print("turn left")
                    count += 1
                    if ang_z < MAX_ANGULAR_SPEED: 
                        ang_z += 0.1
                    tw.linear.x  =  tw.angular.z =  0.0
                    tw.angular.z =  ang_z
                elif key == 'd':
                    print("turn right")
                    count += 1
                    if ang_z > -MAX_ANGULAR_SPEED: 
                        ang_z -= 0.1
                    tw.linear.x  =  tw.angular.z =  0.0
                    tw.angular.z =  ang_z
                elif key == ' ':
                    count += 1
                    print("stop")
                    lin_x = ang_z = 0
                    tw.linear.x  =  tw.angular.z =  0.0
                pub.publish(tw)
                count = count % 15
                if count == 0:
                    print(msg)
                #rclpy.spin_once(node, timeout_sec=0.1)
            sys.exit(1)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt(SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()
        
if __name__ == '__main__':
    main()