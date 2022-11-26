#!/usr/bin/env python3
# 2023.11.26 McMaster AutoPlow 
# Authors : Zachary Figueria https://www.linkedin.com/in/zachary-farrugia/  Yuxiang Guan https://www.linkedin.com/in/yuxiang-guan/

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

def callback(joyData):
    joy_Stick_Left_X_raw_value = joyData.axes[0]
    joy_Stick_Left_Y_raw_value = joyData.axes[1]
    joy_Stick_Right_X_raw_value = joyData.axes[3]
    #joyStickRightYvalue = joydata.axes[4]
    
    joy_stick_left_angular_speed = 0.85*joy_Stick_Left_X_raw_value           
    joy_stick_left_linear_speed = 0.4*joy_Stick_Left_Y_raw_value
        
    print("joy_stick_left_angular_speed: {} joy_stick_left_linear_speed: {}\n".format(joy_stick_left_linear_speed, joy_stick_left_angular_speed))
    print("stepper_motor_publisher: {}\n".format(joy_Stick_Right_X_raw_value))

    twist = Twist()
    twist.angular.z = joy_stick_left_angular_speed
    twist.linear.x = joy_stick_left_linear_speed
    robot_joystick_speedcontrol_publisher.publish(twist)

    #joy_Stick_Right_X_raw_value ranges from 0 to 1 
    #half revolution is 1024
    stepper_motor_publisher.publish(joy_Stick_Right_X_raw_value*128)

if __name__ == "__main__":
    rospy.init_node('joy_listener', anonymous=True)
    global pub_1, stepper_motor_publisher
    robot_joystick_speedcontrol_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10) 
    stepper_motor_publisher = rospy.Publisher('/stepper_velocity', Float64 , queue_size=10)
    sub = rospy.Subscriber('/joy', Joy, callback)
    rospy.spin()
