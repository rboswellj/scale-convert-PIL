#!/usr/bin/env python3

'''
1. Open directory path
2. get all files in the directory
3. for each file:
    a. resize from 192x192 to 128x128
    b. rotate 90 degrees clockwise
    c. save as jpg to new directory /opt/icons/
'''

import os
from PIL import Image

def process_image(input_path, file, output_path):
    try:
        with Image.open(input_path + file) as img:
            # Rotate image 90 degrees clockwise
            img = img.rotate(-90)
            # Save the image as jpg
            img = img.convert("RGB")
            # Resize image to 128x128
            img = img.resize((128, 128))
            if file.endswith('.tiff') or file.endswith('.tif'):
                file = file[:-4] + '.jpeg'
            else:
                file += '.jpeg'
            img.save(output_path + file, 'JPEG')
            output_test(output_path, file)
    except Exception as e:
        print(f"Error processing {file}: {e}")

def process_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(str(input_dir)):
        process_image(input_dir, filename, output_dir)

def output_test(path, file):
    try:
        with Image.open(path + file) as img:
            print(f"{file} output: {img.format}: {img.size}")
    except Exception as e:
        print(f"Error displaying {file}: {e}")

def main():

    input_dir = './images/'  # Change to your input directory
    output_dir = './opt/icons/'  # Change to your desired output directory

    process_directory(input_dir, output_dir)
            
if __name__ == "__main__":
    main()