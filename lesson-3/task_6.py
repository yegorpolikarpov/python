"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и
максимальным элементами. Сами минимальный и максимальный элементы в сумму не
включать.
"""


import random


MIN_INT = 0
MAX_INT = 10
SIZE = 20
arr = [random.randint(MIN_INT, MAX_INT) for _ in range(SIZE)]
print(arr)

i_max = 0
i_min = 0
for i, a_i in enumerate(arr):
    if a_i > arr[i_max]:
        i_max = i
    if a_i < arr[i_min]:
        i_min = i

start = i_min + 1 if i_min < i_max else i_max + 1
finish = i_min if i_min > i_max else i_max
summa = 0
for i in range(start, finish):
    summa += arr[i]

print(f"Сумма между минимальным элементом ({arr[i_min]})",
      f" и максимальным ({arr[i_max]}): {summa}")
