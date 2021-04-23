#  Вводятся три разных числа. Найти, какое из них является средним
#  (больше одного, но меньше другого).

print("Введите три разных числа: ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if (a > b and a < c) or (a < b and a > c):
    print(f"Среднее число: a = {a}")
elif (b > a and b < c) or (b < a and b > c)
    print(f"Среднее число: b = {b}")
else:
    print(f"Среднее число: c = {c}")
