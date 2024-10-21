# Non-Truncated Version
rm print/*
magick convert whispering-woods-75ppi.png -colorspace RGB -crop 750x600 +repage -gravity northwest -background white -extent 750x600 +adjoin print/whispering-woods-75ppi-%02d.png

# Truncated version
rm print_trunc/*
magick convert whispering-woods-75ppi.png -colorspace RGB -crop 2850x2400+0+75 +repage -crop 750x600 +repage -gravity northwest -background white -extent 750x600 +adjoin print_trunc/whispering-woods-75ppi-%02d.png
