from launch import LaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    
    gazebo = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([os.path.join(
        get_package_share_directory('turtlebot3_gazebo'), 'launch'),
        '/turtlebot3_world.launch.py'])
        
    )

   
    # ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=<arquivo-do-mapa>.yaml
    mapa_salvo = ExecuteProcess(
        cmd=["ros2", "launch", "turtlebot3_navigation2", "navigation2.launch.py", "use_sim_time:=True", "map:=./my_map.yaml"],
        output="screen"
    )
    
     
    trajeto = Node(
            package='pacotao',
            executable='trajeto',
            output='screen',
          prefix = 'xterm -e',
        )
    
    delay = ExecuteProcess(
        cmd=["sleep", "5"],
        output="screen",
    )

    return LaunchDescription([
        gazebo,
        mapa_salvo,
        delay,
        trajeto
       
    ],)