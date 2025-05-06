# Below imports all neccessary packages to make this Python Script run
import time
import board
from adafruit_motor import stepper #removed for some reasons
from adafruit_motorkit import MotorKit
import functions.function_motor as motor
import functions.function_photosensor as sensor
from time import sleep
import functions.function_motor2 as motor2

# Below initialises the variable kit to be our I2C Connected Adafruit Motor HAT
kit = MotorKit(i2c=board.I2C())




# If you uncomment below it will start by de-energising the Stepper Motor,
# Worth noting the final state the stepper motor is in is what will continue.
# Energised Stepper Motors get HOT over time along with the electronic silicon drivers

# kit.stepper1.release()

# The below loop will run 500 times. Each loop it will move one step, clockwise, then pause for 0.01 seconds
# This will almost look like a smooth rotation.

# print("Motor 3 running")
# kit.motor2.throttle=1
# sleep(5)
# kit.motor2.throttle=0

# print("Motor 1 running slowly up")
# motor.move_dist_time_dir_released_1(80,80, 1)
# sleep(3)
# print("Motor 1 running slowly down")
# motor.move_dist_time_dir_released_1(80,80, 1)

# print("SLOWER")

# print("Motor 1 running slowly up")
# motor.move_dist_time_dir_released_1(80,160, 1)
# sleep(3)
# print("Motor 1 running slowly down")
# motor.move_dist_time_dir_released_1(80,160, 1)


print("Forward SINGLE")


# motor.move_dist_dir_1(80,1)
# sleep(5)
# motor.move_dist_dir_2(8,-1)
# sleep(2)
# motor.move_dist_dir_2(8,1)
# sleep(2)
# motor.move_dist_dir_2(8,-1)









# for i in range(1000):
#     kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)          

# l_container=72
# attract_time=20
# motor.move_dist_dir_2((210/2+l_container/2),1)                                          #Move to the other size of the resin container
# sleep(attract_time)                                                                     #Time to slepp to gather particlesto side
# temp_position=0
# while temp_position<l_container:                                                        #Back and forth movement to gather most of the particles with the magnet
#     motor.move_dist_dir_2(9,-1)
#     sleep(attract_time)
#     motor.move_dist_dir_2(3,1)
#     sleep(attract_time)
#     temp_position+=6







# print("ending 1")
# kit.stepper2.release()
# Moteur 1 running
# print("motor 1 running")
# kit.motor1.throttle=1.0
# sleep(6)
# kit.motor1.throttle=0

#  Motor 2 running 
# print("motor 2 runnning")
# kit.motor2.throttle=1.0
# sleep(6)
# kit.motor2.throttle=0

# Motors running
# kit.motor1.throttle=1.0
# kit.motor2.throttle=1.0
# sleep(6)
# kit.motor1.throttle=0
# kit.motor2.throttle=0

##### COMMENTE PARCE QUE PROBLEMES HAT

# print("moving motor 1 and 20mm ")
# motor.move_dist_dir_1(80, 1)
# motor.move_dist_dir_2(8, -1)



# for i in range(200):
#     kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
# sleep(2)
# print("backwards")
# for j in range(500):
#     kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
# motor.move_dist_time_dir_1(20, 5, -1)
# sleep(3)
# motor.move_dist_time_dir_1(200, 10, -1)

# print("rotor function")
# motor.rotor_no_mvt_1(1, 2, 1)
# print("faster backwards") 
# motor.rotor_no_mvt_1(10, 2, -1)
# print("stop")
      
# sleep(3)



# sensor_pin = sensor.init_sensor()
# print(sensor_pin)
# motor.start_position_1(sensor_pin)
# sleep(2)
# motor.move_dist_dir_1(64,1)
# motor.move_dist_dir_1(24,-1)

# print("moving motor 2 and testing functions")
# motor.move_dist_time_dir_2(20, 10, 1)
# print("back wards")
# motor.move_dist_time_dir_2(200, 10, -1)

# print("rotor function")
# motor.rotor_no_mvt_2(1, 20, 1)
# print("faster")
# motor.rotor_no_mvt_2(10, 20, -1)



# The below loop will run 500 times. Each loop it will move two step, Clockwise, then pause for 0.01 seconds
# This will almost look like a smooth rotation.

# for i in range(500):
#     print("Forward DOUBLE")
#     kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
#     time.sleep(0.01)  


# The below line will de-energise the Stepper Motor so it can freely move
kit.stepper2.release()
kit.stepper1.release()