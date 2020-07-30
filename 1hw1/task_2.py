"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

import random


# Алгоритм 1


def min_var(vars):
    min = 0
    for i in vars:
        if i >= min:
            min = i
            for j in vars:
                if j <= min:
                    min = j
    return min


c = [c for c in range(1, 31)]

random.shuffle(c)
print(min_var(c))
print(c)


# Алгоритм 2

def min_var2(vars):
    min_var = min(vars)
    return (min_var)


cc = [c for c in range(1, 31)]

random.shuffle(cc)
print(min_var(cc))