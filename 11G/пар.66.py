
'''
#№2
a=input()
n=0
for i in range (len(a)):
    if a[i]!=a[len(a)-1-i]:
        n+=1
if n>0:
    print('не палиндром')
else: print('палиндром')
'''
'''
#№3
a=input()+'/'
n=0

for i in a:
    n+=1
    if i=='/':
        print(a[:n-1])
        a=a[n:]
        n=0
'''
'''
a=input()+'+'
n=0
q=0
b=0
for i in a:
    n+=1
    if i=='+':
      b=int(a[:n-1])
      q+=b
      a=a[n:]
      n=0
print(q)
'''
'''
#8
a=input('Название файла: ')
b=input('Необходимое разширение: ')
s=a.rfind('.')
a=a[:s+1]+b
print(a)
'''
'''
#9
a=' '+input('Введите сроку: ')+' '
b=' '+input('Искомое слово: ')+' '
s=a.find(b)
f=len(b)
c=0
while s!=-1:
    a=' '+a[a.find(b)+f:]
    s=a.find(b)
    c+=1
    print(a) #это мне для проверки, что все нормально срезает и нет косяков
print('слово встречается '+str(c)+' раз(а)')
'''

#10
n=int(input('Кол-во футболистов: '))
for i in range (n):
    if



