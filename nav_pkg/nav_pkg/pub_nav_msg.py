import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from arduino.getchar import Getchar

class PubNAV_MSG(Node):

    def __init__(self):
        super().__init__('pub_nav_msg')
        self.pub_nav = self.create_publisher(String, 'nav_msg', 10)
        self.nav_msg = String()
        
    def pub_nav_msg(self, nav_msg):
        msg = String()
        msg.data = nav_msg
        self.pub_nav.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    node = PubNAV_MSG()

    #rclpy.spin(node)
    try:
        kb = Getchar()
        key =''
        while rclpy.ok():
            key = kb.getch()
            if key == '1':
                node.pub_nav_msg('point1')
            elif key == '2':
                node.pub_nav_msg('point2')
            elif key == '3':
                node.pub_nav_msg('point3')
            elif key == '4':
                node.pub_nav_msg('point4')
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
