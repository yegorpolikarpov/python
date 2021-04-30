"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его
значение и позицию в массиве.
"""


import random


MIN_INT = -10
MAX_INT = 10
SIZE = 20
arr = [random.randint(MIN_INT, MAX_INT) for _ in range(SIZE)]
print(arr)

max_neg = MIN_INT
for number in arr:
    if max_neg < number < 0:
        max_neg = number
print(f"Максимальный отрицательный элемент: {max_neg}")
