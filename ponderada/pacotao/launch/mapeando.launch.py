from launch import LaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription,RegisterEventHandler,ExecuteProcess,LogInfo
from ament_index_python.packages import get_package_share_directory
import os
from launch.event_handlers import OnProcessExit

def generate_launch_description():

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
        get_package_share_directory('turtlebot3_gazebo'), 'launch'),
        '/turtlebot3_world.launch.py'])
    )

    mapear = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
        get_package_share_directory('turtlebot3_cartographer'), 'launch'),
        '/cartographer.launch.py']),
        launch_arguments={'use_sim_time': 'True'}.items(),
    )
    
    teleop = Node(
        package="turtlebot3_teleop",
        executable="teleop_keyboard",
        output="screen",
        prefix="xterm -e"
    )

    #ros2 run nav2_map_server map_saver_cli -f ./my_map
    salvando_mapa = RegisterEventHandler(
            OnProcessExit(
            target_action=teleop,
            on_exit=[
                LogInfo(msg=(' fechando turtlebot')),
                ExecuteProcess(
                cmd=["ros2", "run", "nav2_map_server", "map_saver_cli", "-f", "./my_map"],
                output='screen'
            )

        ]
    )
)    


    return LaunchDescription([
        teleop,
        gazebo,
        mapear,
        salvando_mapa   
    ])

