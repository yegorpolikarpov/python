"""
В одномерном массиве целых чисел определить два наименьших элемента. Они могут
быть как равны между собой (оба являться минимальными), так и различаться.
"""


import random


MIN_INT = 0
MAX_INT = 10
SIZE = 20
arr = [random.randint(MIN_INT, MAX_INT) for _ in range(SIZE)]
print(arr)

first_min = 0
second_min = 1

for i in range(1, len(arr)):
    if arr[i] <= arr[first_min]:
        second_min = first_min
        first_min = i
    elif arr[i] <= arr[second_min]:
        second_min = i

print(f"Два наименьших числа: {arr[first_min]}, {arr[second_min]}")
