import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askinteger

def add_layer(state):
    try:
        subset = askinteger("Subset", "Enter the number of layers for this state:", minvalue=1)
        if subset is None:
            return
        for _ in range(subset):
            layer_states.append(state)
        update_status()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def save_layers():
    file_name = file_name_entry.get().strip()
    if not file_name:
        messagebox.showerror("Error", "Please enter a valid file name.")
        return

    # Adjust the list if too many values
    if len(layer_states) > nb_layers:
        layer_states[:] = layer_states[:nb_layers]
    
    # Save to file
    try:
        # with open(f"/home/alchemy/LAYERS/{file_name}.txt", "w") as f:
        with open(f"C:/Users/arnau/OneDrive/Desktop/{file_name}.txt", "w") as f:
            f.write("\n".join(map(str, layer_states)))
        messagebox.showinfo("Success", f"Layers saved to {file_name}.txt")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving: {e}")

def set_nb_layers():
    global nb_layers
    try:
        nb_layers = askinteger("Number of Layers", "Enter the total number of layers:", minvalue=1)
        if nb_layers is None:
            return
        nb_layers_label.config(text=f"Total Layers: {nb_layers}")
        update_status()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def update_status():
    status_label.config(text=f"Layers Added: {len(layer_states)} / {nb_layers}")

# Initialize variables
nb_layers = 0
layer_states = []

# Create the GUI
root = tk.Tk()
root.title("Layer State Manager")

# Widgets
nb_layers_label = tk.Label(root, text="Total Layers: 0")
nb_layers_label.pack(pady=5)

status_label = tk.Label(root, text="Layers Added: 0 / 0")
status_label.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_particles_button = tk.Button(button_frame, text="Particles (1)", command=lambda: add_layer(1), width=15)
add_particles_button.grid(row=0, column=0, padx=5)

no_particles_button = tk.Button(button_frame, text="No Particles (0)", command=lambda: add_layer(0), width=15)
no_particles_button.grid(row=0, column=1, padx=5)

set_layers_button = tk.Button(root, text="Set Number of Layers", command=set_nb_layers, width=20)
set_layers_button.pack(pady=10)

file_name_label = tk.Label(root, text="File Name:")
file_name_label.pack(pady=5)

file_name_entry = tk.Entry(root, width=30)
file_name_entry.pack(pady=5)

save_button = tk.Button(root, text="Save Layers", command=save_layers, width=20)
save_button.pack(pady=10)

# Run the application
root.mainloop()

