import rclpy, sys
from rclpy.node import Node
from rclpy.qos import QoSProfile

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

from math import radians, degrees


class RotateTurtle(Node):

    def __init__(self):
        self.pose = Pose()
        self.tw = Twist()
        super().__init__('rotate_turtle')
        qos_profile = QoSProfile(depth=10)
        self.create_subscription(Pose, '/turtle1/pose', self.get_pose,qos_profile)        

    def get_pose(self, msg):
        self.pose = msg
               
    def print_pose(self):
            print('x = "%s", y="%s", theta="%s"' %(self.pose.x, self.pose.y, self.pose.theta))


def main(args=None):
    rclpy.init(args=args)
    node= RotateTurtle()
    pub = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
    tw = Twist()
    try:
            while rclpy.ok():
                rclpy.spin_once(node, timeout_sec=0.1)
                deg = int(input("input angle to rotate(deg: "))
                
                if deg < 0:
                    dir = -1
                else:
                    dir = 1

                current = node.pose.theta
                goal = current + radians(deg)
                print('current = "%s", goal="%s"' %(degrees(current), degrees(goal)))
                
                tw.angular.z = radians(30) * dir
                if dir < 0:
                    while goal < current:
                        rclpy.spin_once(node, timeout_sec=0.1)
                        current = node.pose.theta
                        print('current = "%s"' %(degrees(current)))
                        pub.publish(tw)
                    tw.angular.z = 0.0
                    pub.publish(tw)
                    
                else:
                    while goal > current:
                        rclpy.spin_once(node, timeout_sec=0.1)
                        current = node.pose.theta
                        print('current = "%s"' %(degrees(current)))
                        pub.publish(tw)
                    tw.angular.z = 0.0
                    pub.publish(tw)
                
                #rclpy.spin_once(node, timeout_sec=0.1)
            sys.exit(1)
            rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt(SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()
        
if __name__ == '__main__':
    main()
