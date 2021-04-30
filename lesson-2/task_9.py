"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


numbers = input("Введите числа (между каждым должен быть пробел): \n")

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

print(f"Наибольшее число по сумме его цифр: {NUMBER_WITH_BIGGEST_DIGIT_SUM} с",
      f"суммой цифр равной {BIGGEST_DIGIT_SUM}")
