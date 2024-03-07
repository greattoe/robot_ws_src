import rclpy, sys
from rclpy.node import Node
from rclpy.qos import QoSProfile

from geometry_msgs.msg import Twist
from turtle_pkg.getchar import Getchar

msg = """
------------------------------------

            forward
              +---+
              | w |
          +---+---+---+
turn left | a | s | d | turn right
          +---+---+---+
           backward
           
### space for stop\n

------------------------------------
"""

class RemoteTurtle(Node):

    def __init__(self):
        self.cnt_sec = 0
        super().__init__('remote_turtle')
        qos_profile = QoSProfile(depth=10)
        #self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', qos_profile)
        self.timer    = self.create_timer(1, self.count_sec)
        #self.subscription  # prevent unused variable warning

    def get_pose(self, msg):
        self.pose = msg
        #self.get_logger().info('x = "%s", y="%s", theta="%s"' %(self.pose.x, self.pose.y, self.pose.theta))

    def count_sec(self):
        self.cnt_sec = self.cnt_sec + 1
        #print(self.cnt_sec)


def main(args=None):
    rclpy.init(args=args)
    node= RemoteTurtle()
    pub = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
    tw = Twist()
    kb = Getchar()
    key = ' '
    count = 0
    print(msg)
    try:
            while rclpy.ok():
                key = kb.getch()
                if      key == 'w':
                    print("forward")
                    count = count + 1
                    tw.linear.x  =  tw.angular.z =  0.0
                    tw.linear.x  =  2.0
                elif key == 's':
                    print("backward")
                    count = count + 1
                    tw.linear.x  =  tw.angular.z =  0.0
                    tw.linear.x  = -2.0
                elif key == 'a':
                    print("turn left")
                    count = count + 1
                    tw.linear.x  =  tw.angular.z =  0.0
                    tw.angular.z = 2.0
                elif key == 'd':
                    print("turn right")
                    count = count + 1
                    tw.linear.x  =  tw.angular.z =  0.0
                    tw.angular.z = -2.0
                elif key == ' ':
                    count = count + 1
                    print("stop")
                    tw.linear.x  =  tw.angular.z =  0.0
                pub.publish(tw)
                count = count % 15
                if count == 0:
                    print(msg)
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
