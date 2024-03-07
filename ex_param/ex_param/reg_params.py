import rclpy, sys
from rclpy.node import Node
from rclpy.qos import QoSProfile

from geometry_msgs.msg import Twist
from rclpy.exceptions import ParameterNotDeclaredException
from rcl_interfaces.msg import ParameterType

class RegParams(Node):
    def __init__(self):
        super().__init__('reg_params')
        qos_profile = QoSProfile(depth=10)

        self.declare_parameter('go2wp1', 'stop')
        self.declare_parameter('go2wp2', 'stop')
        self.declare_parameter('go2wp3', 'stop')
        self.declare_parameter('go2wp4', 'stop')

def main():
    rclpy.init()
    node = RegParams()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
