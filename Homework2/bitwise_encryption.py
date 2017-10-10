#! /usr/bin/python
import sys
from random import randint

from PIL import Image

# Cody Stephenson
# CYEN406
# Assignment2 - the Magic of XOR
# resources used: Stack Overflow, and pixels.py as provided

##############################################################
def genRandom():
	return randint(0,255)
##############################################################
def gen_key():
	# generate random numbers, save to output file
	key = open(key_file, "w+")
	for y in range(1,col):
		for x in range(1,row):
			key.write(str(genRandom()) + "," + str(genRandom()) + "," + str(genRandom()) + "\n")
	key.close
##############################################################
def bitwise_enc():
	# open key
	key = open(key_file)
	# create a pixel object
	pix = im.load()
	x = 0
	y = 0
	writeImage = 0
	# seperating each operation to decrease complexity
	# by doing 1/3rd the required if checks on opType
	if (opType == "and"):
		# set bool high to write to new image
		writeImage = 1
		# read line by line
		for line in key.readlines():
			# grab the data from each line, use as list
			line_rows = line.split(',')
			r, g, b = pix[x, y]
			pix[x, y] = (int(line_rows[0]) & r, int(line_rows[1]) & g, int(line_rows[2]) & b )
			x = x + 1
			if (x == row - 1):
				x = 0
				y = y + 1
	elif (opType == "or"):
		# set bool high to write to new image
		writeImage = 1
		# read line by line
		for line in key.readlines():
			# grab the data from each line, use as list
			line_rows = line.split(',')
			r, g, b = pix[x, y]
			pix[x, y] = (int(line_rows[0]) | r, int(line_rows[1]) | g, int(line_rows[2]) | b )
			x = x + 1
			if (x == row - 1):
				x = 0
				y = y + 1
	elif (opType == "xor"):
		# set bool high to write to new image
		writeImage = 1
		# read line by line
		for line in key.readlines():
			# grab the data from each line, use as list
			line_rows = line.split(',')
			r, g, b = pix[x, y]
			pix[x, y] = (int(line_rows[0]) ^ r, int(line_rows[1]) ^ g, int(line_rows[2]) ^ b )
			x = x + 1
			if (x == row - 1):
				x = 0
				y = y + 1
	else:
		print("Incorrect usage: operation should be or, xor, OR and")
	# if no error, then write new image
	if (writeImage):
		im.save(output_image)
	# otherwise, error message is printed, so now exit
	else:
		exit()
##############################################################
# MAIN BEGINS HERE		
# if not 3 or 4 arguments, print usage	
if not ((len(sys.argv) ==  4) or (len(sys.argv) == 3)):
	print("Incorrect usage:")
	print("encrpyting: python bitwise_encryption xor t-rex.png")
	print("decrypting: python bitwise_encryption xor t-rex.png key_xor.txt")
	exit()

# and/or/xor variable
opType = sys.argv[1]
#input file's name
filename = sys.argv[2]

# create strings for the outputs
# ex: encrypted_or.png
output_image = "encrypted_" + opType + ".png"
# ex: key_and.txt
key_file = "key_" + opType + ".txt"
# this is incase we're decrypting, dont write to our input file
# ex: output_or.png
alt_output = "output_" + opType + ".png"

# if not xor | and | or, then error
if not ((opType == "or") or (opType == "and") or (opType == "xor")):
	print("Invalid input.")
	exit()
# open the image file
im = Image.open(filename)
# grab the height and width of the image
row, col = im.size

# if no key is given, generate one
if len(sys.argv) == 3:
	gen_key()
# otherwise, assign the key file and output image names
if len(sys.argv) == 4:
	# if we're "decrypting", then key file is given and change output file
	key_file = sys.argv[3]
	output_image = alt_output

bitwise_enc()