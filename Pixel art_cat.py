#Pixel Art - http://www.101computing.net/pixel-art-in-python/

import turtle


Pen = turtle.Turtle()
wn=turtle.Screen()

wn.tracer(0)
Pen.speed(0)
#Pen.color("#000000")
Pen.color("black")

a1=turtle.Turtle()
a1.hideturtle()
a1.pendown()

for j in range (13):
    a1.penup()
    a1.goto(0,20*j)
    a1.goto(320,20*j)
    a1.penup()
    a1.goto(0,20*j)
    a1.pendown()
    a1.goto(320,20*j)

for i in range (17):
    a1.penup()
    a1.goto(20*i,0)
    a1.goto(20*i,240)
    a1.penup()
    a1.goto(20*i,0)
    a1.pendown()
    a1.goto(20*i,240)

# This function draws a box by drawing each side of the square and using the fill function
def box(face):
    Pen.begin_fill()
    # 0 deg.
    Pen.forward(face)
    Pen.left(90)
    # 90 deg.
    Pen.forward(face)
    Pen.left(90)
    # 180 deg.
    Pen.forward(face)
    Pen.left(90)
    # 270 deg.
    Pen.forward(face)
    Pen.end_fill()
    Pen.setheading(0)
	
boxSize = 20	
#Position myPen in top left area of the screen

Pen.penup()
#  #!!!!!!!!!!!!
#Pen.forward(-100)
Pen.setheading(90)
Pen.goto(0,120)
Pen.forward(100)
Pen.setheading(0)

##Here is an example of how to draw a box	
#box(boxSize)

##Here are some instructions on how to move "myPen" around before drawing a box.
#myPen.setheading(0) #point to the right, 90 to go up, 180 to go to the left 270 to go down
#myPen.penup()
#myPen.forward(boxSize)
#myPen.pendown()

#Here is how your PixelArt is stored (using a "list of lists")

pixels     = [[0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0]]
pixels.append([1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0])
pixels.append([1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1])
pixels.append([1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1])
pixels.append([1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1])
pixels.append([1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1])
pixels.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])
pixels.append([0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0])
pixels.append([0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0])
pixels.append([0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,0])
pixels.append([0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0])
pixels.append([0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0])

for column in pixels:
        for item in column:
                print(item, end = " ")
        print()

#print(pixels,"n\\")


for i in range (0,len(pixels)):
    for j in range (0,len(pixels[i])):
        if pixels[i][j]==1:
            box(boxSize)
        Pen.penup()
        Pen.forward(boxSize)
        Pen.pendown()	
    Pen.setheading(270) 
    Pen.penup()
    Pen.forward(boxSize)
    Pen.setheading(180) 
    Pen.forward(boxSize*len(pixels[i]))
    Pen.setheading(0)
    Pen.pendown()
	
Pen.getscreen().update()	
