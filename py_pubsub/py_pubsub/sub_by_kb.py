import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Sub_by_KB(Node):

    def __init__(self):
        super().__init__('sub_by_kb')
        self.create_subscription(String, 'control', self.get_control,10)

    def get_control(self, msg):
        print('"%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    node = Sub_by_KB()

    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
