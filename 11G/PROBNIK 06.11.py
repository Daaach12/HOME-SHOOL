#№1   35


#№2   wzyx
# print('x y z w')
# for x in range (2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (x and not(y)or (y==z) or not(w))==0:
#                     print(x,y,z,w)


#№3   3570


#№4   5


#№5   163
# def f(N):
#     R=bin(N)[2:]
#     if N%3==0: R+=R[-3:]
#     else: R+=bin((N%3)*3)[2:]
#     return int(R,2)
#
# mas=[]
# for i in range(500):
#     if f(i)>151:
#         mas.append(f(i))
# print(mas)
# print(min(mas))


#№6.1   38
# from turtle import *
# tracer(0)
# lt(90)
# k=25
# for i in range(7):
#     fd(10*k)
#     rt(120)
# up()
# for x in range(10):
#     for y in range(10):
#         goto(x*k,y*k)
#         dot(3,'red')
# exitonclick()


#№6.2   18
from turtle import *
tracer(0)
k=20
lt(90)
for i in range(2):
    fd(8*k)
    rt(90)
    fd(18*k)
    rt(90)
up()
fd(4*k)
rt(90)
fd(10*k)
lt(90)
down()
for i in range(2):
    fd(17*k)
    rt(90)
    fd(7*k)
    rt(90)
up()
for x in range(25):
    for y in range(25):
        goto(x*k,y*k)
        dot(3,'red')
exitonclick()


#№7   288


#№8   180


#№9   83


#10   17


#11   4352


#12   152
# for n in range(4,10000):
#     s='5'+'2'*n
#     while ('52' in s) or ('2222' in s) or ('1122' in s):
#         s=s.replace('52','11',1)
#         s=s.replace('2222','5',1)
#         s=s.replace('1122','25',1)
#     if s.count('1')+s.count('5')*5+s.count('2')*2==64:
#         print(n)
#         break


#13   8


#14