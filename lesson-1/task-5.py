#  5
#  Пользователь вводит две буквы.
#  Определить, на каких местах алфавита они стоят и сколько между ними
#  находится букв.

print("Введите две буквы: ")
letter1 = ord(input("Первая буква = "))
letter2 = ord(input("Вторая буква = "))

place1 = letter1 - ord('a') + 1
place2 = letter2 - ord('a') + 1
difference = abs(letter2 - letter1) - 1

print(f"""
Буква '{chr(letter1)}' находится на {place1} месте.
Буква '{chr(letter2)}' находится на {place2} месте.
Между ними букв: {difference}
""")
