from turtle import *
tracer(0)
k=30
for i in range (7):
    goto(6*k,-9*k)
    goto(-6*k,2*k)
    goto(12*k,3*k)
up()
for x in range(-10,15):
    for y in range(-15, 15):
        goto(x*k,y*k)
        dot(3,'red')
exitonclick()