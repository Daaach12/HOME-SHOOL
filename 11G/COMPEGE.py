#13
# for n in range(1000,3,-1):
#     s='5'+'2'*n
#     while '52' in s or '2222' in s or '1122' in s:
#         if '52' in s: s=s.replace('52','11',1)
#         if '2222' in s: s=s.replace('2222','5',1)
#         if '1122' in s: s=s.replace('1122','25',1)
#     if sum(list(map(int,s))) == 64:
#         print(n)
#         break





#14.1
# for x in range (0,19):
#     N=int(f'98897021',19)+x*19**2+int('20923',19)+x*19**3
#     if N%18==0:
#         print(N//18,x)



#14.2
# cnt=0
# N=3*3125**8+2*625**7-4*625**6+3*125**5-2*25**4-2024
# while N>0:
#     if N%25==0: cnt+=1
#     N//=25
# print(cnt)


#15
# for A in range(1,1000):
#     for x in range(1,500):
#         for y in range(1,500):
#             ok=((x+2*y<A) or (y>x) or (x>60))
#             if ok==0: break
#         if ok==0: break
#     if ok:
#         print(A)
#         break



#17
# A=[int(x) for x in open('17-3.txt')]
# B=[x for x in A if x%100==13]
# m13=max(B)
#
# cnt,ms=0,0
# for i in range(len(A)-2):
#     if (99<A[i]<1000)+(99<A[i+1]<1000)+(99<A[i+2]<1000)==2 and\
#         (A[i]+A[i+1]+A[i+2]<=m13):
#         cnt+=1
#         ms=max(ms,A[i]+A[i+1]+A[i+2])
# print(cnt,ms)



# #19-21
# def F(s,c,m):
#     if s>=129: return c%2==m%2
#     if c==m: return 0
#     h=[F(s+1,c+1,m), F(s*2,c+1,m)]
#     return any(h) if (c+1)%2==m%2 else all(h)
# for s in range(1,129):
#     for m in range (1,5):
#        if F(s,0,m):
#            if m==3:
#                print(s,m)



# #№5
# def f(N):
#     R=bin(N)[2:]
#     R+=R[-1]
#     if R.count('1')%2==0: R+='0'
#     else:R+='1'
#     R+='0'
#     return int(R,2)
# for N in range(1,150):
#     if f(N)>114:
#         print(N)
#         break



# #№23
# def F(x,stop):
#     if x>stop or x==11: return 0
#     if x==stop: return 1
#     return F(x+1,stop)+F(x*2,stop)+F(x**2,stop)
# print(F(2,9)*F(9,20))



#№24
s=open('24.txt').readline().split('T')
cnt=sum(len(s[i]) for i in range(101))
mc=0
for i in range(101,len(s)-1):
    cnt=cnt+len(s[i])-len(s[i-101])
    mc=max(mc,cnt)
print(mc)




