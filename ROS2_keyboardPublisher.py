'''
A small program that based on keyboard input in ROS2 publishes messages on topic cmd_vel 
Author: Maarten Dequanter
'''


import threading
import rclpy
import os

from geometry_msgs.msg import Twist


NODE_NAME = "simple_publisher"


def handle_keyboard(publisher):
    while True:

        print('\n- Simple Publisher Menu -')
        print('   z: move forward')
        print('   w: move backward')
        print('   q: move left')
        print('   d: move right')

        print('   99. Exit')

        menu = input('Input the menu: ')

        if menu == 'z':
            move_cmd = Twist()
            move_cmd.linear.x = 1.0
            move_cmd.linear.y = 0.0
            move_cmd.angular.z = 0.0
            publisher.publish(move_cmd)

            print("forward is published")

        elif menu == 'w':
            move_cmd = Twist()
            move_cmd.linear.x = -1.0
            move_cmd.linear.y = 0.0
            move_cmd.angular.z = 0.0
            publisher.publish(move_cmd)            
            print("back is published")

        elif menu == 'q':
            move_cmd = Twist()
            move_cmd.linear.x = 0.0
            move_cmd.linear.y = 1.0
            move_cmd.angular.z = 0.0
            publisher.publish(move_cmd)            
            print("left is published")

        elif menu == 'd':
            move_cmd = Twist()
            move_cmd.linear.x = 0.0
            move_cmd.linear.y = -1.0
            move_cmd.angular.z = 0.0
            publisher.publish(move_cmd)            
            print("right is published")


        elif menu == '99':
            rclpy.shutdown()
            os._exit(1)


def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node(NODE_NAME)

    publisher = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)

 
    th = threading.Thread(target=handle_keyboard, args=(publisher,))
    th.start()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
