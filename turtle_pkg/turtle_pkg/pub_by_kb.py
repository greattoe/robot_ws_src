import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from .getchar import Getchar


class Remote_Turtle(Node):

    def __init__(self):
        super().__init__('remote_turtle')
        #self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
def main(args=None):
    rclpy.init(args=args)

    node = Remote_Turtle()
    kb = Getchar()
    
    pub = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
    
    tw = Twist()
    try:
        while rclpy.ok():

          key = kb.getch()

          if key == 'w':
             tw.linear.x = tw.angular.z = 0.0
             tw.linear.x = 2.0
          elif key == 's':
             tw.linear.x = tw.angular.z = 0.0
             tw.linear.x = -2.0
          elif key == 'a':
             tw.linear.x = tw.angular.z = 0.0
             tw.angular.z = 2.0
          elif key == 'd':
             tw.linear.x = tw.angular.z = 0.0
             tw.angular.z = -2.0
          elif key == ' ':
             tw.linear.x = tw.angular.z = 0.0
          else:
              pass
          pub.publish(tw)

          node.pub.publish(msg)
            
    except KeyboardInterrupt:
        
        
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
        node.de.stroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
