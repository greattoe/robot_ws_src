import rclpy, sys
from rclpy.node import Node
from rclpy.qos import QoSProfile

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import radians, degrees

class RotateTurtle(Node):

    def __init__(self):
        self.tw = Twist()
        self.pose = Pose()      #Pose => import Pose , self.pose(x,y,theta,linear,angular)
        #self.cnt_sec = 0        #클래스 멤버 변수
        super().__init__('rotate_turtle')
        qos_profile = QoSProfile(depth=10)              #self. = 클래스 멤버 함수
        self.create_subscription(Pose, '/turtle1/pose', self.get_pose, qos_profile)
        
        #subscriber만듬 create_subscription을 호출해서 (타입, 이름, 콜백함수의 이름, q size)

    def get_pose(self, msg):        #클래스 내부에서 만들어야 함(why? -> self.)
        self.pose = msg
        
    def print_pose(self):
        print('x = "%s", y="%s", theta="%s"' %(self.pose.x, self.pose.y, self.pose.theta))
  

def main(args=None):
    rclpy.init(args=args)
    node= RotateTurtle()
    pub = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)      #mian -> node., class -> self.
    tw = Twist()
    try:
            while rclpy.ok():
                rclpy.spin_once(node, timeout_sec=0.1)
                deg = int(input("Input angle to rotate(deg): ") )      #input :일단 화면에 출력, 문자열
                
                if deg < 0:
                    dir = -1
                else:
                    dir = 1
                
                current = node.pose.theta 
                goal = current + radians(deg)
                print('current = "%s", goal="%s"' %(degrees(current), degrees(goal)))
                
                tw.angular.z = radians(30) * dir      #radians(15) : 초당 15도씩 돌아라
                if dir < 0:
                    while goal < current :
                        rclpy.spin_once(node, timeout_sec=0.1)
                        current = node.pose.theta 
                        print("=================")
                        print('current = "%s"' %(degrees(current)))
                        pub.publish(tw)
                    tw.angular.z = 0.0 
                    pub.publish(tw)
                else:
                    while goal > current :
                        rclpy.spin_once(node, timeout_sec=0.1)
                        current = node.pose.theta 
                      
                        print("=================")
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
