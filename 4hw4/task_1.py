"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_arr = []
    i = 0
    for el in nums:
        if el % 2 == 0:
            new_arr.append(i)
            i += 1
    return new_arr

nums = [i for i in range(1, 100)]

print(timeit.timeit(f"func_1({nums})", setup="from __main__ import func_1", number=1000))
print(timeit.timeit(f"func_2({nums})", setup="from __main__ import func_2", number=1000))
"В новой функции использовал последовательный перебор, чем по сути должно быть чуть быстрее"