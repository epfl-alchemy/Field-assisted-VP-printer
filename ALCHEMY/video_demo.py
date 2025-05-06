import functions.function_vibration as vibration
from time import sleep
import functions.function_motor2 as motor2


l_container=74
attract_time=300
motor2.move_dist_time_dir_dm((210/2-l_container/2), 10,1,2)                                #Move to the side of the resin container
sleep(0.5)
motor2.move_dist_time_dir_dm(l_container, attract_time,1, 2)
sleep(5)
motor2.move_dist_time_dir_dm(l_container, 20,-1, 2)     
sleep(0.5)
motor2.move_dist_time_dir_dm((210/2-l_container/2), 20,-1,2)                                #Move to the side of the resin container



motors=[5,13,17,25]
time_on=600
vibration.setup_vibration(motors)     
vibration.activate_v(motors, time_on)
