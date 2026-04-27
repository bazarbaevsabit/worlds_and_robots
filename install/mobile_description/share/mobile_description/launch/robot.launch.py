from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, TimerAction
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg_share = FindPackageShare('mobile_description')
    urdf_file = PathJoinSubstitution([pkg_share, 'urdf', 'robot_v1.urdf'])

    # Аргументы позы спавна
    x_pose = LaunchConfiguration('x_pose', default='0.0')
    y_pose = LaunchConfiguration('y_pose', default='-2.0')
    z_pose = LaunchConfiguration('z_pose', default='1.0')
    roll  = LaunchConfiguration('roll',  default='0.0')
    pitch = LaunchConfiguration('pitch', default='0.0')
    yaw   = LaunchConfiguration('yaw',   default='0.0')

    # robot_state_publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': Command(['cat ', urdf_file])
        }]
    )

    # Мосты ROS ↔ Gazebo (используем полные gz-типы)
    bridges = ExecuteProcess(
        cmd=['ros2', 'run', 'ros_gz_bridge', 'parameter_bridge',
             '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
             '/lidar@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan',
             '/camera/image_raw@sensor_msgs/msg/Image@gz.msgs.Image',
        ],
        output='screen'
    )

    # Спавн робота
    spawn_robot = ExecuteProcess(
        cmd=['ros2', 'run', 'ros_gz_sim', 'create',
             '-world', 'car_world',
             '-topic', '/robot_description',
             '-name', 'vehicle_blue',
             '-x', x_pose,
             '-y', y_pose,
             '-z', z_pose,
             '-R', roll,
             '-P', pitch,
             '-Y', yaw],
        output='screen'
    )

    spawn_delayed = TimerAction(
        period=2.0,
        actions=[spawn_robot]
    )

    return LaunchDescription([
        DeclareLaunchArgument('x_pose', default_value='0.0'),
        DeclareLaunchArgument('y_pose', default_value='-2.0'),
        DeclareLaunchArgument('z_pose', default_value='1.0'),
        DeclareLaunchArgument('roll',   default_value='0.0'),
        DeclareLaunchArgument('pitch',  default_value='0.0'),
        DeclareLaunchArgument('yaw',    default_value='0.0'),
        robot_state_publisher,
        bridges,
        spawn_delayed,
    ])