from geometry_msgs.msg import PoseStamped

def waypoints(header, pose):
    
    print('success!')
    rgoal = PoseStamped()
    rgoal.header.frame_id = "map"
    rgoal.header.stamp.sec = 0
    rgoal.header.stamp.nanosec = 0
    '''
    self.rgoal.pose.position.z = 0.0
    self.rgoal.pose.position.x = 4.15
    self.rgoal.pose.position.y = -0.37
    '''
    
    rgoal.pose.position.z = -0.0
    rgoal.pose.position.x = 2.89
    rgoal.pose.position.y = -1.12
    
    rgoal.pose.orientation.w = 1.0
    #print(rgoal)
    mgoal = [rgoal]
    
    #send_points(mgoal)
