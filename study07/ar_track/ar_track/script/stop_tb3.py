import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Twist

class StopTB3(Node):
    
    def __init__(self):
        super().__init__('stop_tb3')
        qos_profile   = QoSProfile(depth=10)
        self.pub_tw   = self.create_publisher(Twist, '/cmd_vel', qos_profile)
        self.timer    = self.create_timer(1, self.stop_tb3_)
        
    def stop_tb3_(self):
        tw = Twist()
        self.pub_tw.publish(tw)
        
        
def main(args=None):
    rclpy.init(args=args)
    node = StopTB3()
        
    try:
        print("### publish topic '/cmd_vel' to stop turtlebot3 every second!") 
        rclpy.spin(node)
                
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt(SIGINT)')
        
    finally:
        node.destroy_node()
        rclpy.shutdown()
    
            
if __name__ == '__main__':
    main()

