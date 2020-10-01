# Python learning - A simple racing game using Turtle module in python 
# Source tutorial - https://codeclubprojects.org/en-GB/python/turtle-race/

# importing turtle module for graphics, randint for random numbers
from turtle import *
from random import randint

# speed of drawing
speed(20)
# taking the starting point to top-left without drawing
penup()
goto(-140,140)

# drawing race track with 16 vertical lines
for step in range(16):
  # line no
  write(step, align='center')
  # turn right and forward with space
  right(90)
  forward(10)
  # start drawing with pendown
  pendown()
  # vertical line with dash and stroke of equal lenghts 
  for dash in range(0,150,10):
    if (dash%20) == 0:
      forward(10)
      penup()
    else:
      forward(10)
      pendown()
  # penup and go back to start of vertical line, turn and go forward for next vertical line
  penup()
  backward(160)
  left(90)
  forward(20)

# turtle one
ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160,100)
ada.pendown()
ada.right(360)

# turtle two
bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160,70)
bob.pendown()
bob.right(360)

# turtle three
tim = Turtle()
tim.color('green')
tim.shape('turtle')

tim.penup()
tim.goto(-160,40)
tim.pendown()
tim.right(360)

# turtle four
sid = Turtle()
sid.color('turquoise')
sid.shape('turtle')

sid.penup()
sid.goto(-160,10)
sid.pendown()
sid.left(360)

# moving each turtle forward with random length
for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  tim.forward(randint(1,5))
  sid.forward(randint(1,5))
