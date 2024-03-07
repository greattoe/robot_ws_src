

from launch import LaunchDescription
from launch_ros.actions import Node

from launch import LaunchContext
from launch.actions import SetEnvironmentVariable



def generate_launch_description():
    ns = "/camera" 
    return LaunchDescription([
        Node(
            package='v4l2_camera',
            node_executable='v4l2_camera_node',
            output="screen",
            node_namespace=ns,
            parameters=[{"camera_calibration_file": "file:///home/spragunr/.ros/camera_info/camera.yaml"}],
            remappings=[
                ('/camera_info', '/camera/camera_info'),
                ('/image_raw', '/camera/image_raw')]
        ),
        Node(
            package="tf2_ros",
            node_executable="static_transform_publisher",
            arguments=["0","0","0","0","0","0","world","camera"],
            output="screen")

    ])

    
