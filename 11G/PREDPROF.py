#№1
fin=open('students.csv','r',encoding='utf-8')
title=fin.readline()
student=[x.strip().split(',') for x in fin]
fin.close()

bal_sum={} #bal_sum {key - номер класса, value - сумма оценок}
bal_cnt={} #bal_cnt {key - номер класса, value - количество оценок}
for x in student:
    '''
x[0] - порядковый номер
x[1] - ФИО
x[2] - номер проекта
x[3] - класс
x[4] - оценка
'''

    if x[4]!='None':
        if x[3] in bal_sum:
            bal_sum[x[3]]+= int(x[4])
            bal_cnt[x[3]]+= 1
        else:
            bal_sum[x[3]]=int(x[4])
            bal_cnt[x[3]]=1


    fio=x[1].split()
    if fio[0]=='Хадаров' and fio[1]=='Владимир':
        print(f'Ты получил: {x[4]} за проект - {x[2]}')
for x in student:
    if x[4]=='None':
        x[4]=f'{bal_sum[x[3]]/bal_cnt[x[3]]:.3f}'
fout=open('students_new1.csv','w',encoding='utf-8')
fout.write(title)
for x in student:
    s=','.join(x)+'\n'
    fout.write(s)
fout.close()


#№2
fin=open('students.csv','r',encoding='utf-8')
title=fin.readline()
student=[x.strip().split(',') for x in fin]
fin.close()
for i in range(1,len(student)):
    for j in range(i,0,-1):
        if student[j][4]<student[j-1][4]:
            student[j], student[j - 1]=student[j - 1], student[j]
        else: break
cnt=0
for x in student:
    '''
x[0] - порядковый номер
x[1] - ФИО
x[2] - номер проекта
x[3] - класс
x[4] - оценка
'''

    if '10' in x[3] and x[4]=='5':
        cnt+=1
        fio=x[1].split()
        print(f'{cnt} место: {fio[1][0]}.{fio[0]}')
    if cnt==3: break



#№3
fin=open('students.csv','r',encoding='utf-8')
title=fin.readline()
student=[x.strip().split(',') for x in fin]
fin.close()

while True:
    n=input(' Введите № проекта (или СТОП): ')
    if n.upper()=='СТОП':
        break

    for x in student:
        '''
    x[0] - порядковый номер
    x[1] - ФИО
    x[2] - номер проекта
    x[3] - класс
    x[4] - оценка
    '''
        if x[2]==n:
            fio=x[1].split()
            print(f'Проект № {x[2]} делал: {fio[1][0]}. {fio[0]} он(а) получил(а) оценку - {x[4]}.')
            break
    else: print('Ничего не найдено.')


#№4
from random import choice

fin=open('students.csv','r',encoding='utf-8')
title=fin.readline().strip()
student=[x.strip() for x in fin]
fin.close()
simbol='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

for i in range(len(student)):
    x=student[i].split(',')
    '''
x[0] - порядковый номер
x[1] - ФИО
x[2] - номер проекта
x[3] - класс
x[4] - оценка
'''
    fio=x[1].split()
    login=fio[0]+'_'+fio[1][0]+fio[2][0]

    password='' #.join(choice(simbol) for _ in range (8))
    for _ in range(8):
        password+=choice(simbol)
    student[i]=student[i]+','+login+','+password
fout=open('students_passwords.csv','w',encoding='utf-8')
fout.write(title+',login,password\n')
for x in student:
    fout.write(x+'\n')
fout.close()


# №5
def hash_str(st):
    # def hash_str() - функция, которая создает хеш строки
    # входные параметры: st - строка данных
    # выходные параметры: hash_name - hash-строка
    p = 67
    m = 10 ** 9 + 9
    alf = 'ёЁйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТБЮ '
    d = {} #d={symbol: ind for ind, symbol in enumerate(alf, 1)}
    for ind, symbol in enumerate(alf, 1):
        d[symbol] = ind

    hash_name = 0
    for i in range(len(st)):
        hash_name += d[st[i]] * p ** i
    return hash_name % m


fin = open('students.csv', 'r', encoding='utf-8')
title = fin.readline()
student = [x.strip().split(',') for x in fin]
fin.close()

fout = open('students_with_hash.csv', 'w', encoding='utf-8')
fout.write(title)
for x in student:
    '''
x[0] - порядковый номер
x[1] - ФИО
x[2] - номер проекта
x[3] - класс
x[4] - оценка
'''
    s = ','.join((str(hash_str(x[1])), x[1], x[2], x[3], x[4])) + '\n'
    print(s)
    fout.write(s)
#ewerwerwrwerrwerwrewerwerw
#dggggg
#gdgdfgdf