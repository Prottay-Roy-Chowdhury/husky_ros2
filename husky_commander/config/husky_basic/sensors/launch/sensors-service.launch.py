from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import EnvironmentVariable, FindExecutable, PathJoinSubstitution, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    # Include Packages

    # Declare launch files
    launch_file_lidar2d_0 = '/dev_ws/src/husky_commander/config/husky_basic/sensors/launch/lidar2d_0.launch.py'
    launch_file_lidar3d_0 = '/dev_ws/src/husky_commander/config/husky_basic/sensors/launch/lidar3d_0.launch.py'
    launch_file_camera_0 = '/dev_ws/src/husky_commander/config/husky_basic/sensors/launch/camera_0.launch.py'

    # Include launch files
    launch_lidar2d_0 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([launch_file_lidar2d_0]),
    )

    launch_lidar3d_0 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([launch_file_lidar3d_0]),
    )

    launch_camera_0 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([launch_file_camera_0]),
    )

    # Create LaunchDescription
    ld = LaunchDescription()
    ld.add_action(launch_lidar2d_0)
    ld.add_action(launch_lidar3d_0)
    ld.add_action(launch_camera_0)
    return ld
