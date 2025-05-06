# import RPi.GPIO as GPIO
import gpiod
from time import sleep
import time


def init_vibration():
    """Initialize the motor list with the GPIO pins numbers of the vibration element(s) and return the actuation time (user input).
    return: motor: list of int GPIO pin number(s) of the piezo element(s)
            t_on: int actuation time of the piezo element(s)
    """ 

    motors = []
    t_on = 0
    
    
    n = input("How many GPIO are used for vibration element(s)? : ")
    if not n:
        return(motors, t_on)
    else:
        for i in range(int(n)):
            motors.append(int(input("Enter the GPIO BCM pin number :")))

        t_on = int(input("How long motors on [s] ?"))

        return(motors, t_on)
    

def setup_vibration(motors):
    """Set the pins present in the pins list as outputs"""
    if motors==[]:
        return()
    else:
        # for p in piezos:
        chip=gpiod.Chip("gpiochip0")
        line=chip.get_lines(motors)
        line.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
        return()


def activate_v(motors, time_on):
    """Actuation of the piezo element(s) for a given time
       Args:   piezos: list of int GPIO pin number(s)
               time_on: int activation time
               freq: int frequency
    """ 
    if motors==[] or time_on==0  or time_on<0  or not motors:
        return()
    else:
        chip=gpiod.Chip("gpiochip0")
        line=chip.get_lines(motors)
        line.request(consumer="main",type=gpiod.LINE_REQ_DIR_OUT)
        # print("vibration start")
        line.set_values([1 for _ in range(len(motors))])
        sleep(time_on) 
        line.set_values([0 for _ in range(len(motors))])                          #line.set_value([value]), set the line to the given value, 0 for low, 1 for high
        # print("vibration end")
        return()












