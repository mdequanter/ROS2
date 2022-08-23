import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist


import datetime



class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher2')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        move_cmd = Twist()
        move_cmd.linear.x = 0.5 + (self.i*0.1)
        move_cmd.angular.z = 1.0
        self.publisher_.publish(move_cmd)
        self.get_logger().info('Publishing twist')
        self.i += 1
        if (self.i > 1000) :
            exit()



def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()