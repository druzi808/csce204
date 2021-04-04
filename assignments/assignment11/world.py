#Author: Drew Rafferty
import turtle
import random

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

def getScene():
    sceneShapes = []
    with open("assignments/assignment11/scene.txt") as file:
        for line in file:
            sceneShape = line.replace("\n", "").strip().lower()
            sceneShapes.append(sceneShape)   
        return sceneShapes

def drawStar(x,width):
    drawTriangle(x,y,size)
    drawUpsideDownTriangle(x,y,size)

def drawTree(x,width):

    #tree
    squareSize = 50
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

def drawTriangle(x,y,size):
    #draw up triangle
    size = 50

    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.fillcolor("yellow")
    pen.begin_fill()
    for i in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()


def drawUpsideDownTriangle(x,y,size):
    #draw down triangle
    size = 50

    pen.up()
    pen.setpos(x, y + size/2)
    pen.down()
    pen.begin_fill()
    for i in range(3):
        pen.forward(size)
        pen.left(-120)
    pen.end_fill()


#PROGRAM


shapes = getScene()
numShapes = len(shapes)
width = 50
size = 50
x = turtle.window_width()/numShapes
y = turtle.window_height()/numShapes

for shape in shapes:
    if shapes == "star":
        drawStar(x, width)
    elif shapes == "tree":
        drawTree(x,width)
turtle.done()