"""
Посчитать четные и нечетные цифры введенного натурального числа. Например, если
введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def count_even(num):
    last_digit = num % 10
    if num == 0:
        return 0
    if last_digit % 2 == 0:
        return 1 + count_even((num - last_digit) / 10)
    return count_even((num - last_digit) / 10)


def count_odd(num):
    last_digit = num % 10
    if num == 0:
        return 0
    if last_digit % 2 == 1:
        return 1 + count_odd((num - last_digit) / 10)
    return count_odd((num - last_digit) / 10)


number = int(input("Введите натуральное число: "))
even = count_even(number)
odd = count_odd(number)
print(
f"""У числа {number}:
Количество чётных цифр = {even}
Количество нечётных цифр = {odd}""")
