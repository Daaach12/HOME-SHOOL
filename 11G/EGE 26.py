#2
f=open('26-2.txt')
s,n=map(int,f.readline().split())
a=sorted([int(x) for x in f])
f.close()

sm,cnt=0,0
for i in range(n):
    if sm+a[i]<=s:
        sm+=a[i]
        cnt+=1
    elif sm-a[i]+a[i+1]<=s:
        sm=sm-a[i]+a[i+1]
    else:
        print(cnt,a[i])
        break

