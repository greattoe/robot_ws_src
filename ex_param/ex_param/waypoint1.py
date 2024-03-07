import rclpy, sys
from rclpy.node import Node
from rclpy.parameter import Parameter
from rcl_interfaces.msg import ParameterValue
from rclpy.exceptions import ParameterNotDeclaredException
from rcl_interfaces.srv import SetParameters, GetParameters

class WayPoint1(Node):

    def __init__(self):
        super().__init__('waypoint1') # /reg_params/get_parameters
        self.cli_get = self.create_client(GetParameters, '/reg_params/get_parameters')
        while not self.cli_get.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req_get = GetParameters.Request()
        
        self.cli_set = self.create_client(SetParameters, '/reg_params/set_parameters')
        while not self.cli_set.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req_set = SetParameters.Request()

    def send_request_get(self):
            self.req_get.names = ['waypoint1']
            self.future = self.cli_get.call_async(self.req_get)
            rclpy.spin_until_future_complete(self, self.future)

    def send_request_set(self):
        self.req_set.parameters = [Parameter(name='waypoint2', value="on_").to_parameter_msg()]
        self.future = self.cli_set.call_async(self.req_set)

def main(args=None):
    param = ""
    i = 0
    rclpy.init(args=args)
    node = WayPoint1()
    node.send_request_get()
    
    while rclpy.ok():
        rclpy.spin_once(node, timeout_sec = 0.1)
        
        if node.future.done():
            try:
                response = node.future.result()
                param = response.values[0]._string_value
                print(param)
                # print(response.values[0]._string_value)   
            except Exception as e:
                node.get_logger().info('Service call failed %r' % (e,))
                break
            
        if param == "on_":
            while i < 10:
                print("waypoint1")
                i = i+ 1
            print("end waypoint1")
            node.send_request_set()
            break
            
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
