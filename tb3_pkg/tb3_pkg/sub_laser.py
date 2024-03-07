import rclpy, sys
from rclpy.node import Node
from rclpy.qos import QoSProfile
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan # sensor_msgs/msg/LaserScan

class SubLaser(Node):
    
    def __init__(self):
        super().__init__('sub_laser')
        #qos_profile = QoSProfile(depth=10)
        
        # define subscriber
        self.sub_scan = self.create_subscription(
           LaserScan,           # topic type
            '/scan',        # topic name
            self.get_scan,   # callback function
            qos_profile_sensor_data)
        self.scan = LaserScan()
        
        
    def get_scan(self, msg):
        self.scan = msg
        print("front = %s" %(self.scan.ranges[0]))
        print("left  = %s" %(self.scan.ranges[90]))
        print("back  = %s" %(self.scan.ranges[180]))
        print("right = %s" %(self.scan.ranges[270]))
        print("--------------------------")
        
        
def main(args=None):
    rclpy.init(args=args)
    node = SubLaser()
    
    try:
        rclpy.spin(node)
                
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt(SIGINT)')
        
    finally:
        node.destroy_node()
        rclpy.shutdown()
    
            
if __name__ == '__main__':
    main()

