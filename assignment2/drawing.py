#Author: Drew Rafferty
#this was hard to do and didn't turn out how i expected
import turtle

turtle.bgcolor("white")

pen = turtle.Turtle()

pen.pensize(10)
pen.speed(.5)

#base circle
pen.color('black')
pen.pendown()
pen.circle(100)

#left ear
pen.penup()
pen.setx(-50)
pen.sety(185)
pen.pendown()
pen.left(180)
pen.begin_fill()
pen.right(90)
pen.circle(30, 250)
pen.end_fill()

#right ear
pen.penup()
pen.setx(50)
pen.sety(185)
pen.pendown()
pen.begin_fill()
pen.right(90)
pen.circle(30, -250)
pen.end_fill()

#left eye (i hope aha)
pen.penup()
pen.setx(-35)
pen.sety(95)
pen.pendown()
pen.begin_fill()
pen.circle(25)
pen.end_fill()

#right eye
pen.penup()
pen.setx(35)
pen.sety(95)
pen.pendown()
pen.circle(25)

#mouth
pen.color('black')
pen.penup()
pen.setx(0)
pen.sety(50)
pen.pendown()

pen.begin_fill()
pen.circle(10)
pen.end_fill()







turtle.done()