import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from .getchar import Getchar


MAX_LIN_SPD = 0.22
MAX_ANG_SPD = 2.84

MIN_LIN_SPD = -0.22
MIN_ANG_SPD = -2.84

LIN_SPD_STEP = 0.01
ANG_SPD_STEP = 0.1

msg = """
Control Your TurtleBot3!
---------------------------
Moving around:
        w
   a    s    d
        x

w/x : increase/decrease linear velocity (Burger : ~ 0.22)
a/d : increase/decrease angular velocity (Burger : ~ 2.84)

space key, s : force stop

CTRL-C to quit
"""


class RemoteTB3(Node):

    def __init__(self):
        super().__init__('remote_tb3')

def main(args=None):
    rclpy.init(args=args)
    node = RemoteTB3()
    tw = Twist()
    kb = Getchar()
    pub = node.create_publisher(Twist, '/cmd_vel', 10)
    
    lin_spd = 0.0
    ang_spd = 0.0
    
    try:
            print(msg)
            while rclpy.ok():
                key = kb.getch()
                if key == 'w':
                    if MAX_LIN_SPD >= lin_spd + LIN_SPD_STEP:
                        lin_spd = lin_spd + LIN_SPD_STEP
                        print(lin_spd)
                    else:
                        lin_spd = MAX_LIN_SPD
                
                elif key == 'x':
                    if MIN_LIN_SPD <= lin_spd - LIN_SPD_STEP:
                        lin_spd = lin_spd - LIN_SPD_STEP
                    else:
                        tw.linear.x = MIN_LIN_SPD
                elif key == 'a':
                    if MAX_ANG_SPD >= ang_spd + ANG_SPD_STEP:
                        ang_spd = ang_spd + ANG_SPD_STEP
                    else:
                        ang_spd = MAX_ANG_SPD
                
                elif key == 'd':
                    if MIN_ANG_SPD <= ang_spd - ANG_SPD_STEP:
                        ang_spd = ang_spd - ANG_SPD_STEP
                    else:
                        ang_spd = MIN_ANG_SPD
                elif key == 's' or key == ' ':
                    lin_spd = ang_spd = 0.0
                tw.linear.x = lin_spd
                tw.angular.z = ang_spd
                print('linear speed = %s, angular speed = %s' % (tw.linear.x, tw.angular.z))
                pub.publish(tw)
                
                
                    
            sys.exit(1)
            rclpy.spin(node)
    except KeyboardInterrupt:
        tw.linear.x = tw.angular.z = 0.0
        pub.publish(tw)
        node.get_logger().info('Keyboard Interrupt(SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()
        
if __name__ == '__main__':
    main()
