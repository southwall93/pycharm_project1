import turtle
import random

swidth,sheight,pSize,exitcount=300,300,0,0
r,g,b, angle, dist, curX, curY = [0]*7

turtle.title("거북이가 맘대로 다니기")
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width=swidth + 30, height = sheight + 30)

while True:
    r = random.random()
    g = random.random()
    b = random.random()

    turtle.pencolor((r,g,b))

    angle= random.randrange(0,360)
    dist=random.randrange(10,100)
    turtle.left(angle)
    turtle.forward(dist)
    curX=turtle.xcor()
    curY=turtle.ycor()

    if(-swidth/2<=curX and curX <= swidth/2) and (-sheight/2<=curY and curY <= sheight/2):
        pass
    else:
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()

        exitcount +=1
        #while문 바깥으로 빠져나가는 조건문
        if exitcount>5:
            break

turtle.done()