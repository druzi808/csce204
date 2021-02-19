#Author: Drew Rafferty
#submitting this because i keep getting an error on the for loop when trying to loop through the list
import turtle

turtle.bgcolor("white")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(1)
pen.color("black")
pen.hideturtle()
turtle.hideturtle()
turtle.speed(0)
turtle.colormode(255)
numShapes = int(turtle.numinput("Names", "Enter shape (circle, square, trianlge, or star)", 10, 0,100))

shapes = ["circle", "square", "triangle", "star"]


for i in range(shapes):
    if numShapes == "1":
        #draw a circle
        pen.setpos(-200,300)
        pen.pendown()
        pen.circle(50)
        pen.penup()
    #elif numShapes == "2":
        #circle & square
    #elif numShapes == "3":
        #circle square and triangle
    #elif numShapes == "4":
        #circle square triangle and star
    #else: 
        #cirlce square triangle and x

    

turtle.done()