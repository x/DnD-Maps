rm print/*

# Basement
magick convert wyrmrest-castle-fl0-80ppi.png -crop 640x800 +repage +adjoin print/wyrmrest-castle-fl0-80ppi-%02d.png

# Ground Floor
magick convert wyrmrest-castle-fl1-80ppi.png -crop 640x800 +repage +adjoin print/wyrmrest-castle-fl1-80ppi-%02d.png

# Top Floor
magick convert wyrmrest-castle-fl2-80ppi.png -crop 640x800 +repage +adjoin print/wyrmrest-castle-fl2-80ppi-%02d.png
