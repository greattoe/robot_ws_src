import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge
import cv2
import numpy as np

class ImageCovertor(Node):

    def __init__(self):
        super().__init__('img_convert')
        qos_profile = QoSProfile(depth=10)

        self.subscription = self.create_subscription(CompressedImage, 
                'camera/image/compressed', 
                self.get_compressed, 
                10)

        self.pub_img = self.create_publisher(Image, 'image_raw', qos_profile)
        self.bridge = CvBridge()

    def get_compressed(self, msg):
        self.cv_img = self.bridge.compressed_imgmsg_to_cv2(msg, "bgr8")
        self.img_msg = self.bridge.cv2_to_imgmsg(self.cv_img)#, "bgr8")
        self.pub_img.publish(self.img_msg)

def main(args=None):
    rclpy.init(args=args)
    node = ImageCovertor()
    try:
        print("start publish image_raw...") 
        rclpy.spin(node)     
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt(SIGINT)')
        print("finish publish image_raw...") 


if __name__ == '__main__':
    main()
