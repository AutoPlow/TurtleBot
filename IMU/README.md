Sensor BNO055: https://www.amazon.ca/Adafruit-Absolute-Orientation-Fusion-Breakout/dp/B017PEIGIG/ref=sr_1_4?crid=HMPSW284ACFF&keywords=bno055&qid=1662742159&sprefix=BNO%2Caps%2C125&sr=8-4

Repo (installation guides & electrical wiring): https://github.com/RoboticArts/ros_imu_bno055

Commands

source ~/catkin_ws2/devel/setup.bash 

roslaunch ros_imu_bno055 imu.launch serial_port:=/dev/ttyUSB0 operation_mode:=NDOF_FMC_OFF use_magnetometer:=True 

roslaunch ros_imu_bno055 view_imu.launch serial_port:=/dev/ttyUSB0 operation_mode:=NDOF_FMC_OFF use_magnetometer:=True 

Result:
![Screenshot from 2022-09-18 20-54-07](https://user-images.githubusercontent.com/55643200/191790802-576d9124-adf3-4c10-9f56-fc66a94a1277.png)



Furthure integration:

imu_filter_madgwick 
https://github.com/CCNYRoboticsLab/imu_tools

Problems: the turtlebot (physical) publishes IMU to /imu
BNO055 pushed topics to /imu/magnetometer and /imu/data
imu_filter_madgwick listens to topics from /imu/mag


![image](https://user-images.githubusercontent.com/55643200/191800376-25ddc95d-58de-4c26-b556-72f183c39ff9.png)




