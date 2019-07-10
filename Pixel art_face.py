import turtle
t=turtle.Turtle('square')
t.shapesize(2.5)

t.hideturtle()
t.speed('fastest')
t.up()    
t.goto(-240,100)

#Here is how your PixelArt is stored (using a "list of lists")

row0=[0,0,1,1,1,1,1,1,0,0]
row1=[0,1,1,1,1,1,1,1,1,0]
row2=[1,1,2,2,1,1,2,2,1,1]
row3=[1,1,2,2,1,1,2,2,1,1]
row4=[1,1,1,1,1,1,1,1,1,1]
row5=[1,3,1,1,1,1,1,1,3,1]
row6=[1,1,3,1,1,1,1,3,1,1]
row7=[1,1,1,3,4,4,3,1,1,1]
row8=[0,1,1,1,4,4,1,1,1,0]
row9=[0,0,1,1,1,1,1,1,0,0]

clm=[row0,row1,row2,row3,row4,row5,row6,row7,row8,row9]

clr=['gold','blue','black','red']

for i in range (10):
    #print(25)
    for j in range (10):
        
        t.fd(60)
        for k in range(4):
            if clm[i][j]==(k+1):
                t.showturtle()
                t.color(clr[k])
                t.stamp()
                t.hideturtle()
                     
    t.setposition(-240,100-60*(i+1))
    t.setheading(0)

    
            
        
    
       
    
