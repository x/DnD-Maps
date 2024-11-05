"""A script for cropping surrounding whitspace in an image.

Usage:
    pip install pillow
    python crop_whitespace.py input_image.png output_image.png
"""
from PIL import Image, ImageChops
import sys
import os


def crop_whitespace(input_path, output_path):
    try:
        # Open the input image
        image = Image.open(input_path).convert("RGB")

        # Create a background that is solid white
        bg = Image.new(image.mode, image.size, (255, 255, 255))

        # Calculate the difference between image and white background
        diff = ImageChops.difference(image, bg)

        # Get the bounding box of the non-white content
        bbox = diff.getbbox()

        if bbox:
            # Crop to the bounding box
            cropped_image = image.crop(bbox)
            cropped_image.save(output_path)
            print(f"Image saved to {output_path}")
        else:
            print("No content detected. Image is all whitespace.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python crop_whitespace.py <input_image_path> <output_image_path>")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]

    # Check if the input file exists
    if not os.path.exists(input_image_path):
        print(f"Error: The file '{input_image_path}' does not exist.")
        sys.exit(1)

    # Run the cropping function
    crop_whitespace(input_image_path, output_image_path)
