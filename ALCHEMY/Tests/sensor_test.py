import functions.function_photosensor as sensor



#import RPi.GPIO as GPIO
from time import sleep

import gpiod
import os
import random


sensor_pin = sensor.init_sensor()
print(sensor_pin)
#GPIO.setup(sensor_pin, GPIO.INPUT)
chip=gpiod.Chip("/dev/gpiochip0")
line=chip.get_line(sensor_pin)
line.request(consumer="sensor",type=gpiod.LINE_REQ_DIR_IN)


print("photo sensor setup succehqpiIPHBess")

while True: 
    #value=GPIO.input(sensor_pin)
    value=line.get_value()
    value==True 
    print(value)
    sleep(0.25)


