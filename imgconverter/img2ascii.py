import argparse
from PIL import Image
import numpy as np
import os

# ASCII characters from darkest to lightest
ASCII_CHARS = "@%#*+=-:. "

def image_to_ascii(image_path='./imgconverter/cranberrymuffin.png', width=100):
    # Open the image
    img = Image.open(image_path)

    # Convert to grayscale
    img = img.convert("L")

    # Calculate new height to maintain aspect ratio
    aspect_ratio = img.height / img.width
    new_height = int(width * aspect_ratio * 0.55)  # Adjusting for font aspect ratio

    # Resize image
    img = img.resize((width, new_height))

    # Convert image pixels to ASCII characters
    pixels = np.array(img)
    ascii_art = "\r\n".join(
        "".join(ASCII_CHARS[pixel // 32] for pixel in row) for row in pixels
    )

    return ascii_art

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art")
    parser.add_argument("image_path", type=str, help="Path to the image file")
    parser.add_argument("--width", type=int, default=100, help="Width of the ASCII output")
    args = parser.parse_args()

    ascii_output = image_to_ascii(args.image_path, args.width)
    print(ascii_output)
