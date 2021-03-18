# Author: Drew Rafferty
import turtle
import random 

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

colors = ["red", "yellow", "orange", "blue", "green", "white"]

def draw_square(x, y, width, color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    color = random.choice(colors)
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(4):
        pen.forward(width)
        pen.left(90)
    pen.end_fill()

def draw_cube(x, y, width, color):
    draw_square(x - width/3, y - width/3, width/3, color)
    draw_square(x + width/3, y + width/3, width/3, color)
    draw_square(x - width/3, y + width/3, width/3, color)
    draw_square(x + width/3, y - width/3, width/3, color)
    draw_square(x , y + width/3, width/3, color)
    draw_square(x , y - width/3, width/3, color)
    draw_square(x - width/3 , y, width/3, color)
    draw_square(x + width/3 , y, width/3, color)
    draw_square(x , y, width/3, color)


for i in range(10):
    color = "blue" #Choose a random color
    x = random.randint(-int(turtle.window_width()/2), int(turtle.window_width()/2))
    y = random.randint(-int(turtle.window_height()/2), int (turtle.window_height()/2))
    size = random.randint(20, 100)
    draw_cube(x,y,size, color)

turtle.done()