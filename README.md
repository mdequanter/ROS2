# ROS2
Ros2 code

This repository contains code for developing in ROS2


<h2>subscribeRos2.py</h2>
Subscribing to a topic.  In this case /turtle1/pose and showing the content on a screen logger

<h2>publishRos2.py</h2>
Making a basic movement with a turtle to show how you can publish a topic.
In this case cmd_vel topic is published so the turtle makes a linear and angular movement.

<h2>showTopicsRos2.py</h2>
Showing topics that are currently active.

<h2>publishAndSubscribeRos2.py</h2>
In this script a publish to /turtle1/cmd_vel is performed. 
At the same time  the code is looking for the X or Y position of the turtle.
When X or Y is more then 10, the scripts stops before the turtle hits the wall

<img src="https://user-images.githubusercontent.com/74420584/186103890-ded878c3-1665-47c7-a4a5-a1e0e26fd2ba.png" width=100>
