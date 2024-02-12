# #174
# A=[int(i) for i in open('17-4.txt')]
# k=0
# minn=20000
# for i in A:
#     if i > 100:
#         if i%100//10<=4:
#             if 3<=i%1000//100<=7:
#                 k+=1
#                 minn=min(minn,i)
# print(k, minn)


# #175
# A=[int(x) for x in open('17-4.txt')]
# c=0
# maxx=0
# for i in A:
#     p=str(i)
#     l=len(p)
#     q = 0
#     for w in range (l):
#         q+=int(p[w-1])
#         print(q)
#     if q%5==0:
#         if i%3+i//3%3!=0:
#                 c+=1
#                 maxx=max(maxx,i)
# print(c, maxx)

