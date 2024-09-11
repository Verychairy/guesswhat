from PIL import Image
import numpy as np
import json

def extract_colors(image_path, grid_size):
    img = Image.open(image_path).convert('RGBA')
    img = img.resize((grid_size, grid_size))  # Resize to grid size
    img_array = np.array(img)

    # Flatten the array and get RGB values
    colors = [tuple(pixel[:3]) for row in img_array for pixel in row]
    return colors

def save_colors(colors, output_path):
    with open(output_path, 'w') as f:
        json.dump(colors, f)

if __name__ == '__main__':
    colors = extract_colors('/Users/junguijae/Desktop/Poetic System/Loop (2024)/catty3.jpg', 100)  # Adjust the path and grid size
    save_colors(colors, 'color_map.json')

