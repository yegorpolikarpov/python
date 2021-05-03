"""
Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего
задания первых трех уроков.
Был взят алгоритм из задания 2.9:
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


import random
import timeit
import cProfile
import matplotlib.pyplot as plt
from graph import draw


def generate_numbers(size):
    MIN_INT = 1000000
    MAX_INT = 9999999
    numbers = [str(random.randint(MIN_INT, MAX_INT)) for _ in range(size)]
    numbers = ' '.join(numbers)
    return numbers

def f1(numbers):
    # numbers = input("Введите числа (между каждым должен быть пробел): \n")
    i = 0
    NUMBER = ""
    BIGGEST_DIGIT_SUM = 0
    NUMBER_WITH_BIGGEST_DIGIT_SUM = ""
    for i in numbers:
        if i == ' ':
            DIGIT_SUM = 0
            for j in NUMBER:
                DIGIT_SUM += int(j)
            if BIGGEST_DIGIT_SUM < DIGIT_SUM:
                BIGGEST_DIGIT_SUM = DIGIT_SUM
                NUMBER_WITH_BIGGEST_DIGIT_SUM = NUMBER
            NUMBER = ""
        else:
            NUMBER += i
    # print(f"Наибольшее число по сумме его цифр: {NUMBER_WITH_BIGGEST_DIGIT_SUM} с",
    #       f"суммой цифр равной {BIGGEST_DIGIT_SUM}")
    return None


def f2(numbers_str):
    # numbers = input("Введите числа (между каждым должен быть пробел): \n")
    numbers = numbers_str.split(' ')
    digit_sums = [sum(k) for k in [[int(j) for j in i] for i in numbers]]
    BIGGEST_DIGIT_SUM = max(digit_sums)
    NUMBER_WITH_BIGGEST_DIGIT_SUM = numbers[digit_sums.index(BIGGEST_DIGIT_SUM)]
    # print(f"Наибольшее число по сумме его цифр: {NUMBER_WITH_BIGGEST_DIGIT_SUM} с",
    #       f"суммой цифр равной {BIGGEST_DIGIT_SUM}")

n = generate_numbers(1000000)
cProfile.run('f1(n)')
cProfile.run('f2(n)')
#         4 function calls in 2.608 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    2.608    2.608 <string>:1(<module>)
#        1    2.608    2.608    2.608    2.608 task_1.py:22(f1)
#        1    0.000    0.000    2.608    2.608 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#         1000008 function calls in 0.659 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.002    0.002    3.066    3.066 <string>:1(<module>)
#        1    0.000    0.000    3.064    3.064 task_1.py:44(f2)
#        1    0.377    0.377    2.547    2.547 task_1.py:45(<listcomp>)
#        1    0.000    0.000    3.066    3.066 {built-in method builtins.exec}
#        1    0.017    0.017    0.017    0.017 {built-in method builtins.max}
#  1000000    0.188    0.000    0.188    0.000 {built-in method builtins.sum}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        1    0.007    0.007    0.007    0.007 {method 'index' of 'list' objects}
#        1    0.069    0.069    0.069    0.069 {method 'split' of 'str' objects}

print("Generating integer numbers for the tests")
n = [10 ** i for i in range(7)]
temp = [generate_numbers(i) for i in n]
timeit_for_f1 = []
timeit_for_f2 = []
print("Testing f1 algorithm: ")
for i in temp:
    spam = timeit.timeit('f1(i)', number=100, globals=globals())
    print(spam)
    timeit_for_f1.append(spam)

# 0.00011560000000088166
# 0.002703200000000905
# 0.024903699999999418
# 0.247652200000001
# 2.7010609
# 26.205714299999997
# 256.85689579999996

print("Testing f2 algorithm: ")
for i in temp:
    spam = timeit.timeit('f2(i)', number=100, globals=globals())
    print(spam)
    timeit_for_f2.append(spam)

# 0.0003373999999780608
# 0.0020108999999592925
# 0.017671199999995224
# 0.16257720000004383
# 1.7548371999999972
# 17.43932209999997
# 186.6543719

# Ploting the results
# Credit to Сергей Криворучко
draw(False, "Мой график", [n, timeit_for_f1, "f1"], [n, timeit_for_f2, "f2"])
