import rclpy, sys
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
from rcl_interfaces.srv import SetParameters, GetParameters, ListParameters
from rclpy.exceptions import ParameterNotDeclaredException
from rclpy.parameter import Parameter
#from rcl_interfaces.msg import Parameter, ParameterType

SVC_MSG = (sys.argv[1])

class ReqSetParam(Node):
    def __init__(self):
        super().__init__('req_set_param')
        qos_profile = QoSProfile(depth=10)
        self.cli = self.create_client(SetParameters, 'move_by_param/set_parameters')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = SetParameters.Request()
    def send_request(self):
        self.req.parameters = [Parameter(name='go_turtle', value=SVC_MSG).to_parameter_msg()]
        self.future = self.cli.call_async(self.req)



def main(args=None):
    rclpy.init(args=args)

    client = ReqSetParam()
    client.send_request()

    while rclpy.ok():
        rclpy.spin_once(client)
        if client.future.done():
            try:
                response = client.future.result()
                print(response)
            except Exception as e:
                client.get_logger().info(
                    'Service call failed %r' % (e,))
            break

    client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
