import rclpy, sys
from rclpy.node import Node
from rclpy.qos import QoSProfile

from geometry_msgs.msg import Twist
from rclpy.exceptions import ParameterNotDeclaredException
from rcl_interfaces.msg import ParameterType

class RegParams(Node):
    def __init__(self):
        super().__init__('reg_params')
        qos_profile = QoSProfile(depth=12)

        self.declare_parameter('z1_state', '가능')
        self.declare_parameter('z2_state', '가능')
        self.declare_parameter('z3_state', '가능')
        self.declare_parameter('z4_state', '가능')
        self.declare_parameter('z5_state', '가능')
        self.declare_parameter('z6_state', '가능')
        self.declare_parameter('z1_plate', '')
        self.declare_parameter('z2_plate', '')
        self.declare_parameter('z3_plate', '')
        self.declare_parameter('z4_plate', '')
        self.declare_parameter('z5_plate', '')
        self.declare_parameter('z6_plate', '')
        print("all parameters are initialized...")

def main():
    rclpy.init()
    node = RegParams()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
