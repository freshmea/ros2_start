import rclpy, sys
from rclpy.node import Node
from rclpy.qos import QoSProfile
#from turtlesim.msg import Pose
from geometry_msgs.msg import Pose
from ros2_aruco_interfaces.msg import ArucoMarkers

TARGET_ID = int(sys.argv[1]) # argv[1] = id of target marker

class KeepDist(Node): 
    
    def __init__(self):
        super().__init__('sub_marker_pose')
        qos_profile = QoSProfile(depth=10)
        
        # define subscriber
        self.sub_ar_pose = self.create_subscription(
            ArucoMarkers,           # topic type
            'aruco_markers',        # topic name
            self.get_marker_pose,   # callback function
            qos_profile)
        
        self.pose = Pose()
        
    def get_marker_pose(self, msg):
        if len(msg.marker_ids) != 0:
            for i in range(len(msg.marker_ids)):
                if msg.marker_ids[i] == TARGET_ID:
                    self.pose = msg.poses[i]
                    self.print_marker_pose()
    
    def print_marker_pose(self):
        print("position_x = %s" %(self.pose.position.x))
        print("position_y = %s" %(self.pose.position.y))
        print("position_z = %s" %(self.pose.position.z))
        print("orientation_x = %s" %(self.pose.orientation.x))
        print("orientation_y = %s" %(self.pose.orientation.y))
        print("orientation_z = %s" %(self.pose.orientation.z))
        print("orientation_w = %s" %(self.pose.orientation.w))
        print("")
        
        
def main(args=None):

    rclpy.init(args=args)
    node = KeepDist()
    
    node.tw.angular.z = 0.5 * ANG_SPEED
    
    try:    
        while rclpy.ok():
            rclpy.spin_once(node, timeout_sec=0.1)
        
        node.stop_move()
        print("\n----- 1_target marker found!\n") ###########################
        
        while node.pose.position.x < -0.0155 or node.pose.position.x >  0.0155:
            if   node.pose.position.x < -0.0155:
                node.tw.angular.z =  0.125 * ANG_SPEED
            else:# node.pose.position.x >  0.025:
                node.tw.angular.z = -0.125 * ANG_SPEED
            node.pub_tw.publish(node.tw)
            rclpy.spin_once(node, timeout_sec=0.1)
        
        node.stop_move()        
        print("\n----- 2_arrived reference position!\n") ####################
        
        node.th_ref = node.theta
        node.z_ref  = node.pose.position.z
        if node.th_ref >= 0:
            node.dir =  1
        else:
            node.dir = -1
        
        angle = R - node.th_ref
                                
        if angle > R:
            angle = pi - angle
        
        if   node.th_ref > radians( 10):
            node.tb3.rotate( angle * .9)
        elif node.th_ref < radians(-10):
            node.tb3.rotate(-angle * .97)
        else:
            pass        
        print("\n----- 3_1st rotation finished!\n") #########################
        
        dist1 = abs(node.z_ref * sin(node.th_ref) * 1.125)
        node.tb3.straight(dist1)
        print("\n----- 4_move to front of marker end!\n") ###################
        
        if   node.th_ref >  radians(10):
            node.tb3.rotate(-R * 0.875)
        elif node.th_ref < -radians(10):
            node.tb3.rotate( R)
        else:
            pass        
        print("\n----- 5_2nd rotation finished!\n") #########################
        
        while node.pose.position.x < -0.0025 or node.pose.position.x >  0.0025:
            if   node.pose.position.x < -0.0025:
                node.tw.angular.z =  0.075 * ANG_SPEED
            elif node.pose.position.x >  0.0025:
                node.tw.angular.z = -0.075 * ANG_SPEED
            else:
                node.tw.angular.z =  0.0
                
            node.pub_tw.publish(node.tw)                
            rclpy.spin_once(node, timeout_sec=0.02)
            
        dist2 = node.pose.position.z - 0.185
        node.tb3.straight(dist2)
        print("\n----- 6_arrived lifting position!\n") ####################
        
        node.pub_lift_ctrl("lift_up")
        duration = node.cnt_sec + 10
        
        while node.cnt_sec < duration: 
            print(duration - node.cnt_sec)               
            rclpy.spin_once(node, timeout_sec=1.0)
        print("\n----- 7_finished loading!\n") ############################     
        
        node.tb3.straight(-dist2)
        node.tb3.rotate(R * node.dir)
        node.tb3.straight(-dist1)
        print("\n----- 8_arrived starting point!\n") ######################
        
        node.pub_lift_ctrl("lift_down")
        duration = node.cnt_sec + 8
        
        while node.cnt_sec < duration: 
            print(duration - node.cnt_sec)               
            rclpy.spin_once(node, timeout_sec=1.0)
        print("\n----- 7_finished unloading!\n") ###########################       
        
        node.tb3.straight(-0.1)
        node.tb3.rotate(R * node.dir * -1)
        
        sys.exit(1)
        rclpy.spin(node)
                
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt(SIGINT)')
        
    finally:
        node.destroy_node()
        rclpy.shutdown()
    
            
if __name__ == '__main__':
    main()

