#Author: Drew Rafferty

import turtle

turtle.setup(575, 575)
pen = turtle.Turtle()
turtle.bgcolor("skyblue")
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

#Title
turtle.penup()
turtle.setpos(-250, 250)
turtle.down()
style = ("Arial", 12, "bold")
turtle.write("Shapes List", font = style)
#add shapes
#add colors


turtle.done()