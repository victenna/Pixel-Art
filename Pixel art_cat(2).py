import turtle
import time
t= turtle.Turtle()
wn=turtle.Screen()

wn.tracer(0)
t.speed(0)
#Pen.color("#000000")
t.color("black")

# This function draws a box by drawing each side of the square and using the fill function
def box(size,color):
    t.fillcolor(color)
    t.begin_fill()
    # 0 deg.
    t.forward(size)
    t.left(90)
    # 90 deg.
    t.forward(size)
    t.left(90)
    # 180 deg.
    t.forward(size)
    t.left(90)
    # 270 deg.
    t.forward(size)
    t.end_fill()
    t.setheading(0)
	

#Position t in top left area of the screen
t.penup()
t.forward(-100)
t.setheading(90)
t.forward(100)
t.setheading(0)

pixels     = [[0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0]]
pixels.append([1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0])
pixels.append([1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1])
pixels.append([1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1])
pixels.append([1,1,2,1,1,2,1,1,0,0,0,0,0,0,1,1])
pixels.append([1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1])
pixels.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])
pixels.append([0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0])
pixels.append([0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0])
pixels.append([0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,0])
pixels.append([0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0])
pixels.append([0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0])

for i in range (12):
    for j in range (16):
        if pixels[i][j]==1:
            box(40,'black')
        if pixels[i][j]==2:
            box(40,'blue')
        t.penup()
        t.forward(40)
        t.pendown()	
    t.setheading(270) 
    t.penup()
    t.forward(40)
    t.setheading(180) 
    t.forward(40*16)
    t.setheading(0)
    t.pendown()




