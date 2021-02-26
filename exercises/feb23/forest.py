#Author: Drew Rafferty
import turtle
import random

turtle.setup(575, 575)
pen = turtle.Turtle()
turtle.bgcolor("burlywood")
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

gridSize = int(turtle.numinput("Size", "Enter Size: ", 5, 1, 10))
widthPadding = turtle.window_width()/gridSize
width = widthPadding * .9
padding = widthPadding * .1

leafWidth = width * .5
appleWidth = leafWidth * .1
stumpWidth = width * .2
stumpHeight = width * .5

for row in range(gridSize):
    x = -turtle.window_width()/2 + leafWidth / 2
    y = -turtle.window_width()/2 + widthPadding * row + padding

    for col in range(gridSize):
        pen.up()
        pen.setpos(x + (leafWidth - stumpWidth)/2, y)
        pen.down()

        #stump
        pen.color("sienna")
        pen.begin_fill()

        for i in range(4):
            if i%2 == 0:
                pen.forward(stumpWidth)
            else:
                pen.forward(stumpHeight)
            pen.left(90)
        pen.end_fill()

        pen.color("forest green")
        pen.up()
        pen.setpos(x + leafWidth / 2, stumpHeight * .8)
        x += widthPadding
turtle.done()