from random import randint
obed = 1005
n = 0
result = ''
soups = [
    'Борщ (600гр)',
    'Молочная лапша (500гр)',
    'Куриный суп (600гр)',
    'Суп Харчо (550гр)',
    'Щи с говядиной (600гр)',
    'Щи с курицой (600гр)',
    'Суп солянка (400гр)',
    'Уха (400гр)',
    'Томатный суп (500гр)'
]
soupsccal = [
    420,
    600,
    306,
    810,
    246,
    270,
    304,
    668,
    165
]
index = randint(0, len(soups) - 1)
n += soupsccal[index]
result += soups[index]
haresult = result
while n > obed - 100:
    n = 0
    result = ''
    soupsccal.pop(index)
    soups.pop(index)
    index = randint(0, len(soups) - 1)
    n += soupsccal[index]
    result += soups[index]
    haresult = result

seconddish = [
    'Рис на сковороде (200гр)',
    'Жареная печень с луком (200гр)',
    'Творожная запеканка (150гр)',
    'Жареные шампиньоны с овощами (300гр)',
    'Котлеты (250гр)',
    'Картофельные драники (150гр)',
    'Жареная свинина (170гр)',
    'Макароны с фаршем на сковороде (200гр)',
    'Говяжья печень в сметане (200гр)'
]
secondccal = [
    294,
    258,
    291,
    387,
    680,
    247,
    374,
    550,
    284
]
newseconddish = seconddish
newsecondccal = secondccal
if n < obed - 150:
    index = randint(0, len(newseconddish) - 1)
    n += newsecondccal[index]
    result += f'\n{newseconddish[index]}'
while n > obed + 150:
    n -= newsecondccal[index]
    result = haresult
    newseconddish.pop(index)
    newsecondccal.pop(index)
    print(index)
    print(newsecondccal)
    index = randint(0, len(newsecondccal) - 1)
    n += secondccal[index]
    result += f'\n{seconddish[index]}'
haresult = result

salat = [
    'Винегрет с растит. маслом (300гр)',
    'Тертая морковь (300гр)',
    'салат из капусты (300гр)',
    'Морская капуста с морковью "По-корейски" (300гр)',
    'салат из моркови и яблок (300гр)',
    'салат оливье (200гр)',
    'Фруктовый салат (200гр)'
]
salatccal = [
    130,
    128,
    99,
    210,
    55,
    396,
    220
]

while n < obed - 150:
    if len(salat) == 0:
        break
    else:

        index = randint(0, len(salat) - 1)
        n += salatccal[index]
        result += f'\n{salat[index]}'
        if n > obed + 150:
            result = haresult
            n -= salatccal[index]
        salat.pop(index)
        salatccal.pop(index)