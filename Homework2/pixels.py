'''
These are some operations you can perform on a PNG image using Python.
'''
from PIL import Image

im = Image.open("t-rex.png")
pix = im.load()
row, col = im.size

r, g, b = pix[10, 10]		# RGB values of 10X10th pixel.
print(r)			# Red value
print(g)			# Green value
print(b)			# Blue value

pix[10, 10] = (0, 0, 0)		# Replacing RGB with 0's, so the color is black.
pix[20, 20] = (0, 0, 0)
pix[30, 30] = (0, 0, 0)

im.save("new-t-rex.png")	# Writing updated image (with black pixel) into a new image.