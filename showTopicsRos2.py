### `sample_to_show_topic_list.py` ###
import rclpy
from rclpy.node import Node

def get_topic_list():
    node_dummy = Node("_ros2cli_dummy_to_show_topic_list")
    topic_list = node_dummy.get_topic_names_and_types()
    node_dummy.destroy_node()
    return topic_list


rclpy.init()
topic_list = get_topic_list()
for info in topic_list:
    print(info[0])
rclpy.shutdown()

