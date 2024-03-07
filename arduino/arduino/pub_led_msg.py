import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from arduino.getchar import Getchar

class PubPT_MSG(Node):

    def __init__(self):
        super().__init__('pub_pt_msg')
        self.pub_pt = self.create_publisher(String, 'pt_msg', 10)
        self.pt_msg = String()
        
    def pub_pt_msg(self, pt_msg):
        msg = String()
        msg.data = pt_msg
        self.pub_pt.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    node = PubPT_MSG()

    #rclpy.spin(node)
    try:
        kb = Getchar()
        key =''
        while rclpy.ok():
            key = kb.getch()
            if key == '1':
                node.pub_pt_msg('down')
            elif key == '2':
                node.pub_pt_msg('up')
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
