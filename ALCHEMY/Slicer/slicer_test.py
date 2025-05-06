import Slicer.slicer as slicer
file_path="C:\Users\arnau\OneDrive\Desktop\_sample Cube 15mm v3.pwc"
output_folder="C:\Users\arnau\OneDrive\Desktop\A"
print(output_folder)
slicer.extract_layers_from_pwc(file_path, output_folder)
