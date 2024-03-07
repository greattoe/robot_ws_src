import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from .getchar import Getchar


class RemoteTurtle(Node):

    def __init__(self):
        self.pose = Pose()
        self.tw = Twist()
        super().__init__('turtle_pose_sub')
        self.subscription = self.create_subscription(
            Pose,		#topic type
            '/turtle1/pose',	#topic name
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.pose = msg
        self.get_logger().info('x = "%s", y="%s", theta="%s"' %(self.pose.x, self.pose.y, self.pose.theta))


def main(args=None):
    rclpy.init(args=args)
    node = RemoteTurtle()
    rclpy.spin(node)
    try:
            while rclpy.ok():
                ### =============================================================================
                print('x = "%s", y="%s", theta="%s"' %(self.pose.x, self.pose.y, self.pose.theta))
                ### =============================================================================
            sys.exit(1)
            rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt(SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()
        
if __name__ == '__main__':
    main()
