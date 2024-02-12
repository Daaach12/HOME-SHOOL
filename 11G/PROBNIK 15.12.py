# №1 45
#
# №2 zxwy
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (not((not(y))or z)or(x==w)or x)==0:
#                     print(x,y,z,w)
#
# №3 820
#
# №4 1111
#
# №5 33
# def F(N):
#     R=bin(N)[2:]
#     if N%2==0:
#         R+='10'
#     else:
#         R='11'+R+'1'
#     R=int(R,2)
#     return R
# for i in range(100):
#     if F(i)>441:
#         print(i)
#         break
#
# №6 257
# from turtle import *
# tracer(0)
# k=25
# lt(90)
# for i in range(7):
#     fd(10*k)
#     rt(60)
# up()
# for x in range(-10,20):
#     for y in range(-10, 20):
#         goto(x*k,y*k)
#         dot(3,'red')
# exitonclick()
# print(17*11+70)
# №7 150
# print(640*320*6/8/1024)
#
# №8 24
# print(4*3*2*1)
#
# №9 2601
#
# №10 10
#
# №11 300
#
# №12 888
# s='1'*84
# while ('1111' in s) or ('8888' in s):
#     if ('1111' in s):
#         s=s.replace('1111','888',1)
#
#     else:
#         s=s.replace('8888','8',1)
#
# print(s)
# №13
#
# №14
# c=9**11 * 3**20 - 3**9 - 27
# ans=''
# cnt=0
# while c!=0:
#     if c%3==2:
#         cnt+=1
#     c=c//3
# print(cnt)
# while c != 0:
#     ans += str(c % 3)
#     c //= 3
# print(ans)
# print(ans.count('2'))

#№15

#№16

#№17

#№18

#№19-21

#№22

#№23

# № 15
# for a in range(100):
#     print(a)
#     flag=True
#     for x in range(1000):
#         for y in range(1000):
#             if ((x * y < a) or (x < y) or (7 <= x))==0:
#                 flag = False
#     if flag:
#         print(a)
#         break


# def F(n):
#     if n<3:
#         return 1
#     if n>2:
#         if n%2==0:
#             return F(n-2)-F(n-1)
#         else: return 2*F(n-1)-F(n-2)
# print(F(19))
#
# a=[int(x) for x in open('17.txt')]
# cnt=mm=0
# for i in range(len(a)-1):
#     if a[i]%10==5 and a[i+1]%10==5:
#         cnt+=1
#         mm=max(mm,abs(a[i]-a[i+1]))
# print(cnt,mm)


# def F(s,c,m):
#     if s>=35: return c%2==m%2
#     if c==m: return 0
#     h=[F(s+1,c+1,m),F(s+4,c+1,m),F(s*2,c+1,m)]
#     return any(h) if (c+1)%2==m%2 else all(h)
# for s in range(1,35):
#     for m in range(1,5):
#         if F(s,0,m):
#             if m==4:
#                 print(m,s)
#             break
# #17
# #13 16
# #12
# def F(x,y):
#     if x==y: return 1
#     if x<y: return 0
#     else: return F(x-2,y)+F(x-5,y)
# print(F(17,1))

# cnt=mcnt=0
# s=open('24.txt').readline()
# for i in range(len(s)):
#     if (s[i] in 'AB') or (s[i] in 'BC'):
#         cnt+=1
#         mcnt=max(mcnt,cnt)
#     else: cnt=0
# print(mcnt)
from fnmatch import *
for x in range(0, 10**8, 317): # Перебираем все числа от 0 с шагом 317, будут получены числа кратные 317
    if fnmatch(str(x), '12??1*56'):# Проверяем полученное число соответствию заданию
        print(x, x // 317)