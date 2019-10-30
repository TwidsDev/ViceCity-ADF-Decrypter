#!/usr/bin/python3
import os

Directory = os.getcwd()

for filename in os.listdir(Directory):
    if filename.endswith(".adf"):
        print("Decrypting " + filename)
        new_file = filename.replace('.adf','.mp3')
        b = bytearray(open(filename, 'rb').read())
        xord = bytearray()
        for i in range(len(b)):
            b[i] ^= 0b100010
        open(new_file, 'wb').write(b)
    else:
        print("Couldn't find ADF files, please ensure they're in a folder called Encrypted")
