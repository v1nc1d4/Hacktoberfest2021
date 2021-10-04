#Method One Kinda Big
#!/usr/bin/python3
from cv2 import imread,imwrite
import numpy as np
#pip3 install numpy
from base64 import urlsafe_b64encode
from hashlib import md5
from cryptography.fernet import Fernet
from custom_exceptions import *


#Returns binary  of a string
def str2bin(string):
    return ''.join((bin(ord(i))[2:]).zfill(7) for i in string)

#Returns text  for a  binary string
def bin2str(string):
    return ''.join(chr(int(string[i:i+7],2)) for i in range(len(string))[::7])

#Returns the encrypted/decrypted form of string depending upon mode inputs !
def encrypt_decrypt(string,password,mode='enc'):
    _hash = md5(password.encode()).hexdigest()
    cipher_key = urlsafe_b64encode(_hash.encode())
    cipher = Fernet(cipher_key)
    if mode == 'enc':
        return cipher.encrypt(string.encode()).decode()
    else:
        return cipher.decrypt(string.encode()).decode()


#Encodes secret data in image
#lsb steg technique
def encode(input_filepath,text,output_filepath,password=None,progressBar=None):
    if password != None:
        data = encrypt_decrypt(text,password,'enc') #If password is provided, encrypt the data with given password
    else:
        data = text
    data_length = bin(len(data))[2:].zfill(32)
    bin_data = iter(data_length + str2bin(data))
    img = imread(input_filepath,1)
    if img is None:
        raise FileError("The image file '{}' is inaccessible".format(input_filepath))
    height,width = img.shape[0],img.shape[1]
    encoding_capacity = height*width*3
    total_bits = 32+len(data)*7
    if total_bits > encoding_capacity:
        raise DataError("The data size is too big to fit in this image!")
    completed = False
    modified_bits = 0
    progress = 0
    progress_fraction = 1/total_bits
        
    for i in range(height):
        for j in range(width):
            pixel = img[i,j]
            for k in range(3):
                try:
                    x = next(bin_data)
                except StopIteration:
                    completed = True
                    break
                if x == '0' and pixel[k]%2==1:
                    pixel[k] -= 1
                    modified_bits += 1
                elif x=='1' and pixel[k]%2==0:
                    pixel[k] += 1
                    modified_bits += 1
                if progressBar != None: #If progress bar object is passed
                    progress += progress_fraction
                    progressBar.setValue(progress*100)
            if completed:
                break
        if completed:
            break

    written = imwrite(output_filepath,img)
    if not written:
        raise FileError("Failed to write image '{}'".format(output_filepath))
    loss_percentage = (modified_bits/encoding_capacity)*100
    return loss_percentage

#Extracts secret data from input image
#Deconding Part 
def decode(input_filepath,password=None,progressBar=None):
    result,extracted_bits,completed,number_of_bits = '',0,False,None
    img = imread(input_filepath)
    if img is None:
        raise FileError("The image file '{}' is inaccessible".format(input_filepath))
    height,width = img.shape[0],img.shape[1]
    for i in range(height):
        for j in range(width):
            for k in img[i,j]:
                result += str(k%2)
                extracted_bits += 1
                if progressBar != None and number_of_bits != None: #If progress bar object is passed
                    progressBar.setValue(100*(extracted_bits/number_of_bits))
                if extracted_bits == 32 and number_of_bits == None: #If the first 32 bits are extracted, it is our data size. Now extract the original data
                    number_of_bits = int(result,2)*7
                    result = ''
                    extracted_bits = 0
                elif extracted_bits == number_of_bits:
                    completed = True
                    break
            if completed:
                break
        if completed:
            break
    if password == None:
        return bin2str(result)
    else:
        try:
            return encrypt_decrypt(bin2str(result),password,'dec')
        except:
            raise PasswordError("Invalid password!")

if __name__ == "__main__":

    ch = int(input('What do you want to do Now ?\n\n1.Encrypt\n2.Decrypt\n\nInput(1/2): '))
    if ch == 1:
        ip_file = input('\nEnter cover image name(path)(note:with extension): ')
        text = input('Enter secret data to hide inside a image: ')
        pwd = input('Enter password to encrypt: ')
        op_file = input('Enter output image name(path)(with extension): ')
        try:
            loss = encode(ip_file,text,op_file,pwd)
        except FileError as fe:
            print("Error: {}".format(fe))
        except DataError as de:
            print("Error: {}".format(de))
        else:
            print('Encoded Successfully!\nImage Data Loss = {:.5f}%'.format(loss))
    elif ch == 2:
        ip_file = input('Enter image path: ')
        pwd = input('Enter password: ')
        try:
            data = decode(ip_file,pwd)
        except FileError as fe:
            print("Error: {}".format(fe))
        except PasswordError as pe:
            print('Error: {}'.format(pe))
        else:
            print('Decrypted data:',data)
    else:
        print('Wrong Choice try Again !')




    
