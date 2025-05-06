from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep

def init_magnet():
    """Initialize the magnets list with the GPIO pins numbers of the magnet(s) and return the actuation time (user input).
    return: magnets: list of int GPIO pin number(s) of the magnet(s)
            t_on: int actuation time of the magnet(s)
    """ 

    magnets = []
    t_on = 0
    #t_off = 0

    n = int(input("How many GPIO are used for magnet element(s)? : "))
    if n == 0:
        return([] , 0)
    else:
        for i in range(n):
            magnets.append(int(input("Enter the GPIO BCM pin number :")))
        
        t_on = int(input("How long magnet on [s] ?"))

    return(magnets, t_on)


def setup_magnet(magnets):
    """Set the pins present in the magnets list as outputs.
    Arg:    magnets = list of int GPIO pin number(s) of the magnet(s)
    """

    for m in magnets:
        GPIO.setup(m, GPIO.OUT)                         #setup([pin], [GPIO.IN, GPIO.OUT]), configuring GPIO pins in output mode
    return()


def activate_m(magnets, time_on):
     """Actuation of the electromagnet(s) for a given time
    Args:   magnets: list of int GPIO pin number(s) of the magnet(s)
            time_on: int rest time on  actuation time of the magnet(s)
    """
     
     print("Magnet(s) on for", time_on, "sec")
     GPIO.output(magnets, GPIO.HIGH)                    #GPIO.output([pin][GPIO.HIGH]), digital output, set pin p high, GPIO.HIGH will drive it to 3.3V, equivalent GPIO.HIGH = True = 1
     sleep(time_on)
     
     print("Magnet(s) off")
     GPIO.output(magnets, GPIO.LOW)                     #GPIO.output([pin][GPIO.LOW]), digital output, set pin p low, GPIO.LOW will drive it to 0V, equivalent GPIO.LOW = Fase = 0





 