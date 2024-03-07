import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from rclpy.action import ActionClient
from action_msgs.msg import GoalStatus
from nav2_msgs.action import FollowWaypoints
# from rclpy.duration import Duration # Handles time for ROS 2
from selenium import webdriver
drv=webdriver.Chrome()
drv.get("http://localhost:8000/")

from rclpy.qos import QoSProfile
from std_msgs.msg import String
class Sub_n_Follow(Node):

    def __init__(self):
        super().__init__('sub_n_follow')
        qos_profile = QoSProfile(depth=10)
        self.create_subscription( String, '/nav_msg', self.get_nav_msg, qos_profile )
        
        self.nav_msg = String()    
    #-------------------------------------------------------
    def get_nav_msg(self, msg):
        self.nav_msg = msg
    '' #-------------------------------------------------------
    

def main(args=None):
    rclpy.init(args=args)
    node = Sub_n_Follow()
    try:   
        while rclpy.ok():
            rclpy.spin_once(node, timeout_sec = 0.1)
            
            if node.nav_msg.data == "point1":
                print("call update_z1()")
                avail_z1 = 1
                drv.execute_script("z1_busy()")
                
            elif node.nav_msg.data == "point2":
                print("call update_z2()")
                avail_z2 = 1
                drv.execute_script("z2_busy()")
                
            elif node.nav_msg.data == "point3":
                print("call update_z3()")
                avail_z3 = 1
                drv.execute_script("z3_busy()")
                
            elif node.nav_msg.data == "point4":
                print("call update_z4()")
                avail_z4 = 1
                drv.execute_script("z4_busy()")
            else:
                pass            
            print(node.nav_msg.data)
            
            
            
    except KeyboardInterrupt:
    
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    
            node.destroy_node()
            rclpy.shutdown()


if __name__ == '__main__':
    main()
