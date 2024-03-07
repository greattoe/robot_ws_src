import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile

class TimerTest(Node):
    
    def __init__(self):
        super().__init__('timer_test')
        qos_profile = QoSProfile(depth=10)
        self.timer  = self.create_timer(1, self.test)
        self.count  = 0
        
    def test(self):
        self.count = self.count + 1
        print(self.count)
        
        
def main(args=None):
    rclpy.init(args=args)
    node = TimerTest()
    
    try:
        print("### timer test") 
        rclpy.spin(node)
                
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt(SIGINT)')
        
    finally:
        node.destroy_node()
        rclpy.shutdown()
    
            
if __name__ == '__main__':
    main()

