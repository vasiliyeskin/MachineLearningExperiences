from PIL import Image

resize_width = 300
infile = "ship.jpg"
outfile = "test.thumbnail.jpg"
img = Image.open(infile)
#img.show()

# The file format of the source file.
print(img.format) # Output: JPEG

# The pixel format used by the image. Typical values are “1”, “L”, “RGB”, or “CMYK.”
print(img.mode) # Output: RGB

# Image size, in pixels. The size is given as a 2-tuple (width, height).
print(img.size) # Output: (1200, 776)

# Colour palette table, if any.
print(img.palette) # Output: None.size) # Output: (1200, 776)

# Colour palette table, if any.
print(img.palette) # Output: None

wpercent = (resize_width/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((resize_width,hsize), Image.ANTIALIAS)
img.save(outfile)
img.save("test.png")
greyscale_image = img.convert('L')
imgCopy = img.copy()
imgCopy.show()

obj = greyscale_image.load()
obj[25,25] = 0
obj[25,26] = 0
obj[25,27] = 0
obj[25,28] = 0
obj[25,29] = 0
obj[25,30] = 0

greyscale_image.save('greyscale_image.jpg')
greyscale_image.show()
