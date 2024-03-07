import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class TimerTest(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'hello', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        
        
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    node = TimerTest()

    #rclpy.spin(node)
    
    while rclpy.ok():
        rclpy.spin_once(node, timeout_sec = 0.1)
        #print(node.i)
        duration = 10
        while node.i < duration:
            rclpy.spin_once(node, timeout_sec = 0.1)
            print(duration - node.i)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
