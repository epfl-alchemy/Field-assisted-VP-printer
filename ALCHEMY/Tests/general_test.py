# a=1
# b=True
# if a==b: 
#     print("Equal")

# import os
# path = "/home/alchemy/PRINT"
# liste= os.listdir(path)
# nb_layers = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
# print("nombre",nb_layers, liste)
# a=input("press enter")
# print(len(a))
# print(f"efef{a}ettete")
# import board
# from adafruit_motor import stepper
# from adafruit_motorkit import MotorKit
# import functions.function_motor as motor
# kit = MotorKit(i2c=board.I2C())

# import tkinter as tk
# print("success")
# from PIL import Image, ImageTk
# import cnv 
# image=Image.open("/home/alchemy/Pictures/Screenshots/code sensor phot.png")
# import numpy as np
# print(np.pi)

# import sys
# sys.path.append("/home/alchemy/ALCHEMY/alchemy/lib64/python3.12/site-packages")
# print(sys.path)

# w_root = 1920
# h_root = 1080

# cnv.create_image((w_root/2), (h_root/2), anchor=tk.CENTER, image=image)

# from time import sleep
# filename=input("valeu")
# from tkinter import messagebox
# a=[1,2,3,4,5]
# try:
#     with open(f"C:\\Users\\arnau\\OneDrive\\Desktop\\{filename}.txt", "w") as f:
#             f.write("\n".join(map(str, a)))
#     messagebox.showinfo("Success", "Layers saved to .txt")
# except Exception as e:
#     messagebox.showerror("Error", "An error occurred while saving: {e}")

# file_path = f"C:\\Users\\arnau\\OneDrive\\Desktop\\{filename}.txt"  # Use the correct path here


# try:
#     with open(file_path, "r") as f:
#         # Read all lines from the file and strip any extra whitespace or newlines
#         layer_states = [int(line.strip()) for line in f.readlines()]
# except Exception as e:
#     print(f"An error occurred while reading the file: {e}")


# # Example usage:


# print(layer_states)
import numpy as np


a=np.zeros(10)
val=2
for i in range(0,len(a), val):
    for j in range(val):
        print(i+j)
    

