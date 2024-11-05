#!/bin/bash

# Loop through each building-* folder
for building_dir in building-*/; do
    # Create a corresponding output directory
    output_dir="${building_dir%/}/print"
    mkdir -p "$output_dir"

    # Loop through each .png file in the building directory
    for file in "$building_dir"/*.png; do
        # Extract the base filename (without directory path)
        filename=$(basename "$file")
        # Construct the output path, replacing file extension with the sequence pattern
        output_file="$output_dir/${filename%.png}-%02d.png"

        # Perform the conversion
        magick "$file" -crop 1000x800 +repage +adjoin "$output_file"

        echo "Processed $file -> $output_file"
    done
done
