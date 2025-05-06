from PIL import Image

# Specify the dimensions of the binary image (e.g., 1920x1080)
width, height = 3840, 2400

# Create a new binary (mode '1') black image
binary_black_image = Image.new("1", (width, height), 1)  # 0 represents black

# Save the binary image to a file
binary_black_image.save("/home/alchemy/white_image.png")
print("Binary black image saved as 'black_image.png'")

