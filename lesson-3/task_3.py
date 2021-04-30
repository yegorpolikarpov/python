"""
В массиве случайных целых чисел поменять местами минимальный и максимальный
элементы.
"""


import random


MIN_INT = 0
MAX_INT = 100
SIZE = 10
arr = [random.randint(MIN_INT, MAX_INT) for _ in range(SIZE)]
print(arr)

max_element = arr[0]
min_element = arr[0]
for i in arr:
    if i > max_element:
        max_element = i
    if i < min_element:
        min_element = i

print(f'min = {min_element}')
print(f'max = {max_element}')
