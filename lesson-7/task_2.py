"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

import random


def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return

    m = n // 2
    left = arr[:m]
    right = arr[m:]
    merge_sort(left)
    merge_sort(right)

    l = r = i = 0
    while l < m and r < n - m:
        if left[l] < right[r]:
            arr[i]  = left[l]
            l += 1
        else:
            arr[i] = right[r]
            r += 1
        i += 1

    if l < m:
        arr[i:] = left[l:]
    if r < n - m:
        arr[i:] = right[r:]


MIN = 0
MAX = 50
SIZE = 20
arr = [random.uniform(MIN, MAX) for _ in range(SIZE)]
# arr = [random.randint(MIN, MAX) for _ in range(SIZE)]

print(arr)
merge_sort(arr)
print(arr)
