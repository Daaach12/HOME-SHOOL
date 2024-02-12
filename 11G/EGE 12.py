# Функция поиска делителей числа n (не включая 1 и само число)
def find_divs(n):
    divs = set()  # Множество для хранения делителей
    for i in range(2, int(n ** 0.5) + 1):
        if len(divs)==4: return False
        # Если i делитель n
        if n % i == 0:
            # Добавляем делитель и парный ему в множество
            divs.add(i)  # Добавляем i в множество делителей
            divs.add(n // i)  # Добавляем парный делитель
    if len(divs)==3:
        return divs  # Возвращаем множество делителей числа n
    else: return False


for i in range(123456789, 223456789 + 1):
    divs = find_divs(i)  # Множество делителей числа i
    if find_divs(i):
        print(i,max(divs))
