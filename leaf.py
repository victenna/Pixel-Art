#PIXEL ART, leaf
import turtle
t=turtle.Turtle('square')
t.shapesize(1)

t.hideturtle()
turtle.tracer(3)
#t.speed('fastest')
t.up()    
t.goto(-240,100)
t.color('red')

#Here is how your PixelArt is stored (using a "list of lists")

row0=[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0]
row1=[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0]
row2=[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0]
row3=[0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0]
row4=[0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,0,0,0,0]
row5=[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0]
row6=[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0]
row7=[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
row8=[0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0]
row9=[1,1,1,0,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,1]
row10=[0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0]
row11=[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]
row12=[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]
row13=[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]
row14=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
row15=[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]
row16=[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0]
row17=[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0]
row18=[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0]
row19=[0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0]
row20=[0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0]
row21=[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0]
row22=[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0]
row23=[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0]
row24=[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0]
row25=[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0]

clm=[row0,row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12,\
     row13,row14,row15,row16,row17,row18,row19,row20,row21,\
     row22,row23,row24,row25]

box=10
for i in range (26):
    #print(25)
    for j in range (24):
        t.fd(box)
        #print(clm[i][j])

        
        if clm[i][j]==1:
                t.showturtle()
                #t.color(clr[k])
                t.stamp()
                t.hideturtle()
              
    t.setposition(-240,100-box*(i+1))
    t.setheading(0)
