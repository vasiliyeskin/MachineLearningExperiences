from PIL import Image, ImageDraw
import numpy as np

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

draw = ImageDraw.Draw(img)
greyscale_image = img.convert('L')
imgCopy = img.copy()
imgCopy.show()

width = img.size[0]
height = img.size[1]

obj = img.load()
obj = img.load()

obj2 = np.ones((width, height), dtype=int)
# obj[:, :][0] = obj[:, :][0] + obj2[:, :]


greyscale_image.save('greyscale_image.jpg')
# greyscale_image.show()

increas = -50
for i in range(width):
    for j in range(height):
        a = obj[i, j][0] + increas * obj2[i, j]
        b = obj[i, j][1] + increas * obj2[i, j]
        c = obj[i, j][2] + increas * obj2[i, j]
        draw.point((i, j), (a, b, c))

img.show()

obj3 = obj2 + obj2
obj2 = obj3 * obj3
obj4 = 6 * np.ones((width, height), dtype=int)
obj5 = obj2 * obj4
print(obj5)
print(obj5[:, 0].size)
print(obj5[0, :].size)








