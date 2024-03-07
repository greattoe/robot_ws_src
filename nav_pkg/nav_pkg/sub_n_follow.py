import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from rclpy.action import ActionClient
from action_msgs.msg import GoalStatus
from nav2_msgs.action import FollowWaypoints
# from rclpy.duration import Duration # Handles time for ROS 2

from rclpy.qos import QoSProfile
from std_msgs.msg import String

class Sub_n_Follow(Node):

    def __init__(self):
        super().__init__('sub_n_follow')
        self._client = ActionClient(self, FollowWaypoints, '/FollowWaypoints')
        qos_profile = QoSProfile(depth=10)
        self.create_subscription( String, '/nav_msg', self.get_nav_msg, qos_profile )
        self.nav_msg = String()
    def send_points(self, points):
        msg = FollowWaypoints.Goal()
        msg.poses = points
        
        self._client.wait_for_server()
        self._send_goal_future = self._client.send_goal_async(msg, feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return

        self.get_logger().info('Goal accepted')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.missed_waypoints))

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.current_waypoint))
                    
    def get_nav_msg(self, msg):
        self.nav_msg = msg

def main(args=None):
    rclpy.init(args=args)
    node = Sub_n_Follow()
    rgoal = PoseStamped()
    try:   
        while rclpy.ok():
            rclpy.spin_once(node, timeout_sec = 0.1)
            
            if node.nav_msg.data == "point1":
                rgoal.header.frame_id = "map"
                rgoal.header.stamp.sec = 0
                rgoal.header.stamp.nanosec = 0
                rgoal.pose.position.z = 0.0
                rgoal.pose.position.x = 2.85
                rgoal.pose.position.y = 2.64
                rgoal.pose.orientation.w = 1.0
                
            elif node.nav_msg.data == "point2":
                rgoal.header.frame_id = "map"
                rgoal.header.stamp.sec = 0
                rgoal.header.stamp.nanosec = 0
                rgoal.pose.position.z = 0.0
                rgoal.pose.position.x = 2.85
                rgoal.pose.position.y = -0.9
                rgoal.pose.orientation.w = 1.0
                
            elif node.nav_msg.data == "point3":
                rgoal.header.frame_id = "map"
                rgoal.header.stamp.sec = 0
                rgoal.header.stamp.nanosec = 0
                rgoal.pose.position.z = 0.0
                rgoal.pose.position.x = 1.73
                rgoal.pose.position.y = -0.9
                rgoal.pose.orientation.w = 1.0
                
            elif node.nav_msg.data == "point4":
                rgoal.header.frame_id = "map"
                rgoal.header.stamp.sec = 0
                rgoal.header.stamp.nanosec = 0
                rgoal.pose.position.z = 0.0
                rgoal.pose.position.x = 1.73
                rgoal.pose.position.y = 2.6
                rgoal.pose.orientation.w = 1.0
            else:
                pass
            print(rgoal)
            mgoal = [rgoal]
            node.send_points(mgoal)
            
            
            
    except KeyboardInterrupt:
    
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    
            node.destroy_node()
            rclpy.shutdown()


if __name__ == '__main__':
    main()
