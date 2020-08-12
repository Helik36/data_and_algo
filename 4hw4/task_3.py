"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
import timeit

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def main():
    var_str = 54321
    var_rev =  revers(var_str, 0)
    var_rev2 = revers_2(var_str, 0)
    var_rev3 = revers_3(var_str)

cProfile.run('main()')
print(timeit.timeit("revers", setup="from __main__ import revers", number=10000))
print(timeit.timeit("revers_2", setup="from __main__ import revers_2", number=10000))
print(timeit.timeit("revers_3", setup="from __main__ import revers_3", number=10000))

"Вывод: 3 функция считается самой быстрой. После неё идёт вторая и самая медленная - первая. " \
"Третья функция быстрее т.к нет никаих циклов, просто конвертация."