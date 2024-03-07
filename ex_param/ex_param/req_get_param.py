import rclpy, sys
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
from rcl_interfaces.srv import SetParameters, GetParameters, ListParameters
from rclpy.exceptions import ParameterNotDeclaredException
from rclpy.parameter import Parameter
from rcl_interfaces.msg import ParameterValue
#from rcl_interfaces.msg import Parameter, ParameterType


class ReqGetParam(Node):
    def __init__(self):
        super().__init__('req_get_param')
        qos_profile = QoSProfile(depth=10)
        self.cli = self.create_client(GetParameters, 'reg_params/get_parameters')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        
        self.param = "stop"
        self.req = GetParameters.Request()
    def send_request(self):
        self.req.names = ['go2wp1']
        self.future = self.cli.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)

    node = ReqGetParam()
    node.send_request()

    while rclpy.ok():
        print("===")
        rclpy.spin_once(node)
        print(node.param)
        if node.future.done():
            try:
                response = node.future.result()
                print(response.values[0]._string_value)
                node.param = response.values[0]._string_value
                # print(Parameter('go_turtle', list, value=response.values))
            except Exception as e:
                node.get_logger().info(
                    'Service call failed %r' % (e,))
            break

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
