import rclpy, sys
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped 
from rclpy.action import ActionClient
from action_msgs.msg import GoalStatus
from nav2_msgs.action import FollowWaypoints
# from rclpy.duration import Duration # Handles time for ROS 2
#'''
rgoal0 = PoseStamped()
rgoal0.header.frame_id = "map"
rgoal0.header.stamp.sec = 0
rgoal0.header.stamp.nanosec = 0
rgoal0.pose.position.z = 0.0
rgoal0.pose.position.x = 0.0
rgoal0.pose.position.y = -0.0
rgoal0.pose.orientation.w = 1.0
mgoal = [rgoal0]
#'''

class ClientFollowPoints(Node):

    def __init__(self):
        super().__init__('client_follow_points')
        self._client = ActionClient(self, FollowWaypoints, '/FollowWaypoints')
        self.subscription = self.create_subscription(
            String, '/nav_msg', self.get_nav_msg, 10 )
        self.nav_msg = String()
                    
    def get_nav_msg(self, msg):
        self.nav_msg = msg
        print("---")
        print(msg.data)

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

def main(args=None):
    global mgoal
    rclpy.init(args=args)

    follow_points_client = ClientFollowPoints()
    print('client inited')    

    rgoal = PoseStamped()
    rgoal0 = PoseStamped()
    rgoal0.header.frame_id = "map"
    rgoal0.header.stamp.sec = 0
    rgoal0.header.stamp.nanosec = 0
    rgoal0.pose.position.z = 0.0
    rgoal0.pose.position.x = 0.0
    rgoal0.pose.position.y = -0.0
    rgoal0.pose.orientation.w = 1.0
    mgoal = [rgoal0]

    rgoal1 = PoseStamped()
    rgoal1.header.frame_id = "map"
    rgoal1.header.stamp.sec = 0
    rgoal1.header.stamp.nanosec = 0
    rgoal1.pose.position.z = 0.0
    rgoal1.pose.position.x = 2.68
    rgoal1.pose.position.y = -0.99
    rgoal1.pose.orientation.w = 1.0
    print(rgoal1)
    

    rgoal2 = PoseStamped()
    rgoal2.header.frame_id = "map"
    rgoal2.header.stamp.sec = 0
    rgoal2.header.stamp.nanosec = 0
    rgoal2.pose.position.z = 0.0
    rgoal2.pose.position.x = 2.73
    rgoal2.pose.position.y = 2.64
    rgoal2.pose.orientation.w = 1.0
    print(rgoal2)
    
    if follow_points_client.nav_msg.data == "point1":
        print("point1")
        mgoal = [rgoal1]
    elif follow_points_client.nav_msg.data == "point2":
        print("point2")
        mgoal = [rgoal2]

    follow_points_client.send_points(mgoal)   
    rclpy.spin(follow_points_client)
