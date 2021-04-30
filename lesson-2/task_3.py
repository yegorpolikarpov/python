"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и
вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
"""


def reverse_digits(num):
    last_digit = num % 10
    if num == 0:
        return ""
    return f"{last_digit}" + f"{reverse_digits((num - last_digit) // 10)}"


number = int(input("Введите натуральное число: "))
reversed_number = reverse_digits(number)
print(reversed_number)
