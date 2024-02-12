'''
for i in range (126849, 126871+1):
    q=int(i**0.5)
    k = 0     #count=0
    a = []
    for n in range (1,q+1):
        if i%n==0:
            a.append(n)
            k+=1
            if n!=i//n:
                k+=1
                a.append(i//n)
    if k==4:
        a.sort()
        print(a)
'''
'''
for i in range (1820348, 2880927+1):
    a=[]
    count=0
    for n in range (1,int(i**0.5)+1):
        if i%n==0:
            count+=1
            a.append(n)
            if n!=i//n:
                count+=1
                a.append(i//n)
    if count==5:
        a.sort()
        print(a)

'''
'''
a=[]
num=0
for i in range (2943444, 2943529+1):
    count=0
    num+=1
    for n in range (1,int(i**0.5)+1):
        if i%n==0:
            count+=1
            if n!=i//n:
                count+=1
    if count==2:
        i=f'{num}) {i}'
        a.append(i)
a.sort()
print(a)
'''
a=[]
for i in range(33333, 55555):
    count = 0
    summ = 0
    for n in range(1, int(i ** 0.5) + 1):
        if i % n == 0:
            count += 1
            if n != i // n:
                count += 1
    if count == 2:
        i = str(i)
        for q in i:
            summ += int(q)
        if summ > 35: a.append(f'{i}  сумма = {summ}')
print(a)
