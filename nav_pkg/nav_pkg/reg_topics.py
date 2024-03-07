import rclpy, sys, os
from rclpy.node import Node
from rclpy.qos import QoSProfile

from std_msgs.msg import String

class RegTopics(Node):
    def __init__(self):
        super().__init__('reg_topics')
        qos_profile = QoSProfile(depth=10)
        self.pub1 = self.create_publisher(String, '/wp1_msg', qos_profile)
        self.pub2 = self.create_publisher(String, '/wp2_msg', qos_profile)
        self.pub3 = self.create_publisher(String, '/wp3_msg', qos_profile)
        self.pub4 = self.create_publisher(String, '/wp4_msg', qos_profile)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = String(); msg.data = "stop"
        self.pub1.publish(msg); self.pub2.publish(msg); self.pub3.publish(msg); self.pub4.publish(msg); 
        

def main():
    rclpy.init()
    node = RegTopics()
    rclpy.spin(node)
    while rclpy.ok():
    
        try:
            pass
            
        except KeyboardInterrupt:
            node.get_logger().info('Keyboard Interrupt(SIGINT)')
            break
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
