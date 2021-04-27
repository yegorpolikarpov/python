"""
Напишите программу, доказывающую или проверяющую, что для множества натуральных
чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное
число.
"""

n = int(input("Введите количество элементов в сумме натуральных чисел: n = "))
SUM = 0
for i in range(n):
    SUM += i + 1
expression = n * (n + 1) / 2
print(f"Значение суммы найденное через сложение всех элементов (1+2+...+n) = {SUM}")
print(f"Значение суммы найденное через формулу (n(n+1)/2) = {expression}")
if SUM == expression:
    print("Соответственно, равенство 1+2+...+n = n(n+1)/2 верно.")
else:
    print("Соответственно, равенство 1+2+...+n = n(n+1)/2 неверно.")
