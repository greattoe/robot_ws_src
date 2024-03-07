import rclpy
from rclpy.node import Node
from math import degrees

from turtlesim.msg import Pose

class SubPose(Node): 

    def __init__(self):
        super().__init__('sub_turtle_pose')
        sub = self.create_subscription(Pose, '/turtle1/pose', self.get_pose,10)
        
        self.pose = Pose()
        
        
    def get_pose(self, msg):
        self.pose = msg
        
        #self.print_pose()
        
    def print_pose(self):
            print('x = "%s", y="%s", theta="%s"' %(self.pose.x, self.pose.y, self.pose.theta))
        
def main(args=None):
    rclpy.init(args=args)
    node= SubPose()
    
    while rclpy.ok():
        node.print_pose()

    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
