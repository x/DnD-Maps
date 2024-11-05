"""A script for adjusting the surrounding whitspace in an image so it becomes
8"x10" given some ppi for printing on a 8.5"x11" sheet of paper with margin.

Usage:
    pip install pillow
    python printer_whitespace.py input_image.png output_image.png 100
"""
from PIL import Image, ImageChops, ImageOps
import sys
import os


def add_whitespace(input_path, output_path, ppi=100):
    try:
        # Open and crop the image to remove surrounding whitespace
        image = Image.open(input_path).convert("RGB")

        # Remove surrounding whitespace
        bg = Image.new(image.mode, image.size, (255, 255, 255))
        diff = ImageChops.difference(image, bg)
        bbox = diff.getbbox()
        if bbox:
            image = image.crop(bbox)
        else:
            print("No content detected. Image is all whitespace.")
            return

        # Get current image size in pixels
        width, height = image.size

        # Convert target dimensions to pixels based on DPI
        target_800 = 800 * ppi // 100
        target_1000 = 1000 * ppi // 100

        # Calculate potential new dimensions ensuring divisibility
        options = [
            (
                width + (target_800 - width % target_800) % target_800,
                height + (target_1000 - height % target_1000) % target_1000,
            ),
            (
                width + (target_1000 - width % target_1000) % target_1000,
                height + (target_800 - height % target_800) % target_800,
            ),
        ]

        # Choose dimensions that result in the smallest area
        new_width, new_height = min(options, key=lambda x: x[0] * x[1])

        # Calculate padding required for each side
        pad_width = (new_width - width) if new_width > width else 0
        pad_height = (new_height - height) if new_height > height else 0
        padding = (
            pad_width // 2,
            pad_height // 2,
            pad_width - pad_width // 2,
            pad_height - pad_height // 2,
        )

        # Add padding and save the new image
        padded_image = ImageOps.expand(image, padding, fill=(255, 255, 255))

        # Rotate if needed
        width, height = padded_image.size
        if height % 1000 != 0:
            padded_image = padded_image.rotate(90, expand=True)

        padded_image.save(output_path)

        print(f"Image saved to {output_path} with dimensions {padded_image.size}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print(
            "Usage: python add_whitespace.py <input_image_path> <output_image_path> <ppi>"
        )
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]
    ppi = int(sys.argv[3])

    # Check if the input file exists
    if not os.path.exists(input_image_path):
        print(f"Error: The file '{input_image_path}' does not exist.")
        sys.exit(1)

    # Run the function
    add_whitespace(input_image_path, output_image_path, ppi)
