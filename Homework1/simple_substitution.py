#! /usr/bin/python
import sys

# Cody Stephenson
# CYEN406
# Assignment1 - key word and caesar ciphers


# parse input arguments
if len(sys.argv) != 5:
	print("Incorrect usage:")
	print("   First argument : 'c' or 'k' (caesar or key ciphers)")
	print("   Second argument : 'enc' or 'dec'")
	print("   Third argument : key of type int or a string")
	print("   Fourth argument : inputfile's name")
	print("\nExample: python simple_substitution k enc DANG example.txt")
	exit()
# inputfile's name
filename = sys.argv[4]
# "c" or "k" <- caesar or key
encType = sys.argv[1]
# enc or dec <- encrypt or decrypt
encOrDec = sys.argv[2]
# key value, either an int or a string
key = sys.argv[3]

# open the file provided from input
f = open(filename)

# caesar function
def caesar(key):
	# key will be used as an int
	key = int(key)
	# if encrypting, output is shifting chars left
	# else, output is shifting chars right
	if encOrDec == "enc":
		key = -1 * key
	# read the first character
	char = f.read(1)
	# while not EOF
	while char != "":
		# return the ascii value for the char
		val = ord(char)
		# if it is uppercase alphabetic
		if (val >= 65 and val <= 90) :
			# shift the character
			val = val + key
			# if outside of bounds, reset accordingly
			while val > 90:
				val = val - 26
			while val < 65:
				val = val + 26
			# convert value back to character
			char = chr(val)
		# write the character to output file
		output.write(char)
		# read a new character
		char = f.read(1)

# keyword cipher function
def keyword(key):
	# this alphabet string will be modified
	modAlph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	# strip the alphabet of the characters in our key
	modAlph = modAlph.translate(None,key)
	# concatenate the two strings
	modAlph = key + modAlph
	# read a character from input file
	char = f.read(1)
	# if encrypting
	if encOrDec == "enc":
		# while not EOF
		while char != "":
			# get the ascii value of the character
			val = ord(char)
			# if uppercase alphabetic
			if (val >= 65 and val <= 90):
				# A = 65, we want this value to be 0; so val-=65
				val = val - 65
				# find the character at the index of val
				char = modAlph[val]
			# write the character to output
			output.write(char)
			# read a new character
			char = f.read(1)
	# if decrypting		
	if encOrDec == "dec":
		# while not EOF
		while char != "":
			# find ascii value of the character
			val = ord(char)
			# if uppercase alphabetic
			if (val >= 65 and val <= 90):
				# char to write is (current char's index in modAlph + 65) in ascii
				char = chr(65 + modAlph.index(char))
			# write the character to our output file
			output.write(char)
			# read a new character
			char = f.read(1)

# open either a ciphertext or plaintext file
if encOrDec == "enc":
	output = open("ciphertext.txt", "w+")
else:
	output = open("plaintext.txt", "w+")

# determine which function to run
if (encType == 'c'):
	caesar(key)
else:
	keyword(key)

# close the files
f.close
output.close