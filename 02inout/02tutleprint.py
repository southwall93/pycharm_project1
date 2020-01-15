#-*-coding: utf-8-*-
import turtle
import random
pSize, tSize= 10,0
r,g,b=0.0,0.0,0.0

#함수 선언 - 2줄 띄우세요
#함수의 이름을 모두 소문자로 사용하세요
#변수의 이름도 모두 소문자로 사용하세요
#포함관계는 {}를 사용하지 않고 들여쓰기를 하세요
def screen_left_click(x,y):
    global r,g,b
    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.goto(x,y)

def screen_right_click(x,y):
    turtle.penup()
    turtle.goto(x,y)

def screen_mid_click(x,y):
    global r,g,b
    tSize=random.randrange(1,10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

#메인코드
turtle.title('거북이 그림그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screen_left_click, 1)
turtle.onscreenclick(screen_right_click, 3)
turtle.onscreenclick(screen_mid_click, 2)

turtle.done()
