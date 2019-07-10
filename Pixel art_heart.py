#PIXEL ART, heart
import turtle
import time
turtle.bgcolor('blue')

t= turtle.Turtle('turtle')
t.hideturtle()
wn=turtle.Screen()
image='heart3.gif'
wn.addshape(image)
t2=turtle.Turtle()
t2.shape(image)
t2.hideturtle()
t.speed('fastest')
t2.up()    
t2.goto(-240,0)

#Here is how your PixelArt is stored (using a "list of lists")

row0=[0,1,1,0,1,1,0]
row1=[1,0,0,1,0,0,1]
row2=[1,0,0,0,0,0,1]
row3=[0,1,0,0,0,1,0]
row4=[0,0,1,0,1,0,0]
row5=[0,0,0,1,0,0,0]

clm=[row0,row1,row2,row3,row4,row5]

for i in range (6):
    #print(25)
    for j in range (7):
        t2.fd(60)
        #print(px[i][j])
        if clm[i][j]==1:
            t2.showturtle()
            time.sleep(0.5)
            t2.stamp()
            t2.hideturtle()
    t2.setposition(-240,-60*(i+1))
    t2.setheading(0)
            
        
    
       
    
