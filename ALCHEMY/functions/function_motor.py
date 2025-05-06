import board
# import RPi.GPIO as GPIO
from time import sleep
from time import monotonic
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit
import gpiod
from time import time

################################################################################################################################
## Steup I2C communiaciton + base movement
kit = MotorKit(i2c=board.I2C())             #initialises the variable kit to be our I2C Connected Adafruit Motor HAT

def move_up(step_nb):
    """Move the building platform upward by activating the stepper motor in the forward direction
    Args : number of motor rotation step."""

    print("Forward for ", step_nb ,"double steps")

    for i in range(step_nb):
        kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        # sleep(0.01)      
    kit.stepper2.release()                  #de-energise the Stepper Motor so it can freely move
################################################################################################################################   
    
    
################################################################################################################################
## MOTOR1 (Z-table)
def move_dist_time_dir_1(distance, temps, sens):
    """Move the building platform
    Args : distance in mm, time in seconds, direction in integer (1: forward, -1: backward)"""
    
    # print(f"Stepper motor moves by {distance}mm in {temps}s, in direction {sens}")
    step_num = round(distance/8*360/1.8)
    sleep_time = temps/step_num
    if sens > 0:
        start_time = monotonic()
        for i in range(step_num):
            kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
                    # Wait for the delay without blocking other processes
            while monotonic() - start_time < sleep_time:
                pass
            start_time=monotonic()
    else :
        start_time = monotonic()
        for i in range(step_num):
            kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
            while monotonic() - start_time < sleep_time:
                pass
            start_time=monotonic()
            
def rotor_no_mvt_1(vitesse, temps, sens): 
    """Moves the motor 1 at a defined speed (build platform motor)
    Args : vitesse in rpm, temps in seconds, direction in integer (1: forward, -1: backward)"""
    
    # print(f"Stepper motor moves at speed {vitesse}rpm during {temps}s, in direction {sens}")
    n_steps_tot=round(vitesse*360/1.8*temps)
    sleep_time=temps/n_steps_tot
    if sens > 0:
        for i in range(n_steps_tot):
            kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
            sleep(sleep_time) 
    else :
        for i in range(n_steps_tot):
            kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
            sleep(sleep_time)
    kit.stepper1.release()

def move_dist_dir_1(distance, sens): #moteur 1 ou 2, distance en mm, temps en secondes, sens en entier positif ou negatif
    """Move the building platform (motor 1)
    Args : distance in mm, sens as integer (1: forward, -1: backward)"""
    start_time=time()
    delta_1=0
    # print(f"Stepper motor moves by {distance}mm, in direction {sens}")
    step_num = round(2*distance*200/8)
    if sens > 0:
        for i in range(step_num):
            start_1=time()
            kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
            end_1=time()
            if abs(delta_1- (end_1-start_1))>0.0005 and i!=0:
                print("sth wrong")
            else:
                pass      
            delta_1=end_1-start_1
    else :
        for i in range(step_num):
            start_1=time()
            kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
            # sleep(0.02)
            end_1=time()
            if abs(delta_1- (end_1-start_1))>0.0005 and i!=0:
                print("sth wrong")
            else:
                pass      
            delta_1=end_1-start_1
            
    kit.stepper1.release()
    end_time=time()
    print(f"Time to reach the position : {end_time-start_time}s")                               #used as control of the stepper motor movement and code performance


def move_dist_time_dir_released_1(distance, temps, sens): #moteur 1 ou 2, distance en mm, temps en secondes, sens en entier positif ou negatif
    """Move the building platform (motor 1) speed is defined and motor released between each step
    Args : distance in mm, temps in seconds, sens in integer (1: forward, -1: backward)"""
    
    # print(f"Stepper motor moves by {distance}mm in {temps}s, in direction {sens}")
    step_num = round(distance/8*360/1.8)
    sleep_time = temps/step_num
    if sens > 0:
        start_time = monotonic()
        for i in range(step_num):
            kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
            kit.stepper1.release()
                    # Wait for the delay without blocking other processes
            while monotonic() - start_time < sleep_time:
                pass
            start_time=monotonic()
    else :
        start_time = monotonic()
        for i in range(step_num):
            kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
            kit.stepper1.release()
            while monotonic() - start_time < sleep_time:
                pass
            start_time=monotonic()
    kit.stepper1.release()


################################################################################################################################
## For MOTOR2 (magnets guide)    
def move_dist_time_dir_2(distance, temps, sens): #moteur 1 ou 2, distance en mm, temps en secondes, sens en entier positif ou negatif
    """Move the magnetic actuator (motor 2)
    Args : distance in mm, time in seconds, direction in integer (1: forward, -1: backward)"""
    
    # print(f"Stepper motor moves by {distance}mm in {temps}s, in direction {sens}")
    step_num = round(distance/8*360/1.8)
    sleep_time = temps/step_num
    if sens > 0:
        start_time = monotonic()
        for i in range(step_num):
            kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
            while monotonic() - start_time < sleep_time:
                pass
            start_time=monotonic()
    else :
        start_time = monotonic()
        for i in range(step_num):
            kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
            while monotonic() - start_time < sleep_time:
                pass
            start_time=monotonic()
    kit.stepper2.release()                                                  # Release the motor after the movement to free up the resources
    
##########################################################    Not used    
def rotor_no_mvt_2(vitesse, temps, sens): #vitesse en tours par minute, temps en secondes, sens entier positif
    """Moves the motor at a defined speed 
    Args : vitesse in rpm, temps in seconds, sens as integer (1: forward, -1: backward)"""
    
    # print(f"Stepper motor moves at speed {vitesse}rpm during {temps}s, in direction {sens}")
    n_steps_tot=round(vitesse*360/1.8*temps)
    sleep_time=temps/n_steps_tot
    if sens > 0:
        for i in range(n_steps_tot):
            kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
            sleep(sleep_time) 
    else :
        for i in range(n_steps_tot):
            kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
            sleep(sleep_time) 
    kit.stepper2.release()
##########################################################      
          
          
            
def move_dist_dir_2(distance, sens): #moteur 1 ou 2, distance en mm, temps en secondes, sens en entier positif ou negatif
    """Move the magnetic actuator (motor 2)
    Args : distance in mm, direction in integer (1: forward, -1: backward)"""
    start_time=time()
    delta_1=0
    step_num = round(2*distance*200/8)
    if sens > 0:
        for i in range(step_num):
            start_1=time()
            kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
            end_1=time()
            if abs(delta_1- (end_1-start_1))>0.0005 and i!=0:
                print("something wrong happened")
            else:
                pass      
            delta_1=end_1-start_1
    else :
        for i in range(step_num):
            start_1=time()
            kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
            end_1=time()
            if abs(delta_1- (end_1-start_1))>0.0005 and i!=0:
                print("something wrong happened")
            else:
                pass      
            delta_1=end_1-start_1
            
    kit.stepper1.release()
    end_time=time()
    print(f"Time to reach the position : {end_time-start_time}s")                               #used as control of the stepper motor movement and code performance

    
    
## SET initial position 
def start_position_1(sensor_pin):
    """Move the building platform downward, to the starting position (until the photosensor is not reached) by activating the stepper motor in the backrward direction
    Args : GPIO pin number of the photosensor."""
    
    print("Stepper motor goes to start position")
    chip=gpiod.Chip("gpiochip0")
    line=chip.get_line(sensor_pin)
    line.request(consumer="sensor",type=gpiod.LINE_REQ_DIR_IN)
    while line.get_value() == 1:
         kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    kit.stepper1.release()                      #de-energise the Stepper Motor so it can freely move
    print("Start position reached")




def move_dist_time_dir_released_2(distance, temps, sens): #moteur 1 ou 2, distance en mm, temps en secondes, sens en entier positif ou negatif
    """Move the magnetic actuator (motor 2) at a defined speed and motor released between each step
    Args : distance in mm, time in seconds, direction in integer (1: forward, -1: backward)"""
    
    # print(f"Stepper motor moves by {distance}mm in {temps}s, in direction {sens}")
    motor_stepsize = 200  #in mm/step (8 steps per revolution)
    step_num = round(distance/8*360/1.8)
    sleep_time = temps/step_num * motor_stepsize
    id_step=0
    if sens > 0:
        start_time = monotonic()
        for i in range(0,step_num,motor_stepsize):
            for j in range(motor_stepsize):
                id_step+=1
                kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
                # kit.stepper2.release()
                # while monotonic() - start_time < sleep_time:
                #     pass
                # start_time=monotonic()
                if id_step==step_num:
                    break
                else:
                    pass   
            if id_step==step_num:
                break
            else:
                pass
            kit.stepper2.release()
            sleep(sleep_time)
            
    else :
        start_time = monotonic()
        for i in range(0,step_num, motor_stepsize):
            for j in range(motor_stepsize):
                id_step+=1
                kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
                kit.stepper2.release()
                while monotonic() - start_time < sleep_time:
                    pass
                start_time=monotonic()
                if id_step==step_num:
                    break
                else:
                    pass   
            if id_step==step_num:
                break
            else:
                pass
            kit.stepper2.release()
            sleep(sleep_time)
    kit.stepper2.release()





def move_dist_dir_pause_2(distance, sens, pause_time=5, step_condition=100): #moteur 1 ou 2, distance en mm, temps en secondes, sens en entier positif ou negatif
    """Move the magnetic actuator (motor 2) at a defined speed and motor paused between for some time between each group of steps
    Args : distance in mm, time in seconds, pause_time in s, step_condition as integer, direction in integer (1: forward, -1: backward)"""
    
    # print(f"Stepper motor moves by {distance}mm, in direction {sens}")
    step_num = round(distance*200/8)
    # step_condition=100
    if sens > 0:
        for i in range(step_num):
            kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
            if i%step_condition==0:
                sleep(pause_time)
            else:
                pass
    else :
        for i in range(step_num):
            kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
            if i%step_condition==0:
                sleep(pause_time)
            else:
                pass
    kit.stepper2.release()
    




"""
#TEST MOTOR
#uncomment the code below to test the photosensor

# The below loop will run 500 times. Each loop it will move one step, clockwise, then pause for 0.01 seconds
# This will almost look like a smooth rotation.

for i in range(500):
    
    print("Forward DOUBLE")
    kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
    sleep(0.01) 


sleep(2) 


# The below loop will run 1000 times. Each loop it will move two step, anti-Clockwise, then pause for 0.01 seconds
# This will almost look like a smooth rotation.

for i in range(500):

    print("Backward DOUBLE")
    kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    sleep(0.01) 

"""