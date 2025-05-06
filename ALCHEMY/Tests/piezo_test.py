
import functions.function_piezo as piezo
from time import sleep

piezos, p_time_on, frequency = piezo.init_piezo()      
print(piezos)             
piezo.setup_piezo(piezos)     
print("Piezo setup succes") 

piezo.activate_p(piezos, p_time_on,frequency)








