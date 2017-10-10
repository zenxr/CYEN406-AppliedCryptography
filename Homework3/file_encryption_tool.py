#! /usr/bin/python

# Cody Stephenson
# CYEN406
# Assignment3 - AES and SHA-256

import sys
from Crypto.Cipher import AES
import hashlib

# the block size for the cipher object; must be 16 bytes for AES
BLOCK_SIZE = 16
# pad at the end, so all blocks including the last one are 128 bit long
PAD_WITH = '#'

def parseArgs():
	if len(sys.argv) != 4:
		print("Incorrect usage:")
		print("   First argument : 'enc' or 'dec'")
		print("   Second argument : key of 16, 24, or 32 bytes")
		print("   Third argument : filename")
		exit()
	# if first argument isn't enc or dec	
	if not ((sys.argv[1] == "enc") or (sys.argv[1] == "dec")):
		print("Improper usage: First argument should be 'enc' or 'dec'")
		exit()
	# if length of key isn't 16, 24, or 32 throw error message	
	if not ((len(sys.argv[2]) == 16) or (len(sys.argv[2]) == 24) or (len(sys.argv[2]) == 32)):
		print("Improper usage: Second argument should be key of length 16, 24, or 32 bytes")

def pad(plaintext):
    return plaintext + (BLOCK_SIZE - len(plaintext) % BLOCK_SIZE) * PAD_WITH

# Encrypts 'plaintext' using 'cipher' object.
def encrypt(cipher, plaintext):
    return cipher.encrypt(pad(plaintext))

# Decrypts 'ciphertext' using 'cipher' object.
def decrypt(cipher, ciphertext):
    return  cipher.decrypt(ciphertext).rstrip(PAD_WITH)

def hash_sha256(data):
	return hashlib.sha256(data.encode('utf8')).hexdigest()

def determineOutputName(encOrDec, filename):
	parts = filename.rsplit('.', 1)
	if encOrDec == "enc":
		outputfile = "".join(parts[0] + "_enc." + parts[1])
	else:
		outputfile = "".join(parts[0] + "_dec." + parts[1])
	return outputfile	

def aes_func(encOrDec, key, filename):
	# 16-byte key. It can be 16, 20, or 32 bytes long.
	# Create a 'cipher' object using 'secret_key'
	cipher = AES.new(key)
	# open the file
	f = open(filename, 'rb')

	# determine the outputfile's name and open output file
	of = open(determineOutputName(encOrDec, filename), 'wb')

	# hash the key with sha256
	hashed_key = hash_sha256(key)

	# if encrypting, append the hashed key to the beginning of output file
	if (encOrDec) == "enc"
		of.write(hashed_key)
	# if decrypting, grab the key from the beginning of input file
	else:
		key_check =	f.read(len(hashed_key))
		if not (key_check == hashed_key):
			print("Invalid key!")
			exit()
	# read the file one block_size at a time
	fileBlock = f.read(BLOCK_SIZE)
	while len(fileBlock):
		if encOrDec == "enc":
			cipherBlock = encrypt(cipher, fileBlock)
		else:
			cipherBlock = decrypt(cipher, fileBlock)
		of.write(cipherBlock)
		f.read(BLOCK_SIZE)

parseArgs()
encOrDec = sys.argv[1]
key = sys.argv[2]
filename = sys.argv[3]
aes_func(encOrDec, key, filename)

f.close()
of.close()