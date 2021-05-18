"""
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в виде
функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random


def bubble_sort(arr_original):
    arr = arr_original.copy()
    n = 1
    n_arr = len(arr)
    while n < n_arr:
        for i in range(n_arr-n):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        n += 1
    return arr


def bubble_sort_plus(arr_original):
    arr = arr_original.copy()
    n = 1
    n_arr = len(arr)
    while n < n_arr:
        is_sorted = True
        for i in range(n_arr-n):
            if arr[i] < arr[i+1]:
                is_sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
        n += 1
        if is_sorted:
            break
    return arr

MIN = -100
MAX = 99
SIZE = 20
arr = [random.randint(MIN, MAX) for _ in range(SIZE)]

print('Original array:',
      arr,
      'Sorted:',
      bubble_sort(arr),
      'Original array after sorting:',
      arr,
      'Sorted by "smarter" bubble sort:',
      bubble_sort_plus(arr),
      'Original array after sorting:',
      arr, sep='\n')
