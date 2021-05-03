import matplotlib.pyplot as plt
import numpy as np
import os

"""
Инструкция по использованию

Установка matplotlib:
python -m pip install -U pip
python -m pip install -U matplotlib

Для использования модуля рисования импортируйте его к себе
from graph import draw

После этого вам необходимо создать два массива одинаковой длины.
х - массив со значениями по оси Х
у - массив со значениями по оси У

В нашем случае х - это количество итераций в цикле выполнения вашей функции
у - это время выполнения функции

Для модуля рисования нужны параметры
to_disk - True или False, если истина, то график сохраняется на диск, если ложь, то отображается на экране
tabel_name - Название таблицы с графиками
[param] - список параметров для рисования графика
    Два первых параметра обязательны, это массив х и массив у
    третий параметр Необязательный - название графика
    четвертый параметр Необязательный - цвет графика

Пример использования (можно скопировать и исполнить у себя)
    x = [1, 10, 20, 30]
    y = [0.0005, 0.0049, 0.0846, 1.458]
    draw(False, "Мой график", [ x, y, "Рекурсия", "red"])

Возможно рисование сразу нескольких графиков в одной таблице, тогда просто повторяем массив с параметрами 
нужное количество раз
Например
    x1 = [1, 10, 20, 30]
    y1 = [0.0005, 0.0049, 0.0846, 1.458]

    x2 = [1, 10, 20, 30]
    y2 = [0.0002, 0.0019, 0.0216, 0.198]

    draw(False, "Мой график", [ x1, y1, "Рекурсия"], [x2, y2, "Перебор"])

"""


def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = './pictures/{}'.format(fmt)
    if not os.path.exists(iPath):
        os.makedirs(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt))
    os.chdir(pwd)
    plt.close()


def draw(to_disk, tabel_name, *args):
    plt.title(tabel_name)  # заголовок
    plt.xlabel("Количество элементов")  # ось абсцисс
    plt.ylabel("Время выполнения")  # ось ординат
    plt.grid()      # включение отображение сетки
    color_array = ["b", "g", "r", "c", "m", "y", "k"]
    i = 1
    for line in args:
        if len(line) < 2:
            raise Exception("Ошибка в параметрах")
        if line[0] is None:
            raise Exception("Ошибка в параметрах")
        else:
            x = line[0]
        if line[1] is None:
            raise Exception("Ошибка в параметрах")
        else:
            y = line[1]
        if len(line) < 3:
            line_name = f'Функция {i}'
        else:
            line_name = line[2]
        if len(line) < 4:
            color = color_array[i % 7]
        else:
            color = line[3]
        plt.plot(x, y, label=line_name, c=color)  # построение графика
        i += 1

    plt.legend()
    if to_disk:
        save(name='pic_graph')
    plt.show()
