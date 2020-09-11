#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:45:47 2020

@author: hannahimhoff
"""

#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
hideturtle()

speed(10)

up()
goto(-200,-200)
down()

color("white")
dot(120)
up()
goto(-200,-140)
down()

dot(80)

up()
goto(-200,-95)
down()

dot(40)

up()
goto(-15,90)
down()
color("blue")
circle(25)

up()
goto(10,90)
down()

goto(40,93)
down()
circle(25)

up()
goto(0,0)
down()

color("lightgreen")
width(4)
forward(150)

up()
goto(100,-150)
color([100,0,100])
down()

polygon = range(5)

begin_fill()

for element in polygon:
    forward(50)
    left(72)
    
end_fill()
