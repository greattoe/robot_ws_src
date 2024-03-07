import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.create_subscription(String, 'hello', self.get_hello,10)

    def get_hello(self, msg):
        print('"%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimalsubscriber = MinimalSubscriber()

    rclpy.spin(minimalsubscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
