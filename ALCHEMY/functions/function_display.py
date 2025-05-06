import tkinter as tk 
from PIL import Image, ImageTk
from screeninfo import get_monitors


def name_selection(target_name):
    """Gets a list of the available monitors and allows the user to select a monitor based on its name 
    Args:   target_name: string of the name of the monitor
    return: monitor: object of the selected monitor if found, None otherwise
    """    
    
    monitors =get_monitors()                                    # get all monitors
    for monitor in monitors:
        if monitor.name == target_name:                         # find the monitor with the given name
            return monitor                                      # return the monitor
    return None


def convert_list(folder_path, nb_slice):
    """Create a list of image paths from sliced png image 
    Args:   folder_path: string of the folder path
            nb_slice: int of the total number of png images in the folder
    return: list of image paths
    """

    paths = []
    for i in range(nb_slice):
        paths.append(folder_path + str(i) + ".png")          #create image path with the folder path and the image number for
        return paths



def convert_full_0 (image_path, w_root, h_root, monitors):
    """Upload a single image path and create ImageTk.PhotoImage object
    Args:   image_path: string of the image path
            w_root, h_root: int of the width and heigh of the monitor
            monitors: list of monitor
    return: image_tk: resized ImageTk.PhotoImage object of the single image
    """

    image = Image.open(image_path)                          #open image path

    w, h = image.size                                       #image dimensions
    factor_w = w_root / w
    factor_h = h_root / h
    factor = min(factor_w, factor_h)                        #factor to adapt image to full screen without distorting it
    # print(factor_h, "\n", factor_w)

    new_w = int(w*factor)
    if len(monitors) > 1: 
        new_h = int(int(h*factor)*3)                     #factor 3,15 to adapte image heigth to the LCD screen
    else:
        new_h = int(h*factor)

    image = image.resize((new_w, new_h))                    #resize image
    image_tk = ImageTk.PhotoImage(image)                    #create ImageTk.PhotoImage object

    return image_tk 



def convert_full_1(image_paths, w_root, h_root, monitors):
    """Upload list of image paths and create ImageTk.PhotoImage object of each argument
    Args:   image_path: list of string images paths
            w_root, h_root: int of the width and heigh of the monitor
            monitors: list of monitor
    return: images_tk: list of resized ImageTk.PhotoImage object
    """

    images_tk=[]     

    for path in image_paths:       
        image = Image.open(path)                            #open image path

        w, h = image.size                                   #image dimensions
        # print("init w " + str(w))
        # print("init h " + str(h))
        factor_w = w_root / w
        factor_h = h_root / h
        factor = min(factor_w, factor_h)                    #factor to adapt image to full screen without distorting it
        
        new_w = int(w*factor)
        if len(monitors) > 1: 
            new_h = int(int(h*factor)*3)                    #factor 3,15 to adapte image heigth to the LCD screen
        else:
            new_h = int(h*factor)
            
        # print("new w " + str(new_w))
        # print("new h " + str(new_h))

        image = image.resize((new_w, new_h))                #resize image
        image_tk = ImageTk.PhotoImage(image)                #create ImageTk.PhotoImage object
        images_tk.append(image_tk)                          #add ImageTk.PhotoImage object to the list
        
    return images_tk



def show_image(cnv, w_root, h_root, image_tk):
    """Create a Canvas widget and display a single image
    Args:   cnv: root
            w_root, h_root: int of the width and heigh of the monitor
            image_tk: ImageTk.PhotoImage objects
    """                     
    
    cnv.create_image((w_root/2), (h_root/2), anchor=tk.CENTER, image=image_tk) #displays the image on the screen