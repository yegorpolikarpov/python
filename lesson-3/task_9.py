"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""


import random


COLUMN_SIZE = 5
ROW_SIZE = 5
MIN_VAL = 0
MAX_VAL = 10
matrix = [[random.randint(MIN_VAL, MAX_VAL) for _ in range(ROW_SIZE)] for __ in range(COLUMN_SIZE)]
for row in matrix:
    print(row)

max_of_min_of_column = MIN_VAL
for j in range(ROW_SIZE):
    min_of_column = matrix[0][j]
    for i in range(COLUMN_SIZE):
        if min_of_column > matrix[i][j]:
            min_of_column = matrix[i][j]
    print(j, ': ', min_of_column)  # Вывод минимальных элементов столбцов
    if min_of_column > max_of_min_of_column:
        max_of_min_of_column = min_of_column

print(f"Максимальный элемент среди минимальных элементов столбцов матрицы: {max_of_min_of_column}")
