# Based on: https://www.raspberrypi.org/forums/viewtopic.php?t=242928\.
# Route 3.3 VDC to the controller "+" input for each: ENA, PUL, and DIR
#
from time import sleep
import gpiod
from time import sleep
import time
from time import monotonic

#
PUL = 17  # Stepper Drive Pulses
DIR = 27  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
ENA = 22  # Controller Enable Bit (High to Enable / LOW to Disable).
# DIRI = 14  # Status Indicator LED - Direction
# ENAI = 15  # Status indicator LED - Controller Enable
#
# NOTE: Leave DIR and ENA disconnected, and the controller WILL drive the motor in Default direction if PUL is applied.
# 
## MOTOR1 (Z-table)
def move_dist_time_dir_dm(distance, temps, sens, ID):
    
    if ID==1:
        PUL = 22  # Stepper Drive Pulses
        DIR = 23  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
        ENA = 24 
    else:
        PUL=21
        DIR=20
        ENA=26
    
    chip=gpiod.Chip("gpiochip0")
    linePUL=chip.get_line(PUL)
    linePUL.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
    lineDIR=chip.get_line(DIR)
    lineDIR.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
    lineENA=chip.get_line(ENA)
    lineENA.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
    
    # stepfactor=2
    step_num = round(distance/8*400)
    
    sleep_time = temps/step_num       #temps d'attente entre chaque step (diviser par deux car haut puis bas)
    
    on=1
    off=0
    if sens > 0:
        # start_time = monotonic()
        lineENA.set_value(on)
        sleep(0.1)
        lineDIR.set_value(0)
        sleep(0.1)
        for i in range(step_num):
            linePUL.set_value(1)
            sleep(sleep_time/2)
            linePUL.set_value(0)
            sleep(sleep_time/2)
        # lineENA.set_value(off)

    else :
        # start_time = monotonic()
        lineENA.set_value(on)
        sleep(0.1)
        lineDIR.set_value(1)
        sleep(0.1)
        for i in range(step_num):
            linePUL.set_value(1)
            sleep(sleep_time/2)
            linePUL.set_value(0)
            sleep(sleep_time/2)
        # lineENA.set_value(off)
    return




################################################################################################################################################################################



def start_position_1(sensor_pin):
    """Move the building platform downward, to the starting position (until the photosensor is not reached) by activating the stepper motor in the backrward direction
    Args : GPIO pin number of the photosensor."""
    
    # print("Stepper motor goes to start position")
    chip=gpiod.Chip("gpiochip0")
    line=chip.get_line(sensor_pin)
    line.request(consumer="sensor",type=gpiod.LINE_REQ_DIR_IN)
    linePUL=chip.get_line(22)
    linePUL.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
    lineDIR=chip.get_line(23)
    lineDIR.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
    lineENA=chip.get_line(24)
    lineENA.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
    lineENA.set_value(1)
    sleep(0.1)
    lineDIR.set_value(1)
    sleep(0.1)
    while line.get_value() == 1:
        linePUL.set_value(1)
        sleep(1/400)
        linePUL.set_value(0)
        sleep(1/400)        
    
    
      
    
    
    
def motor_release(ID):
    off=0
    if ID==1:
        PUL = 22  # Stepper Drive Pulses
        DIR = 23  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
        ENA = 24 
    else:
        PUL=21
        DIR=20
        ENA=26  
    chip=gpiod.Chip("gpiochip0")
    lineENA=chip.get_line(ENA)
    lineENA.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)        
        