#!/usr/bin/env python3

# Imports
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

def callback(joydata):
    joyLX = joydata.axes[0]
    joyLY = joydata.axes[1]
    joyRX = joydata.axes[3]
    #joyRY = joydata.axes[4]
    
    angular_speed = 0.85*joyLX           
    linear_speed = 0.4*joyLY
        
    print("L: {} A: {}\n".format(linear_speed, angular_speed))
    print("RX: {}\n".format(joyRX))

    twist = Twist()
    twist.angular.z = angular_speed
    twist.linear.x = linear_speed
    pub_1.publish(twist)

    stepper = joyRX*128
    pub_2.publish(stepper)

if __name__ == "__main__":
    rospy.init_node('joy_listener', anonymous=True)

    global pub_1, pub_2
    pub_1 = rospy.Publisher('/cmd_vel', Twist, queue_size=10) 
    pub_2 = rospy.Publisher('/servo', Float64 , queue_size=10)
    sub = rospy.Subscriber('/joy', Joy, callback)
    
    rospy.spin()
