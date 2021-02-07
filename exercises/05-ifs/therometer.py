#Author: Drew Rafferty

import turtle

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.color("black")
pen.fillcolor("pink")
style = ("Arial", 12, "normal")

#draw the therometer
tHeight = 400
tWidth = tHeight/4
pen.up()
pen.setpos(-tWidth/2, -tHeight/2)
pen.down()
pen.forward(tWidth)
pen.left(90)
pen.forward(tHeight)
pen.up()
pen.left(90)
pen.forward(tWidth)
pen.down()
pen.left(90)
pen.forward(tHeight)

#setup 0%
turtle.up()
turtle.setpos(tWidth/2 +20, - tHeight/2)
turtle.down()
turtle.write("0%", font = style)

#setup 25%
turtle.up()
turtle.setpos(tWidth/2 +20, - tHeight/4)
turtle.down()
turtle.write("25%", font = style)

#setup 50%
turtle.up()
turtle.setpos(tWidth/2 +20, 0)
turtle.down()
turtle.write("50%", font = style)

#setup 75%
turtle.up()
turtle.setpos(tWidth/2 +20, tHeight/4)
turtle.down()
turtle.write("75%", font = style)

#setup 100%
turtle.up()
turtle.setpos(tWidth/2 +20, tHeight/2)
turtle.down()
turtle.write("100%", font = style)

#get donations
donations = turtle.numinput("Donations", "Enter total Donations: ");
goal = 10000
percentGoal = donations/goal

#error check
if percentGoal < 0:
    percentGoal = 0
elif percentGoal > 1:
    percentGoal = 1

dHeight = tHeight * percentGoal

#draw
pen.up()
pen.setpos(-tWidth/2, -tHeight/2)
pen.down()
pen.fillcolor("red")
pen.begin_fill()
pen.setheading(0)
pen.forward(tWidth)
pen.left(90)
pen.forward(tHeight)
pen.left(90)
pen.forward(tWidth)
pen.left(90)
pen.forward(dHeight)
pen.end_fill()


#if reached
if percentGoal >= 1:
    turtle.up()
    turtle.setpos(-tWidth/2, tHeight/2 + 20)
    turtle.down()
    turtle.write("Goal Achieved", font = style)

turtle.done()