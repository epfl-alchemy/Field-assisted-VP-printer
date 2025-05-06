import functions.function_vibration as vibration
from time import sleep

motors, time_on = vibration.init_vibration()      
print(motors)             
vibration.setup_vibration(motors)     
print("Piezo setup succes") 

vibration.activate_v(motors, time_on)