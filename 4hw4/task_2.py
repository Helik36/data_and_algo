"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
import timeit


def memorize(func):
    memory = {}
    def memo(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
            return r
    return memo


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

@memorize
def recursive_reverse_memo(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'



var = int(input("Число: "))
print(recursive_reverse(var))

print(timeit.timeit(f"recursive_reverse({var})", setup="from __main__ import recursive_reverse", number=1000))
print(timeit.timeit(f"recursive_reverse_memo({var})", setup="from __main__ import recursive_reverse_memo", number=1000))
"Функция с мемоизоацией работает быстрее"