'''
In this script a publish to /turtle1/cmd_vel is performed. 
At the same time  the code is looking for the X or Y position of the turtle.
When X or Y is more then 10, the scripts stops before the turtle hits the wall

author : Maarten Dequanter
'''



import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose



import datetime



class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher2')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

        self.subscription = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.handle_turtle_pose,
            10)
        self.subscription  # prevent unused variable warning



    def timer_callback(self):
        move_cmd = Twist()
        move_cmd.linear.x = 0.5 + (self.i*0.1)
        move_cmd.angular.z = 1.0
        self.publisher_.publish(move_cmd)
        self.get_logger().info('Publishing twist')
        self.i += 1


    def handle_turtle_pose(self, msg):
        
        if (msg.x > 10 or msg.y > 10):
            self.get_logger().info("Stop before hitting the wall")
            rclpy.shutdown()





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