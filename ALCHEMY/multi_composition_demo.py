from PIL import Image
import os

width, height =3840, 2400
square_size = 150
image=Image.new('L', (width, height), color=255)
pixels = image.load()
for y in range(0,height, square_size):
    for x in range(0, width, square_size):
        if (x//square_size + y//square_size) % 2 == 0:
            for i in range(square_size):
                for j in range(square_size):
                    if x+i < width and y+j < height:
                        pixels[x+i, y+j] = 0
# image.save(f"/home/alchemy/Pictures/damier{square_size}.png")
image.save(f"C:/Users/arnau/OneDrive/Desktop/damier{square_size}.png")
# image.show()


import numpy as np

# Load binary target image
target = Image.open("C:/Users/arnau/OneDrive/Desktop/9.png").convert("1")
mask = Image.open(f"C:/Users/arnau/OneDrive/Desktop/damier{square_size}.png").convert("1")

# Ensure sizes match
if mask.size != target.size:
    mask = mask.resize(target.size)

# Convert both to numpy arrays (bool type: True for white, False for black)
target_array = np.array(target, dtype=bool)
mask_array = np.array(mask, dtype=bool)

# Apply mask: keep target pixel only where mask is True (white)
masked_array = target_array & mask_array  # logical AND
masked_array2 = target_array & ~mask_array
recovered_image=masked_array | masked_array2
# Convert back to image (multiply by 255 to get 0 or 255)
masked_image = Image.fromarray(masked_array.astype(np.uint8) * 255).convert("1")
masked_image2 = Image.fromarray(masked_array2.astype(np.uint8) * 255).convert("1")
# recovered_image= Image.fromarray(recovered_image.astype(np.uint8) * 255).convert("1")

# Save and show result
# masked_image.show()
# masked_image2.show()
# recovered_image.show()

# Save 
desk_path="C:/Users/arnau/OneDrive/Desktop"
folder=f"dogbone{square_size} 0.1mm"
folder_path = os.path.join(desk_path, folder)
file_path=os.path.join(desk_path, f"{folder}.txt")
os.makedirs(folder_path, exist_ok=True)

for i in range(64):
    image_path = os.path.join(folder_path, f"{i+1}.png")
    if i%2==0:
        masked_image.save(image_path)
    else:
        masked_image2.save(image_path)
        
        
layer_state = [(i+1) % 2 for i in range(64)]
with open(file_path, "w") as file:
    file.write("\n".join(map(str, layer_state)))
