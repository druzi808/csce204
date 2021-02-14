#Author: Drew Rafferty
import turtle

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.color("black")

#square
squareSize = 100

pen.up()
pen.setpos(-squareSize/2,-squareSize)
pen.down()
pen.fillcolor("orange")
pen.begin_fill()
for i in range(4):
    pen.forward(squareSize)
    pen.left(90)
pen.end_fill()

#triangle
pen.up()
pen.setpos(-squareSize/2 - squareSize/10,-squareSize + squareSize)
pen.down()
triangleSize = 120

pen.fillcolor("purple")
pen.begin_fill()
for i in range(3):
    pen.forward(triangleSize)
    pen.left(120)
pen.end_fill()


#tree
treeBase = squareSize/4

pen.up()
pen.setpos(squareSize,-squareSize)
pen.down()
pen.fillcolor("brown")
pen.color("brown")
pen.begin_fill()
for i in range(4):
    pen.forward(treeBase)
    pen.left(90)
pen.end_fill()


pen.up()
pen.setpos(squareSize + treeBase/2,-squareSize + squareSize/5)
pen.down()
pen.fillcolor("green")
pen.color("green")
pen.begin_fill()
pen.circle(treeBase)
pen.end_fill()

turtle.done()