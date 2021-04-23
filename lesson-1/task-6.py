#  6
#  Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter_number = int(input("Введите номер буквы: "))

letter = chr(ord('a') - 1 + letter_number)
print(f"Буква с номером {letter_number}: '{letter}'")
