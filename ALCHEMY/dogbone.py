import functions.function_display as display
import functions.function_UV as uv
import functions.function_photosensor as sensor
# import functions.function_motor as motor
import functions.function_vibration as vibration
import functions.function_motor2 as motor2
import functions.function_resin as selection
# from gpiozero import LED
from time import sleep
import tkinter as tk 
from screeninfo import get_monitors
import sys
# from time import time
from tqdm import tqdm
import questionary
import os
import signal

################################################################################################################################
### Clean up gpio pins when interupting



# Global list to keep track of all gpiod lines/motors/etc
# registered_cleanup = [2,3,4,5,6,7,8,9,10, 11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
def cleanup_all(signum=None, frame=None):
    print("\nCleaning up GPIO and exiting...")
    try:
        # Release all registered hardware
        # for item in registered_cleanup:
        #     try:
        #         if hasattr(item, 'release'):
        #             item.release()
        #         elif hasattr(item, 'close'):
        #             item.close()
        #     except Exception as e:
        #         print(f"Cleanup error: {e}")
        # Additional manual cleanups
        uv.switch_off(uv_pin)
        motor2.motor_release(1)
        motor2.motor_release(2)
    except Exception as e:
        print(f"Exception during cleanup: {e}")
    finally:
        try:
            root.destroy()
        except:
            pass
        sys.exit(0)

# Attach signal handlers at the top of your script
signal.signal(signal.SIGINT, cleanup_all)
signal.signal(signal.SIGTERM, cleanup_all)

################################################################################################################################
### Object properties 
# print("Object properties")
origin_path = "/home/alchemy/PRINT/"
origin_path_layers="/home/alchemy/LAYERS/" 
file_name=selection.file_def(origin_path)
# file_name=input("Name of the folder containing images (Need to be stored in PRINTS)")
base_path=origin_path + file_name                                                                       #Folder path   
black_image_path = "/home/alchemy/black_image.png"                                                      #Black image path

sequence = sorted(os.listdir(base_path), key=lambda x: int(x.split('.')[0]))
sequence= [os.path.join(base_path,name) for name in sequence]
nb_layers = len([f for f in os.listdir(base_path) if os.path.isfile(os.path.join(base_path, f))])       
layers_state_path = f"/home/alchemy/LAYERS/{file_name}.txt"                                             #file containing the layer's state of the print
try:
    with open(layers_state_path, "r") as f:
        # Read all lines from the file and strip any extra whitespace or newlines
        layers_state_values = [int(line.strip()) for line in f.readlines()]
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# Control that the numbre of layers are matching
if nb_layers!=len(layers_state_values):
    print(f"number of layer not consistent: {nb_layers} in print and {len(layers_state_values)} in layer definition")
    sys.exit("error")
else :
    pass


################################################################################################################################

### Selection of resin properties
exp_time, exp_time_first=selection.resin_selection()
attract_time =300                                                                                # steady magnet time in seconds
vibration_time=450                                                                               # vibration time in seconds

################################################################################################################################### 
### Initialization of printing parameters
SOP = questionary.select(
"Settigns: ",
choices=["Standard Operation", "custom settings"]).ask()


if SOP=="Standard Operation": 
    # layer_thickness=0.10
    layer_index=0                                                                                           #Determines the current layer
    Particles_state=1 
    l_container=72
    
    motors=[]
    time_on=300
    vibration.setup_vibration(motors)
    uv_pin = 27
    sensor_pin=4
else:
    # Layer thickness definition
    # layer_thickness=(input("layer thickness in mm (ENTER for default value (0.20))"))
    # if not layer_thickness:
    #     layer_thickness=0.20
    # else :
    #     layer_thickness=float(layer_thickness)
    layer_index=0                                                                                           #Determines the current layer
    Particles_state=1                                                                                       #Determines if the particles are dispersed or not (initial state : dispersed particle) 

    ################################################################################################################################ 
    ### Initialisation of the hardware components (GPIO pins assignation)

    #Motor magnets 
    l_container=(input("size of resin container in mm (ENTER for default value (72))"))
    if not l_container:
        l_container=72
    else:
        l_container=float(l_container)
    # while True:
    response = input("rotate lead screw to place Magnet and press ENTER").strip().lower()
    print("Magnets setting success")

    # Dispersion elements - vibration motors
    motors, time_on=vibration.init_vibration()
    vibration.setup_vibration(motors)
    print("Vibration motors setup success")


    #UV ligth
    uv_pin = uv.init_uv()
    print("UV light setup success")

    #Photoelctric sensor
    sensor_pin = sensor.init_sensor()                                                                                                                                                                                                                #le setup GPIO qui va faire fonctionner le sensor est présente dans la fontion start_position_1(sensor_pin)
    print("photo sensor setup success")


###################################################################################################################################
#GUI creation with TkInter 
# for m in get_monitors():
#     print("INFO", str(m))

monitors = get_monitors()
monitor=display.name_selection('HDMI-2')                                                                # port for the LCD screen
x_shift = monitor.x
y_shift = monitor.y
w_root = monitor.width
h_root = monitor.height
###################################################################################################################################


################################################################################################################################
### Layer thickness definition for fine tuning
thickness=questionary.select(
"Select layer thickness",
choices=["0.08 mm", "0.10 mm", "0.16 mm", "0.20 mm"]).ask()
layer_thickness=float(thickness[:4])

composite_printing=questionary.select(
"Composite resin",
choices=["Pure Resin", "Composite Resin"]).ask()
if composite_printing=="Pure Resin":
    motors=[]
else:
    motors=[5, 13, 17, 25]
    vibration.setup_vibration(motors)
## Initialization and zero position of the printing bed
response = questionary.select(
"Build head calibrated?",
choices=["Yes", "No"]).ask()
if response == "Yes":
    motor2.start_position_1(sensor_pin)
    Z_table_pos=0
else:
    print("setting")
    motor2.start_position_1(sensor_pin)                                                               # go down to the screen
    Z_table_pos=0
    input("After settting: Press Enter to continue...")

################################################################################################################################


root = tk.Tk()                                                                                          #Tinker window creation
root.attributes('-fullscreen', True)
root.geometry(f"{w_root}x{h_root}+{x_shift}+{y_shift}")                                                 #Create a root with width=w_root, heigth=h_root, shifted by x_shift from the left and y_shift from the top of the monitor

cnv = tk.Canvas(root, bg="black", highlightthickness=0)
cnv.pack(fill=tk.BOTH, expand=True)


################################################################################################################################
###Conversion of the images paths to Image Objects
black_image_tk  = display.convert_full_0(black_image_path, w_root, h_root, monitors)                    #Convert black image path to black image object, with full screen dimensions                                         
image_paths = display.convert_list(base_path, nb_layers)

################################################################################################################################
### MAIN PRINTING
## Start MAIN 
progress_bar = tqdm(total=nb_layers, desc="PRINT", bar_format='{desc}: {percentage:3.0f}% |{bar}| {n_fmt}/{total_fmt}', position=0,leave=True)

for j in range(nb_layers):                                                            #  loop over the image objects 
    images_tk=display.convert_full_1(sequence[j:j+1], w_root, h_root, monitors)            # possible to switch to convert_full_0 by changing indices
    progress_bar.update(1)
    
    motor2.move_dist_time_dir_dm(6,1, 1,1)
    # motor2.move_dist_time_dir_dm(60,5, 1,1)
    sleep(2)
    if composite_printing=="Composite Resin"and Particles_state==1:
        vibration.activate_v(motors, 120)   
    else:
        pass
    motor2.move_dist_time_dir_dm(6-layer_thickness,1,-1,1)
    # motor2.move_dist_time_dir_dm(60,5, -1,1)
    sleep(2)
    Z_table_pos+=layer_thickness
    layer_index+=1
    
    display.show_image(cnv, w_root, h_root, black_image_tk)
    root.update_idletasks()
    root.update()

    ##  PARTICLES ACTUATION IN THE CONTAINER      
    if layer_index<=3:
        cure_time =exp_time 
    else:
        cure_time=exp_time_first 

    ##  PARTICLES ACTUATION IN THE VAT
    ##  Consider state of particles and compare to instructions
    try:
        if layers_state_values[layer_index] != Particles_state:
            motor2.move_dist_time_dir_dm(32, 8, 1, 1)

            if Particles_state==1:
                Particles_state=0
                motor2.move_dist_time_dir_dm((210/2-l_container/2), 10,1,2)                                #Move to the side of the resin container
                sleep(1)
                motor2.move_dist_time_dir_dm(l_container, attract_time,1, 2)                              #ove to the other side of the resin container
            else:
                motor2.move_dist_time_dir_dm(l_container/2,30,-1,2)
                sleep(1)    
                motor2.move_dist_time_dir_dm((210/2-l_container/2), 10,-1,2)
                sleep(1)
                vibration.activate_v(motors, vibration_time)
                Particles_state=1
            # input("press enter to continue") 
        
            motor2.move_dist_time_dir_dm(32, 8, -1, 1)   
        else:
            pass
    except:
        pass

    # vibration.activate_v(motors, 20)
    uv.switch_on(uv_pin)
    display.show_image(cnv, w_root, h_root, images_tk[0])
    root.update_idletasks()
    root.update()
    for i in tqdm(range(100), desc="UV-Light", bar_format='{desc}: {percentage:3.0f}% |{bar}|', position=1, leave=False):        
        sleep(cure_time/100)
    uv.switch_off(uv_pin)
    sleep(2)


    if i == len(images_tk)-1:
        display.show_image(cnv, w_root, h_root, black_image_tk)        
        root.update_idletasks()
        root.update()
        # print("End of the printing")
        root.bind('<Escape>', lambda e: root.quit())   
    else:
        pass

motor2.move_dist_time_dir_dm(60,30,1,1)

motor2.motor_release(1)
motor2.motor_release(2)
print("\n PRINTED")
################################################################################################################################









