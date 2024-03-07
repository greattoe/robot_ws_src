import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge
import cv2
import numpy as np
import random
import os, sys

class ImageConvertor(Node):

    def __init__(self):
        super().__init__('img_convert')
        qos_profile = QoSProfile(depth=10)

        self.create_subscription(CompressedImage, 
                'camera/image/compressed', 
                self.get_compressed,
                10)
        self.cv_img = np.zeros([240,320]) # self.cv_img = cv2.imread("ref320.png")
        #print("===",type(self.cv_img))
        self.bridge = CvBridge()

    def get_compressed(self, msg):
        self.cv_img = self.bridge.compressed_imgmsg_to_cv2(msg, "bgr8")


def main(args=None):
    rclpy.init(args=args)
    node = ImageConvertor()
    try:
        while rclpy.ok():
        
            
        
        
        
            rclpy.spin_once(node, timeout_sec = 0.1)
            frame = node.cv_img
            print(type(frame))
            cv2.imshow("test", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            '''
            if node.cv_img is not None and node.cv_img.size != 0:
                frame = node.cv_img
                cv2.imshow("test", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            '''
            
            
            
        cv2.destroyAllWindows()
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt(SIGINT)')
        
    finally:

        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':

    main()
