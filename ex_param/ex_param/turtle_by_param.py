import rclpy, sys
from rclpy.node import Node
from rclpy.qos import QoSProfile

from geometry_msgs.msg import Twist
from rclpy.exceptions import ParameterNotDeclaredException
from rcl_interfaces.msg import ParameterType

class ByParam(Node):
    def __init__(self):
        super().__init__('move_by_param')
        qos_profile = QoSProfile(depth=10)
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', qos_profile)
        self.tw = Twist()
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.move_turtle)

        self.declare_parameter('go_turtle', 'stop')

    def move_turtle(self):
        param = self.get_parameter('go_turtle').get_parameter_value().string_value
        if param =='go':
            self.tw.linear.x = 0.5
            self.tw.angular.z  = 0.25
        elif param =='stop':
            self.tw.linear.x = 0.0
            self.tw.angular.z  = 0.0
        else:
            pass
        self.pub.publish(self.tw)

        self.get_logger().info('turtle %s!' % param)
        """
        
        self.set_parameters([rclpy.parameter.Parameter(
                        'go_turtle',
                        rclpy.Parameter.Type.STRING,
                        'go'
                    )])
        """

def main():
    rclpy.init()
    node = ByParam()
    node.move_turtle()
   
    rclpy.spin(node)

if __name__ == '__main__':
    main()
