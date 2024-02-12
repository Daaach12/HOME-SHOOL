# def f(x,a):
#     return ((x%a==0) and (x%24==0) and (x%16!=0))<=(x%a!=0)
# for a in range(1,300):
#     if all(f(x,a)==1 for x in range(1,3000)):
#         print(a)
#         break

# def f(x,a):
#     return ((x%4!=3) or (x%6!=1))<=(x%36!=a)
# for a in range(1,300):
#     if all(f(x,a)==1 for x in range(1,3000)):
#         print(a)
#         break


# def f (x,a):
#     return (a%7==0)and ((240%x==0)<=((a%x!=0)<=(780%x!=0)))
# for a in range(1,3000):
#     if all(f(x,a)==1 for x in range(1,30000)):
#         print(a)
#         break


def f (x,y,a):
    return (x**2-10*x+16>0)or(y**2-10*y+21>0)or(x*y<2*a)
for a in range(1,30000):
    if all(f(x,y,a)==1 for x in range(1,3000) for y in range(1,3000)):
        print(a)










