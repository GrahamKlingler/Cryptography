# steganography
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher, HuffmanCodes


class Steganography():

    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None

    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)
        print(image) # for debugging

        # calculate available bytes
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)
        # convert into binary
        if codec == 'binary':
            self.codec = Codec()
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            self.codec = HuffmanCodes()
        binary = self.codec.encode(message + self.delimiter)

        # check if possible to encode the message
        num_bytes = ceil(len(binary)//8) + 1
        if  num_bytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            print("Bytes to encode:", num_bytes)
            self.text = message
            self.binary = binary
            # iterate through bits and insert them into pixels
            for i in range(len(self.binary)):
                bit = int(self.binary[i])
                row_ct = image.shape[1]
                curr_pixel = image[i//(row_ct*3), i // 3 % row_ct]
                curr_pixel[i%3] = (curr_pixel[i%3] & 254) | bit
            # you may create an additional method that modifies the image array
            cv2.imwrite(fileout, image)

    def decode(self, filein, codec):
        flag = True
        image = cv2.imread(filein)
        print(image) # for debugging

        # convert into text
        if codec == 'binary':
            self.codec = Codec()  # delimiter = self.delimiter
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            if self.codec == None or self.codec.name != 'huffman':
                print("A Huffman tree is not set!")
                flag = False
        if flag:
            array = np.array(image)
            binary_data = ''
            max_bits = image.shape[0] * image.shape[1] * 3
            # iterate through pixels and decode
            for i in range(max_bits):
                row = image.shape[1]
                curr_pixel = image[i // (row * 3), i // 3 % row]
                binary_data += str(curr_pixel[i % 3] & 1)
            # update the data attributes:
            self.text = self.codec.decode(binary_data)
            self.binary = binary_data

    def print(self):
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)

    def show(self, filename):
        plt.imshow(mpimg.imread(filename))
        plt.show()
