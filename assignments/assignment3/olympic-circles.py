#Author: Drew Rafferty

cSize = float(input("Size (1-10): "))

import turtle

turtle.bgcolor("white")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)

blackRing = cSize
blueRing = cSize
redRing = cSize
yellowRing = cSize
greenRing = cSize

#black
pen.pencolor("black")
pen.circle(cSize)
blackPos = pen.pos()


#blue
pen.penup()
pen.setx(-blackRing - 1.5 * blackRing)
pen.pendown()
pen.pencolor("blue")
pen.circle(cSize)

#red
pen.penup()
pen.setx(blackRing + 1.5 * blackRing)
pen.pendown()
pen.pencolor("red")
pen.circle(cSize)

#green
pen.penup()
pen.setx(blackRing + 1.5 / 2 + blackRing / 3 )
pen.sety(blackRing - 2.5 * blackRing )
pen.pendown()
pen.pencolor("green")
pen.circle(cSize)

#yello
pen.penup()
pen.setx(-blackRing + 1.5 / 2 - blackRing / 3 )
pen.sety(blackRing - 2.5 * blackRing)
pen.pendown()
pen.pencolor("yellow")
pen.circle(cSize)

turtle.done()
