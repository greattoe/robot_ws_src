import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from .getchar import Getchar

MAX_LIN_SPD = 0.22
MAX_ANG_SPD = 2.84
MIN_LIN_SPD = -0.22
MIN_ANG_SPD = -2.84

LIN_STEP = 0.01
ANG_STEP = 0.1


msg = '''
Remote Control Turtle
'w' for forward
's' for backward
'a' for turn left
'd' for turn right
' ' for stop move
'Q' for terminate code
'''

class Remote_TB3(Node):

    def __init__(self):
        super().__init__('remote_turtle')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        
def main(args=None):
    rclpy.init(args=args)

    node = Remote_TB3()
    kb = Getchar()
    
    #pub = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
    
    tw = Twist()
    try:
        print(msg)
        while rclpy.ok():

            key = kb.getch()

            if key == 'w':
                if tw.linear.x + LIN_STEP <= MAX_LIN_SPD:
                    tw.linear.x = tw.linear.x + LIN_STEP
                else:
                    tw.linear.x = MAX_LIN_SPD
                    
            elif key == 's':
                if tw.linear.x - LIN_STEP >= MIN_LIN_SPD:
                    tw.linear.x = tw.linear.x - LIN_STEP
                else:
                    tw.linear.x = MIN_LIN_SPD
            elif key == 'a':
                if tw.angular.z + ANG_STEP <= MAX_ANG_SPD:
                    tw.angular.z = tw.angular.z + ANG_STEP
                else:
                    tw.angular.z = MAX_ANG_SPD
            elif key == 'd':
                if tw.angular.z - ANG_STEP >= MIN_ANG_SPD:
                    tw.angular.z = tw.angular.z - ANG_STEP
                else:
                    tw.angular.z = MIN_ANG_SPD
            elif key == ' ':
                print("stop")
                tw.linear.x = tw.angular.z = 0.0
            elif key == 'Q':
                print("Bye~")
                break
            else:
              pass
            print('linear speed = %s, angular speed = %s' % (tw.linear.x, tw.angular.z)) 
            node.pub.publish(tw)
            
    except KeyboardInterrupt:
        
        
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
