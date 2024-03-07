import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from .getchar import Getchar


msg = '''
Remote Control Turtle
'w' for forward
's' for backward
'a' for turn left
'd' for turn right
' ' for stop move
'Q' for terminate code
'''

class Remote_Turtle(Node):

    def __init__(self):
        super().__init__('remote_turtle')
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
def main(args=None):
    rclpy.init(args=args)

    node = Remote_Turtle()
    kb = Getchar()
    
    #pub = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
    
    tw = Twist()
    try:
        print(msg)
        while rclpy.ok():

            key = kb.getch()

            if key == 'w':
                print("forward")
                tw.linear.x = tw.angular.z = 0.0
                tw.linear.x = 2.0
            elif key == 's':
                print("backward")
                tw.linear.x = tw.angular.z = 0.0
                tw.linear.x = -2.0
            elif key == 'a':
                print("turn left")
                tw.linear.x = tw.angular.z = 0.0
                tw.angular.z = 2.0
            elif key == 'd':
                print("turn right")
                tw.linear.x = tw.angular.z = 0.0
                tw.angular.z = -2.0
            elif key == ' ':
                print("stop")
                tw.linear.x = tw.angular.z = 0.0
            elif key == 'Q':
                print("Bye~")
                break
            else:
              pass
            node.pub.publish(tw)
            
    except KeyboardInterrupt:
        
        
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
