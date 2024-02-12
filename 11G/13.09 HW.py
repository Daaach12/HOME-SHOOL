'''
from turtle import *
k=25
tracer(0)
for i in range (15):
    fd(4*k)
    rt(60)
up()
for x in range (-10,10):
    for y in range (-10,10):
        goto(x*k,y*k)
        dot(3,'red')
exitonclick()
# Ответ: 38
'''


from turtle import *
tracer(0)
k=25
x=0
y=0
for i in range (7):
    x+=6
    y-=9
    goto(x*k,y*k)
    x-=6
    y+=2
    goto(x*k, y*k)
    x+=12
    y+=3
    goto(x*k, y*k)
up()

for x in range (0,100):
    for y in range (-35,2):
        goto(x*k,y*k)
        dot(3,'red')
exitonclick()
#Ответ: 70