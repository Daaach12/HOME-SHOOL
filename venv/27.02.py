from random import randint

n = int(input('Длина списка: '))
a = [randint(0, 100) for i in range(n)]
a.sort()
a.reverse()
print(a)
a.reverse()
qq = int(input('Искомое: '))
l = 0
r = n

while l < r - 1:
    m = (l + r) // 2
    if qq < a[m]:
        r = m
    else:
        l = m
if a[l] == qq:
    print(f'a[{n-l-1}]={qq}')
else:
    print('no founded')
