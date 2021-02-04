#Author: Drew Rafferty
import turtle

grade = float(input("Enter your Grade: "))

largeCircle = 100
smallCircle = largeCircle * 3/4
eyeSize = smallCircle * 0.1

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.color("black")
pen.fillcolor("white")

if grade >= 80:
    grade = "Smiley"
    pen.sety(-largeCircle)
    pen.begin_fill()
    pen.circle(largeCircle)
    pen.end_fill()

    #left eye
    pen.fillcolor("black")
    pen.up()
    pen.sety(-largeCircle + 1.5 * smallCircle)
    pen.setx(-smallCircle * .5)
    pen.down()
    pen.begin_fill()
    pen.circle(eyeSize)
    pen.end_fill()

    #right eye
    pen.fillcolor("black")
    pen.up()
    pen.sety(-largeCircle + 1.5 * smallCircle)
    pen.setx(smallCircle * .5)
    pen.down()
    pen.begin_fill()
    pen.circle(eyeSize)
    pen.end_fill()

    #smile
    pen.penup()
    pen.goto(-25,-25)
    pen.pendown()
    pen.circle(75,67.5)  
    pen.penup()           
    pen.setheading(180) 
    pen.goto(-25,-25)
    pen.pendown()
    pen.circle(-75,67.5)




elif grade >= 70:
    grade = "Straight Face"
else:
    grade = "Frown"


turtle.done()