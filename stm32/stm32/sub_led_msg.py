import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

#sp  = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

class Sub_LED_MSG(Node):

    def __init__(self):
        super().__init__('sub_led_msg')
        self.create_subscription(String, 'led_ctrl', self.get_led_msg,10)

    def get_led_msg(self, msg):
    
        if msg.data == "LED On":
            print("Send '1'")
            #sp.write(b'1')
        elif msg.data == "LED Off":
            print("Send '0'")
            #sp.write(b'0')
        else:
            pass


def main(args=None):
    rclpy.init(args=args)

    node = Sub_LED_MSG()

    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
