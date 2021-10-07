from turtle import *

from os import system as cmd

bgcolor("#c2e0d4")
color("#009900")

speed(10)
penup()

left(180)
forward(150)
right(90)
forward(150)
down()


def sqr(leng):
    for i in range(4):
        right(90)
        forward(leng)
    

def sqrl(leng):
    for i in range(4):
        left(90)
        forward(leng)


def spa():
    right(90)
    forward(150)
  
          
def spal():
    left(90)
    forward(150)
    
def righ():
    begin_fill()
    sqr(50)
    spa()
    sqr(50)
    forward(100)
    sqr(50)
    forward(100)
    sqr(50)
    end_fill()

def lef():
    begin_fill()
    sqrl(50)
    spal()
    sqrl(50)
    forward(100)
    sqrl(50)
    forward(100)
    sqrl(50)
    end_fill()

def linel():
    forward(50)
    left(90)
    backward(50)

def liner():
    forward(50)
    right(90)
    backward(50)

sqr(400)
for i in range(4):
    righ()
    linel()
    lef()
    liner()
    
hideturtle()

cmd('sleep 10')