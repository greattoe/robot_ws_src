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
        
        self.not_arrived_point1 = True
        self.not_arrived_point2 = False
        self.not_arrived_point3 = False
        self.not_arrived_point4 = False
        
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
        print("Patorol Started !!!")
        while rclpy.ok():
            rclpy.spin_once(node, timeout_sec = 0.1)
            
            if node.not_arrived_point1 is True and node.not_arrived_point2 is False\
                                               and node.not_arrived_point3 is False\
                                               and node.not_arrived_point4 is False:
                rgoal1 = PoseStamped()
                rgoal1.header.frame_id = "map"
                rgoal1.header.stamp.sec = 0
                rgoal1.header.stamp.nanosec = 0
                rgoal1.pose.position.z = 0.0
                rgoal1.pose.position.x = 2.85
                rgoal1.pose.position.y = 2.64
                rgoal1.pose.orientation.w = 1.0
                print(rgoal1)
                mgoal1 = [rgoal1]
                node.send_points(mgoal1)
                print("arrived_point1")
                node.not_arrived_point1 = False
                node.not_arrived_point2 = True
                
            if node.not_arrived_point2 is True and node.not_arrived_point1 is False\
                                               and node.not_arrived_point3 is False\
                                               and node.not_arrived_point4 is False:
                
                rgoal2 = PoseStamped()
                rgoal2.header.frame_id = "map"
                rgoal2.header.stamp.sec = 0
                rgoal2.header.stamp.nanosec = 0
                rgoal2.pose.position.z = 0.0
                rgoal2.pose.position.x = 2.85
                rgoal2.pose.position.y = -0.9
                rgoal2.pose.orientation.w = 1.0
                print(rgoal2)
                mgoal2 = [rgoal2]
                node.send_points(mgoal2)
                print("arrived_point2")
                node.not_arrived_point2 = False
                node.not_arrived_point3 = True
            if node.not_arrived_point3 is True and node.not_arrived_point1 is False\
                                               and node.not_arrived_point2 is False\
                                               and node.not_arrived_point4 is False:
                
                rgoal3 = PoseStamped()
                rgoal3.header.frame_id = "map"
                rgoal3.header.stamp.sec = 0
                rgoal3.header.stamp.nanosec = 0
                rgoal3.pose.position.z = 0.0
                rgoal3.pose.position.x = 1.73
                rgoal3.pose.position.y = -0.9
                rgoal3.pose.orientation.w = 1.0
                print(rgoal3)
                mgoal3 = [rgoal3]
                node.send_points(mgoal3)
                print("arrived_point3")
                node.not_arrived_point3 = False
                node.not_arrived_point4 = True
            if node.not_arrived_point4 is True and node.not_arrived_point1 is False\
                                               and node.not_arrived_point2 is False\
                                               and node.not_arrived_point3 is False: 
               
                rgoal4 = PoseStamped()
                rgoal4.header.frame_id = "map"
                rgoal4.header.stamp.sec = 0
                rgoal4.header.stamp.nanosec = 0
                rgoal4.pose.position.z = 0.0
                rgoal4.pose.position.x = 1.73
                rgoal4.pose.position.y = 2.6
                rgoal4.pose.orientation.w = 1.0
                print(rgoal4)
                mgoal4 = [rgoal4]
                node.send_points(mgoal4)
                print("arrived_point4")
                node.not_arrived_point4 = False
    except KeyboardInterrupt:
    
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    
            node.destroy_node()
            rclpy.shutdown()


if __name__ == '__main__':
    main()
