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
shapes = []
colors = []
size = int(turtle.numinput("Shapes", "Enter Amount of Shapes: ", 1, 1, 6))
#size = int(turtle.numinput("Shapes", "Enter Amount of Shapes (circle, triangle, square, star, or rectangle): ", 1, 1, 6))



#gather shapes and colors

for i in range (size):
    shapeType = turtle.textinput("Shapes", "Enter Shape (circle, triangle, square, diamond, or rectangle): ").strip()
    shapes.append(shapeType)
    shapeColor = turtle.textinput("Colors", "Enter Shape Color (red, orange, yellow, green, blue): ").strip()
    colors.append(shapeColor)
    #triangle
    if shapeType == "triangle":
        pen.up()
        pen.setpos(-159,0)
        pen.down()
        pen.color(shapeColor)
        pen.begin_fill()
        for i in range(3):
            pen.forward(100)
            pen.left(120)
        pen.end_fill()
        pen.up()
        pen.setpos(-150, 100)
        style2 = ("Arial", 7, "bold")
        pen.write(shapeColor + " triangle", font = style2)
        pen.down()     
    #circle
    elif shapeType == "circle":
        pen.up()
        pen.setpos(-200,0)
        pen.down()
        pen.color(shapeColor)
        pen.begin_fill()
        pen.circle(50)
        pen.end_fill()

        pen.up()
        pen.setpos(-225, 100)
        style2 = ("Arial", 7, "bold")
        pen.write(shapeColor + " circle", font = style2)
        pen.down()       
    #square
    elif shapeType == "square":
        pen.up()
        pen.setpos(-50,0)
        pen.down()
        pen.color(shapeColor)       
        pen.begin_fill()
        for i in range(4):
            pen.forward(100)
            pen.left(90)
        pen.end_fill()
        pen.up()
        pen.setpos(-35, 100)
        style2 = ("Arial", 7, "bold")
        pen.write(shapeColor + " square", font = style2)
        pen.down()     
    #diamond
    elif shapeType == "diamond":
        #up triangle
        pen.up()
        pen.setpos(75,50)
        pen.down()
        pen.color(shapeColor)
        pen.begin_fill()
        for i in range(3):
            pen.forward(100)
            pen.left(120)
        #down triangle
        for i in range(3):
            pen.forward(100)
            pen.left(-120)
        pen.end_fill()
        pen.up()
        pen.setpos(85, 130)
        style2 = ("Arial", 7, "bold")
        pen.write(shapeColor + " diamond", font = style2)
        pen.down()     
    else:
        pen.write("INVALID INPUT", font = style)

#for loop
#if shape[i] == "cirlce"
    #print circle


turtle.done()