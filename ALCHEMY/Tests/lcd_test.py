import tkinter as tk 
import functions.function_display as display
from time import sleep
import tkinter as tk 
from screeninfo import get_monitors

monitors = get_monitors()
print(monitors)

# if len(monitors) > 1:   
#     for monitor in monitors:
#         if monitor.is_primary == False:
#             x_shift = monitor.x
#             y_shift = monitor.y
#             w_root = monitor.width
#             h_root = monitor.height
# else:
#     for monitor in monitors:
#         x_shift = monitor.x
#         y_shift = monitor.y
#         w_root = monitor.width
#         h_root = monitor.height
monitor = display.name_selection('HDMI-2')
print("monitor selected")
print(monitor)
x_shift = monitor.x
y_shift = monitor.y
w_root = monitor.width
h_root = monitor.height

root = tk.Tk()                                                                  #Tinker window creation
root.attributes('-fullscreen', True)
root.geometry(f"{w_root}x{h_root}+{x_shift}+{y_shift}")                         #Create a root with width=w_root, heigth=h_root, shifted by x_shift from the left and y_shift from the top of the monitor

cnv = tk.Canvas(root, bg="black", highlightthickness=0)
cnv.pack(fill=tk.BOTH, expand=True)

black_image_tk  = display.convert_full_0("/home/alchemy/PRINT/sample cube/1.png", w_root, h_root, monitors)


# black_image_tk  = display.convert_full_0("/home/alchemy/PRINT/sample cube/1.png", w_root, h_root, monitors)
image_other=display.convert_full_0("/home/alchemy/PRINT/sample cube/30.png", w_root, h_root, monitors)
for i in range(2):
    display.show_image(cnv, w_root, h_root, black_image_tk)
    root.update_idletasks()
    root.update()
    sleep(6)
    display.show_image(cnv, w_root, h_root, image_other)
    root.update_idletasks()
    root.update()
    sleep(6)


