from PIL import Image

width, height =1920, 1080
square_size = 100
image=Image.new('L', (width, height), color=255)
pixels = image.load()
for y in range(0,height, square_size):
    for x in range(0, width, square_size):
        if (x//square_size + y//square_size) % 2 == 0:
            for i in range(square_size):
                for j in range(square_size):
                    if x+i < width and y+j < height:
                        pixels[x+i, y+j] = 0
image.save(f"/home/alchemy/Pictures/damier{square_size}.png")
image.show()