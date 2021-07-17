import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    """Generate launch description with multiple components."""
    container = ComposableNodeContainer(
        name='my_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            ComposableNode(
                package='rt2assignment_package',
                plugin='rt2assignment_package::MiniPublisher',
                name='talker'),
            ComposableNode(
                package='rt2assignment_package',
                plugin='rt2assignment_package::MiniSubscriber',
                name='listener'),
            ComposableNode(
                package='rt2assignment_package',
                plugin='rt2assignment_package::MiniServer',
                name='server'),
            ComposableNode(
                package='rt2assignment_package',
                plugin='rt2assignment_package::MiniClient',
                name='client')
            ],
            output='screen',
    )

    return launch.LaunchDescription([container])

