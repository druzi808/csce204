#Author: Drew Rafferty

import turtle

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.color("black")
pen.fillcolor("red")

#width
uHaulWidth = 300
uHaulBoxWidth = uHaulWidth * 3/4
uHaulCabWidth = uHaulWidth - uHaulBoxWidth

#heights
uHaulHeight = uHaulWidth * 5/8
uHaulBoxHeight = uHaulHeight * 2/3
uHaulCabHeight = uHaulBoxHeight * 2/3
uHaulWheelRadius = (uHaulHeight - uHaulBoxHeight)/2

#draw box
pen.up()
pen.setpos(-uHaulWidth/2,-uHaulHeight/2)
pen.down()
pen.begin_fill()
pen.forward(uHaulWidth)
pen.left(90)
pen.forward(uHaulCabHeight)
pen.left(90)
pen.forward(uHaulCabWidth)
pen.right(90)
pen.forward(uHaulBoxHeight - uHaulCabHeight)
pen.left(90)
pen.forward(uHaulBoxWidth)
pen.left(90)
pen.forward(uHaulBoxHeight)
pen.end_fill()


#left wheel
pen.up()
pen.setpos(-uHaulWidth/2 + uHaulWidth * 1/3 - uHaulWheelRadius, -uHaulHeight + uHaulWheelRadius * 2)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(uHaulWheelRadius)
pen.end_fill()



#right wheel
pen.up()
pen.setpos(-uHaulWidth/2 + uHaulWidth * 2/3 - uHaulWheelRadius, -uHaulHeight + uHaulWheelRadius * 2)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(uHaulWheelRadius)
pen.end_fill()
turtle.done()