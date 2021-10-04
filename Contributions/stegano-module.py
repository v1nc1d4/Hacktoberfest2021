#!/usr/bin/python3
#Encode
from stegano import lsbset
#pip3 install stegano

from stegano.lsbset import generators

flag="This is secret Message For hacktoberfest"
#make sure to have a image.png in a current directory
lets=lsbset.hide("./image.png",flag,generators.eratosthenes())

lets.save("steged.png")
#A new PNG file has been created

# Decode
f=open("steged.png","rb")

lsbset.reveal(f,generators.eratosthenes())
>>> 'This is secret Message For hacktoberfest'

## The secret has been revealed simply

