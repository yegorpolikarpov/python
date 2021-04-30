"""
Посчитать, сколько раз встречается определенная цифра в введенной
последовательности чисел. Количество вводимых чисел и цифра, которую необходимо
посчитать, задаются вводом с клавиатуры.
"""


def counter(number, digit_to_count):
    last_digit = number % 10
    if number == 0:
        return 0
    if last_digit == digit_to_count:
        return 1 + counter((number - last_digit) / 10, digit_to_count)
    return counter((number - last_digit) / 10, digit_to_count)


n = int(input("Введите количество чисел в вашей последовательности: "))
a = int(input("Введите цифру (0-9): "))
COUNT = 0

for i in range(n):
    user_number = int(input(f"Число №{i+1}: "))
    COUNT += counter(user_number, a)

print(f"Цифра {a} встречается {COUNT} раз.")
