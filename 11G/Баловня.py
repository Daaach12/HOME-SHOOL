'''a=int(input("Введите число: "))
summ=0
for i in range (a,51):
    summ+=i**2
print(summ)'''
'''
l=10
k=1
summ=l
for i in range(9):
    l+=l/10
    k+=1
    print(f'Лыжник пробежал {round(l,2)}км за {k} день')
for i in range (6):
    l += l / 10
    summ+=l
print(f'Суммарно за неделю лыжник пробежал {round(summ,2)}км')
'''

k=1
n=int(input('Введите число: '))
while n//10!=0:
    n//=10
    k+=1
print(k)