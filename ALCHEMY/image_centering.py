import os
import numpy as np
from PIL import Image

def find_barycenter(image):
    """Find the barycenter of white pixels in the image."""
    data = np.array(image)
    white_pixels = np.argwhere(data == 255)  # Find all white pixels
    if white_pixels.size == 0:
        raise ValueError("No white pixels found in the image.")
    barycenter = np.round(np.mean(white_pixels, axis=0)).astype(int)
    return barycenter

def shift_image(image, x_shift, y_shift):
    """Shift the image by the given amounts."""
    data = np.array(image)
    shifted_data = np.zeros_like(data)
    height, width = data.shape
    for y in range(height):
        for x in range(width):
            new_x = x + x_shift
            new_y = y + y_shift
            if 0 <= new_x < width and 0 <= new_y < height:
                shifted_data[new_y, new_x] = data[y, x]
    return Image.fromarray(shifted_data)

def main():
    folder = input("Enter the folder containing the images: ").strip()
    images = [f for f in os.listdir(folder) if f.endswith(".png")]
    
    if not images:
        print("No PNG images found in the folder.")
        return

    for idx, img_name in enumerate(images):
        print(f"{idx}: {img_name}")
    
    reference_index = int(input("Enter the index of the reference image: ").strip())
    reference_image_path = os.path.join(folder, images[reference_index])
    
    ref_image = Image.open(reference_image_path).convert("L")  # Convert to grayscale
    ref_barycenter = find_barycenter(ref_image)

    # Calculate the center of the image
    width, height = ref_image.size
    center = np.array([height // 2, width // 2])

    # Calculate shifts
    y_shift, x_shift = center - ref_barycenter

    # Apply the shift to all images
    for img_name in images:
        img_path = os.path.join(folder, img_name)
        image = Image.open(img_path).convert("L")
        shifted_image = shift_image(image, x_shift, y_shift)

        # Save the shifted image
        output_path = os.path.join(folder, f"{img_name[:-4]}.png")
        shifted_image.save(output_path)
        print(f"Shifted image saved as {output_path}")

    print("All images have been processed and saved.")

if __name__ == "__main__":
    main()
