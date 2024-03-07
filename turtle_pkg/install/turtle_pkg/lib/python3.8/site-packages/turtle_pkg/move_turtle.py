import rclpy

from rclpy.node import Node

from geometry_msgs.msg import Twist

class MoveTurtle(Node): 

    def __init__(self):
        super().__init__('move_turtle')
        
def main(args=None):
    rclpy.init(args=args)
    node= MoveTurtle()
    pub = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
    tw = Twist()
    try:
            while rclpy.ok():
                tw.linear.x = 0.0625
                tw.angular.z = 0.0625
                pub.publish(tw)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt(SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()
        
if __name__ == '__main__':
    main()
