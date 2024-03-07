import rclpy, sys, serial
from rclpy.node import Node
from rclpy.qos import QoSProfile

from std_msgs.msg import String



sp  = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
class SubLED_MSG(Node):

    def __init__(self):
        super().__init__('sub_led_msg')
        qos_profile = QoSProfile(depth=10)
        self.subscription = self.create_subscription(
            String, '/led_msg', self.get_led_msg, qos_profile )
        self.led_msg = String()
        

                    
    def get_led_msg(self, msg):
        self.led_msg = msg.data
        
        if self.led_msg == "on":
            sp.write(b'1')
            print("1")
        elif self.led_msg == "off":
            sp.write(b'0')
            print("0")
        else:
            pass
        
        print(self.led_msg)

def main(args=None):
    rclpy.init(args=args)
    node = SubLED_MSG()
    try:    
        #while rclpy.ok():
            #pass
        #sys.exit(1)
        rclpy.spin(node)
    except KeyboardInterrupt:
    
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    
            node.destroy_node()
            rclpy.shutdown()


if __name__ == '__main__':
    main()
