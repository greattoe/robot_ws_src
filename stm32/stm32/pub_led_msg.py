import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from stm32.getchar import Getchar


class Pub_Led_Msg(Node):

    def __init__(self):
        super().__init__('pub_led_msg')
        self.pub = self.create_publisher(String, 'led_ctrl', 10)
        
def main(args=None):
    rclpy.init(args=args)

    node = Pub_Led_Msg()
    kb = Getchar()
    msg = String()
    try:
        while rclpy.ok():

          key = kb.getch()

          if key == '1':
             msg.data = "LED On"
          elif key == '0':
             msg.data = "LED Off"      
          else:
              pass

          node.pub.publish(msg)
            
    except KeyboardInterrupt:
        
        
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
        node.de.stroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
