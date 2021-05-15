"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для
каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования
предприятий, чья прибыль ниже среднего.
"""

import collections


number_of_industries = int(input('Введите количество предприятий: '))
industries = collections.defaultdict(int)

total_income = 0
for i in range(number_of_industries):
    industry_name = input(f'Введите наименование предприятия №{i + 1}: \n')
    prompt = 'Введите прибыль за 4 квартала (через запятую). Пример ввода: "100,200,300,400" \n'
    annual_income = sum(int(j) for j in input(prompt).split(','))
    industries[industry_name] = annual_income
    total_income += annual_income

average_annual_income = total_income/number_of_industries
print(f'Средняя прибыль за год для всех предприятий: {average_annual_income}')
lower_than_avg = ''
higher_than_avg = ''
for industry_name in industries:
    if industries[industry_name] < average_annual_income:
        lower_than_avg += industry_name + '\n'
    else:
        higher_than_avg += industry_name + '\n'

print('Предприятия с прибылью ниже среднего: \n',
      lower_than_avg,
      'Предприятия с прибылью выше среднего: \n',
      higher_than_avg, sep='')


# Вариант без использования модуля collections

number_of_industries = int(input('Введите количество предприятий: '))
industrial_data = {}

for i in range(number_of_industries):
    industry = input(f'Название предприятия №{i+1}: ')

    promt = 'Введите прибыль за 4 квартала через запятую. Пример ввода: "100,200,300,400" \n'
    quarterly_income = tuple(int(income) for income in input(promt).split(','))
    annual_income = sum(quarterly_income)
    industrial_data[industry] = {'Прибыль поквартально': quarterly_income,
                                 'Прибыль за год': annual_income}

avg_annual_income = 0
for industry in industrial_data:
    avg_annual_income += industrial_data[industry]['Прибыль за год']
avg_annual_income /= number_of_industries

below_avg_income = []
above_avg_income = []
for industry in industrial_data:
    if industrial_data[industry]['Прибыль за год'] < avg_annual_income:
        below_avg_income.append(industry)
    else:
        above_avg_income.append(industry)

print(f'Средняя прибыль за год для всех предприятий составила {avg_annual_income}')
print(f'Наименования предприятий с прибылью ниже среднего: ')
print(', '.join(below_avg_income))
print(f'Наименования предприятий с прибылью выше среднего: ')
print(', '.join(above_avg_income))
