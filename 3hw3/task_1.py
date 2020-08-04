"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import time


def t_l(n):
    start_time = time.time()
    res = 0
    for i in range(1, n + 1):
        res = res + i

    new_list = []
    new_list.append('Hello,')
    new_list.append('my')
    new_list.append('name')
    new_list.append('is')
    new_list.append('German')

    end_time = time.time()
    return res, end_time - start_time

print(f'Операция запонления списка заняла {t_l(10000)[1]} сек')

def t_d(n):
    start_time = time.time()
    res = 0
    for i in range(1, n + 1):
        res = res + i

    new_dict = dict()
    new_dict[1] = 'Hello'
    new_dict[2] = 'my'
    new_dict[3] = 'name'
    new_dict[4] = 'is'
    new_dict[5] = 'German'

    end_time = time.time()
    return res, end_time - start_time

print(f'Операция заполнения словаря заняла {t_d(10000)[1]} сек')

if t_l(10000)[1] > t_d(10000)[1]:
    print("Список формируется быстрее")
else:
    print("Словарь формируется быстрее") # В основном у меня формируется быстрее словарь
        # но бывает что и список