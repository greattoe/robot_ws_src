import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from nav_pkg.getchar import GetChar

class PubGoal_MSG(Node):

    def __init__(self):
        super().__init__('pub_goal_msg')
        self.pub = self.create_publisher(String, 'goal_msg', 10)
        self.goal_msg = String()
        
    def pub_goal_msg(self, goal_msg):
        msg = String()
        msg.data = goal_msg
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    node = PubGoal_MSG()

    #rclpy.spin(node)
    try:
        kb = GetChar()
        key =''
        while rclpy.ok():
            key = kb.getch()
            if key == '0':
                node.pub_goal_msg('goal0')
            elif key == '1':
                node.pub_goal_msg('goal1')
                print("goal1")
            elif key == '2':
                node.pub_goal_msg('goal2')
                print("goal2")
            elif key == '3':
                node.pub_goal_msg('goal3')
                print("goal3")
            elif key == '4':
                node.pub_goal_msg('goal4')
                print("goal4")
            else:
                pass
    except KeyboardInterrupt:
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    
            node.destroy_node()
            rclpy.shutdown()


if __name__ == '__main__':
    main()
