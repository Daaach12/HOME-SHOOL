import random


array = []
for i in range(20):
    array.append(random.randint(0, 100))
print(array)
k = int(input("Enter the first index: "))
m = int(input("Enter the second index: "))
for i in range((m - k + 1) // 2):
    array[k + i], array[m - i] = array[m - i], array[k + i]
print(array)