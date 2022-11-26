/*
 * # 2023.11.26 McMaster AutoPlow  
 * Authors : Zachary Figueria https://www.linkedin.com/in/zachary-farrugia/  Yuxiang Guan https://www.linkedin.com/in/yuxiang-guan/
 * 
 * References:
 * 
 * For the full tutorial write up, visit
 * www.ros.org/wiki/rosserial_arduino_demos
 *
 * For more information on the Arduino Servo Library
 * Checkout :
 * http://www.arduino.cc/en/Reference/Servo
 */
 // Arduino stepper motor control code

#include <Stepper.h> // Include the header file

// change this to the number of steps on your motor
#define STEPS 32

// create an instance of the stepper class using the steps and pins
Stepper stepper(STEPS, 8, 10, 9, 11);

//--------------------------------------------------------

#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif


#include <ros.h>
#include <std_msgs/Float64.h>

ros::NodeHandle  nh;


void stepper_cb( const std_msgs::Float64& cmd_msg){
  stepper.step(cmd_msg.data);
  Serial.println(cmd_msg.data); //for debugging
}


ros::Subscriber<std_msgs::Float64> sub("stepper_velocity", stepper_cb);

void setup(){
  stepper.setSpeed(200);
  nh.initNode();
  nh.subscribe(sub);
}

void loop(){
  nh.spinOnce();
  delay(1);
}