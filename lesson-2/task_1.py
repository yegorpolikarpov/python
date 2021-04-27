"""
Написать программу, которая будет складывать, вычитать, умножать или делить два
числа. Числа и знак операции вводятся пользователем. После выполнения вычисления
программа должна не завершаться, а запрашивать новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака
операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
то программа сообщает ему об ошибке и снова запрашивает знак операции. Также
пользователю нужно сообщать о невозможности деления на ноль, если он ввел 0 в
качестве делителя.
"""


def perform_operation():
    operation = input(
        """Введите операцию ('+', '-', '*', '/')
        Для завершения введите '0': """)
    if operation == '0':
        return True
    if operation == '+':
        print(f"{a} + {b} = {a + b}")
    elif operation == '-':
        print(f"{a} - {b} = {a - b}")
    elif operation == '*':
        print(f"{a} * {b} = {a * b}")
    elif operation == '/':
        if b == 0:
            print("Делитель не должен быть равен 0")
            return False
        print(f"{a} / {b} = {a / b}")
    else:
        print("Вы ввели неверный знак операции")
        perform_operation()
    return False


while True:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    EXIT_CONDITION = perform_operation()
    if EXIT_CONDITION:
        break
