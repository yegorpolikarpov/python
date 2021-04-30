"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32
и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять
пар "код-символ" в каждой строке.
"""


FIRST_CODE = 32
LAST_CODE = 127
i = 0
OUTPUT_STR = ""
while (FIRST_CODE + i) != LAST_CODE + 1:
    CURRENT_CODE = FIRST_CODE + i
    if CURRENT_CODE < 100:
        OUTPUT_STR += f"{CURRENT_CODE}-{chr(CURRENT_CODE)}    "
    else:
        OUTPUT_STR += f"{CURRENT_CODE}-{chr(CURRENT_CODE)}   "
    i += 1
    if i % 10 == 0:
        OUTPUT_STR += '\n'

print(OUTPUT_STR)
