import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from arduino.getchar import Getchar

class PubLED_MSG(Node):

    def __init__(self):
        super().__init__('pub_led_msg')
        self.pub_led = self.create_publisher(String, 'led_msg', 10)
        self.led_msg = String()
        
    def pub_led_msg(self, led_msg):
        msg = String()
        msg.data = led_msg
        self.pub_led.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    node = PubLED_MSG()

    #rclpy.spin(node)
    try:
        kb = Getchar()
        key =''
        while rclpy.ok():
            key = kb.getch()
            if key == '1':
                node.pub_led_msg('on')
            elif key == '0':
                node.pub_led_msg('off')
            else:
                pass
    except KeyboardInterrupt:
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    
            node.destroy_node()
            rclpy.shutdown()


if __name__ == '__main__':
    main()
