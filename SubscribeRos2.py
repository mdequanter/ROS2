import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from turtlesim.msg import Pose


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('turtle1')
        self.subscription = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.handle_turtle_pose,
            10)
        self.subscription  # prevent unused variable warning


    def handle_turtle_pose(self, msg):
        self.get_logger().info('"x: %s"' % msg.x)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()