# import RPi.GPIO as GPIO
import gpiod
from time import sleep
import time

def init_piezo():
    """Initialize the piezo list with the GPIO pins numbers of the piezo element(s) and return the actuation time and the applied frequency (user input).
    return: piezo: list of int GPIO pin number(s) of the piezo element(s)
            t_on: int actuation time of the piezo element(s)
            freq: int of the frequency
    """          

    piezos = []
    t_on = 0
    freq = 0 

    n = int(input("How many GPIO are used for piezo element(s)? : "))
    if n == 0:
        return([], 0, None)
    else:
        for i in range(n):
            piezos.append(int(input("Enter the GPIO BCM pin number :")))
        t_on = int(input("How long transducers on [s] ?"))
        freq = int(input("At what frequency piezo elements work [Hz] ? :"))

        return(piezos, t_on, freq)


def setup_piezo(piezos):
    """Set the pins present in the pins list as outputs"""

    # for p in piezos:
    chip=gpiod.Chip("gpiochip0")
    line=chip.get_lines(piezos)
    line.request(consumer="piezo",type=gpiod.LINE_REQ_DIR_OUT)
    # line.set_values([1 for _ in range(len(piezos))])                                #line.set_value([value]), set the line to the given value, 0 for low, 1 for high
    
        # GPIO.setup(p, GPIO.OUT)                         #setup([pin], [GPIO.IN, GPIO.OUT]), configuring GPIO pins in output mode
    return()



def activate_p(piezos, time_on, freq):
    """Actuation of the piezo element(s) for a given time
       Args:   piezos: list of int GPIO pin number(s)
               time_on: int activation time
               freq: int frequency
    """ 

    piezos_pwm =[]
    period = 1.0/freq
    on_time = 0.5*period
    off_time=period-on_time


    chip=gpiod.Chip("gpiochip0")
    line=chip.get_lines(piezos)
    line.request(consumer="main",type=gpiod.LINE_REQ_DIR_OUT)
    # line.set_values([1 for _ in range(len(piezos))])                                #line.set_value([value]), set the line to the given value, 0 for low, 1 for high

    start_time = time.time()
    try:
        while time.time() - start_time < time_on:
            line.set_values([1 for _ in range(len(piezos))]) 
            sleep(on_time)
            line.set_values([0 for _ in range(len(piezos))])
            sleep(off_time)
    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        line.set_values([0 for _ in range(len(piezos))])  # line.set_value([value]), set the line to the given value, 0 for low, 1 for high
        line.release()
        chip.close()
        print("Piezo finished")



    # for p in piezos:
    #     #GPIO.setup(p, GPIO.OUT)                        #setup([pin], [GPIO.IN, GPIO.OUT]), configuring GPIO pins in output mode
    #     piezos_pwm.append(GPIO.PWM(p, freq))            #GPIO.PWM([pin][frequency]), analogue output, initialize PWM pin up with given frequency

    # for pwm in piezos_pwm:
    #     pwm.start(50)                                   #start([duty cycle]) set initil value / output to a 50% duty cycle

    # print("Tranducer(s) on for", time_on, "sec") 
    # GPIO.output(piezos, GPIO.HIGH)                      #GPIO.output([pin][GPIO.HIGH]), digital output, set pin p high, GPIO.HIGH will drive it to 3.3V, equivalent GPIO.HIGH = True = 1

    # sleep(time_on)

    # print("Transducer(s) off")
    # GPIO.output(piezos, GPIO.LOW)                       #GPIO.output([pin][GPIO.LOW]), digital output, set pin p low, GPIO.LOW will drive it to 0V, equivalent GPIO.LOW = Fase = 0

    # for pwm in piezos_pwm:
    #     pwm.stop()                                      #turn PWM on that pin off