/*
 * rosserial Servo Control Example
 *
 * This sketch demonstrates the control of hobby R/C servos
 * using ROS and the arduiono
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

int val = 0;

//--------------------------------------------------------

#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif


#include <Servo.h> 
#include <ros.h>
#include <std_msgs/Float64.h>

ros::NodeHandle  nh;

Servo servo;


void servo_cb( const std_msgs::Float64& cmd_msg){
  //servo.write(cmd_msg.data); //set servo angle, should be from 0-180  
  //val = Serial.parseInt();
  stepper.step(cmd_msg.data);
  Serial.println(cmd_msg.data); //for debugging
}


ros::Subscriber<std_msgs::Float64> sub("servo", servo_cb);

void setup(){
  //pinMode(13, OUTPUT);
  stepper.setSpeed(200);
  nh.initNode();
  nh.subscribe(sub);
  //servo.attach(9); //attach it to pin 9
}

void loop(){
  nh.spinOnce();
  //delay(1);
}
