"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return print(f'Отсортированный: {lst_obj}')


orig_list = [random.randint(-100, 100) for _ in range(50)]
print(f'Исходный массив: {orig_list}')

print('Замер первой функции: ', timeit.timeit("bubble_sort(orig_list)", \
                    setup="from __main__ import bubble_sort, orig_list", number=1))

print('\n')
# Вторая функцияй
def bubble_sort2(lst_obj):
    for i in range(n-1):
        for j in range(n-i-1):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
    return print(f'Отсортированный: {lst_obj}')

n = 50
orig_list = [random.randint(-100, 100) for _ in range(n)]

print(f'Исходный массив 2: {orig_list}')

print('Замер второй функции: ', timeit.timeit("bubble_sort2(orig_list)", \
                    setup="from __main__ import bubble_sort2, orig_list", number=1))

"""
После того, как решил вторую функцию сделать не через проверку, а через два цикла,
второй метод стал работать быстрее.

Замер первой функции:  0.0004598999999999992
Замер второй функции:  0.00028099999999999653
"""