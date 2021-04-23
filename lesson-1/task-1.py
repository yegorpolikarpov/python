#  1
#  Найти сумму и произведение цифр трехзначного числа,
#  которое вводит пользователь.

number = input("Введите трёхзначное число: ")

a = int(number[0])
b = int(number[1])
c = int(number[2])
sum = a + b + c
product = a * b * c

print(f"Сумма цифр: {sum}")
print(f"Произведение цифр: {product}")
