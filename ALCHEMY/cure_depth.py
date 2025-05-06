import functions.function_UV as uv
from time import sleep
import tkinter as tk 
import functions.function_display as display
from time import sleep
import tkinter as tk 
from screeninfo import get_monitors
time_test=float(input("time tested"))
monitors = get_monitors()
monitor = display.name_selection('HDMI-2')
x_shift = monitor.x
y_shift = monitor.y
w_root = monitor.width
h_root = monitor.height
root = tk.Tk()                                                                  #Tinker window creation
root.attributes('-fullscreen', True)
root.geometry(f"{w_root}x{h_root}+{x_shift}+{y_shift}")                         #Create a root with width=w_root, heigth=h_root, shifted by x_shift from the left and y_shift from the top of the monitor
cnv = tk.Canvas(root, bg="black", highlightthickness=0)
cnv.pack(fill=tk.BOTH, expand=True)

# time_test=float(input("time tested"))
# black_image_tk  = display.convert_full_0("/home/alchemy/square.png", w_root, h_root, monitors)
black_image_tk  = display.convert_full_0("/home/alchemy/square.png", w_root, h_root, monitors)


uv_pin = 27


uv.switch_on(uv_pin)
display.show_image(cnv, w_root, h_root, black_image_tk)
root.update_idletasks()
root.update()
sleep(time_test)
uv.switch_off(uv_pin)
print("end of test")
