"""
Определить, какое число в массиве встречается чаще всего.
"""


import random


MIN_INT = 0
MAX_INT = 10
SIZE = 20
arr = [random.randint(MIN_INT, MAX_INT) for _ in range(SIZE)]
print(arr)

count_dict = {}
for number in arr:
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

# print(count_dict)

max_count = 1
max_count_number = arr[0]
for number in count_dict:
    if count_dict[number] > max_count:
        max_count = count_dict[number]
        max_count_number = number

print(f"Число {max_count_number} встречается чаще всего: {max_count} раз.")
