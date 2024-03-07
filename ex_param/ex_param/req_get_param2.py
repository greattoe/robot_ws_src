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
        
        self.param = ""
        self.req = GetParameters.Request()
    def send_request(self):
        self.req.names = ['go2wp1']
        self.future = self.cli.call_async(self.req)
        self.param = ""
        timer_period = 1.0 #(sReqGetParamec)
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
    def timer_callback(self):
        print("in timer call back")
        self.send_request()
        if self.future.done():
            try:
                response = node.future.result()
                print(esponse.values[0]._string_value)
            except Exception as e:
                self.get_logger().info('Service call failed %r' % (e,))
        

def main(args=None):
    rclpy.init(args=args)
    node = ReqGetParam()
    while rclpy.ok():
        rclpy.spin_once(node, timeout_sec = 1)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
