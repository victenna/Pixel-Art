import turtle
import time
t=turtle.Turtle()
t1=turtle.Turtle()
turtle.tracer(30)
wn=turtle.Screen()
wn.bgcolor('red')
image='heart5.gif'
wn.addshape(image)
t.shape(image)
t.hideturtle()
t.up()


image1='heart4.gif'
wn.addshape(image1)
t1.shape(image1)
t1.up()
t1.goto(315,-200)

turtle.tracer(10)
def heart():
    t.showturtle()
    time.sleep(1)
    t.stamp()
    t.hideturtle()
  
for col in range(6):
    t.goto(0,-80*col)
    for row in range(7):
        t.fd(80)
        if col==0 and (row==1 or row==2 or row==4 or row==5) or col==1 and \
           (row==0 or row==3 or row==6) or col==2 and (row==0 or row==6):  
           heart()
        if col==3 and (row==1 or row==5) or col==4 and \
           (row==2 or row==4) or col==5 and row==3:
            heart()

        

            
            
            
            
                                     
                                          
    
                                           
                                     
