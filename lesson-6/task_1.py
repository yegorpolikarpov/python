"""
 Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
 программах в рамках первых трех уроков. Проанализировать результат и
 определить программы с наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python и разрядность
вашей ОС.
"""

import random
import sys
import collections


def show_and_sum(obj):
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                return sys.getsizeof(obj) \
                + show_and_sum(key) + show_and_sum(value)
        else:
            for item in obj:
                return sys.getsizeof(obj) + show_and_sum(item)
    return sys.getsizeof(obj)


MIN_INT = 0
MAX_INT = 10
SIZE = 20
arr = [random.randint(MIN_INT, MAX_INT) for _ in range(SIZE)]
# [5, 1, 5, 3, 5, 2, 0, 4, 10, 4, 1, 7, 3, 5, 2, 0, 4, 0, 10, 8]
print(arr)
print('Количество памяти для массива в котором нужно найти наибольшее число')
overall_sum = 0
overall_sum += show_and_sum(MIN_INT)
overall_sum += show_and_sum(MAX_INT)
overall_sum += show_and_sum(SIZE)
overall_sum += show_and_sum(arr)
print(f'Общая сумма: {overall_sum}')
print('*'*100)
# python 3.9.0
# 64-разрядная Win10
# Количество памяти для массива в котором нужно найти наибольшее число
# type(obj)=<class 'int'>, sys.getsizeof(obj)=24, obj=0
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=10
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=20
# type(obj)=<class 'list'>, sys.getsizeof(obj)=248, obj=[5, 1, 5, 3, 5, 2, 0, 4, 10, 4, 1, 7, 3, 5, 2, 0, 4, 0, 10, 8]
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=5
# Общая сумма: 356


print('Первый способ')
count_dict = {}
for number in arr:
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

max_count = 1
max_count_number = arr[0]
for number in count_dict:
    if count_dict[number] > max_count:
        max_count = count_dict[number]
        max_count_number = number

# print(f'Число {max_count_number} встречается чаще всего: {max_count} раз.')

overall_sum = 0
overall_sum += show_and_sum(count_dict)
overall_sum += show_and_sum(max_count)
overall_sum += show_and_sum(max_count_number)
print(f'Общая сумма: {overall_sum}')
print('*'*100)
# python 3.9.0
# 64-разрядная Win10
# Первый способ
# type(obj)=<class 'dict'>, sys.getsizeof(obj)=360, obj={5: 4, 1: 2, 3: 2, 2: 2, 0: 3, 4: 3, 10: 2, 7: 1, 8: 1}
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=5
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=4
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=4
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=5
# Общая сумма: 472

print('Второй способ')
counter = collections.Counter(arr)
most_common_number, most_common_number_count = counter.most_common(1)[0]
# print(f'Число {most_common_number} встречается чаще всего:',
#       f'{most_common_number_count} раз.')

overall_sum = 0
overall_sum += show_and_sum(counter)
overall_sum += show_and_sum(most_common_number)
overall_sum += show_and_sum(most_common_number_count)
print(f'Общая сумма: {overall_sum}')
print('*'*100)
# python 3.9.0
# 64-разрядная Win10
# Второй способ
# type(obj)=<class 'collections.Counter'>, sys.getsizeof(obj)=376, obj=Counter({5: 4, 0: 3, 4: 3, 1: 2, 3: 2, 2: 2, 10: 2, 7: 1, 8: 1})
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=5
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=4
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=5
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=4
# Общая сумма: 488

print('Третий способ')
arr.sort()
count = 0
max_count = 0
current_count = 0
most_common_number = arr[0]
for i in range(len(arr)-1):
    current_count += 1
    if arr[i] != arr[i+1]:
        if max_count < current_count:
            max_count = current_count
            most_common_number = arr[i]
        current_count = 0
# print(arr)
# [0, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 6, 7, 7, 8, 8, 9, 9, 10, 10]
# print(f'Число {most_common_number} встречается чаще всего:',
#       f'{max_count} раз.')

overall_sum = 0
overall_sum += show_and_sum(count)
overall_sum += show_and_sum(max_count)
overall_sum += show_and_sum(current_count)
overall_sum += show_and_sum(most_common_number)
print(f'Общая сумма: {overall_sum}')
# python 3.9.0
# 64-разрядная Win10
# Третий способ
# type(obj)=<class 'int'>, sys.getsizeof(obj)=24, obj=0
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=4
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=1
# type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=5
# Общая сумма: 108
