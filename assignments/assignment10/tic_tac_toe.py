#Author: Drew Rafferty
import turtle
turtle.setup(600,600)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

size = 200
windowX = 600
windowY= 600

#messed up
def draw_grid():
    pen.up()
    pen.setpos(-windowX / 3, windowY)
    pen.down()
    pen.fillcolor("orange")
    pen.begin_fill()
    for i in range(4):
        pen.forward(windowX)
        pen.left(90)
    pen.end_fill()
def draw_x(x,y):
    pen.up()
    pen.goto(x - (3/4), y - (3/4))
    pen.down()
    pen.goto(x + (3/4), y + (3/4))
    pen.up()
    pen.goto(x - (3/4), y + (3/4))
    pen.down()
    pen.goto(x + (3/4), y - (3/4))

def draw_O(x,y):
    pen.up()
    pen.setpos(x,y - (3/4))
    pen.circle(3/4)

def draw_x_or_o(x,y):
    for i in range(9):
        if i % 2 == 0:
            draw_x(x,y)
        else:
            draw_O(x,y)

#
def drawPlay(x,y):
    draw_x_or_o(x,y)

draw_grid()

turtle.onscreenclick(drawPlay)

turtle.done()