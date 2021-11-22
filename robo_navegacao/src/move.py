#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def callback(msg):
    print(msg.ranges)

    print("\n\n\n")

def move():
    # Inicia o nó
    rospy.init_node('robot', anonymous=True)

    # Inicia a leitura do sensor
    laser = rospy.Subscriber('/laser_scan', LaserScan, callback)

    # Inicia a publicação de velocidade
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    
    # Configura mensagem de velocidade
    vel_msg = Twist()
    vel_msg.linear.x = 0.5 # Velocidade linear (m/s)
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0.2 # Velocidade angular (rad/s)
    
    r = rospy.Rate(1) #atualização a cada 1s
    i = 0
    while not rospy.is_shutdown() and i < 10:

        velocity_publisher.publish(vel_msg)

        r.sleep()

        i = i + 1

    vel_msg.linear.x = 0.0 # Velocidade linear (m/s)  
    vel_msg.angular.z = 0.0 # Velocidade angular (rad/s)
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
