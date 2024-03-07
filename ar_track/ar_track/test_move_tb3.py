import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from ar_track.move_tb3 import MoveTB3
from math import radians, degrees, sqrt, atan2


class TestMoveTB3(Node):

 def __init__(self):
        
        super().__init__('test_move_tb3')
        qos_profile = QoSProfile(depth=10)
        self.tb3 = MoveTB3()

def main(args=None):
    rclpy.init(args=args)
    node = TestMoveTB3()
    
    try:
        while rclpy.ok():
            rclpy.spin_once(node, timeout_sec = 0.1)
            angle = radians(float(input("input rotation (deg): ")))
            dist = float(input("input distance (m)  : "))
        
            node.tb3.rotate(angle)
            node.tb3.straight(dist)
                
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt(SIGINT)')
        
    finally:
        node.destroy_node()
        rclpy.shutdown()
    
            
if __name__ == '__main__':
    main()
    
