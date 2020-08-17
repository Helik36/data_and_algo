"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import profile


# Первое код, решение 1
@profile()
def my_func2(var_1, var_2):
    print(f"Решение 1: {var_1} ** {var_2} =", var_1 ** var_2)
    var_3 = var_1
    for i in range(abs(var_2) - 1):
        var_3 *= var_1
    print(var_3)
    var_3 = 1 / var_3
    print("Решение 2:", var_3)


a = int(input("Укажи целое положительно число: "))
b = int(input("Укажи целое отрицательно число: "))

my_func2(a, b)

# Первое код, решение 2
@profile()
def my_func2(var_1, var_2):
    print(f"Решение 1: {var_1} ** {var_2} =", var_1 ** var_2)
    var_3 = var_1
    mylist = (var_3 * var_1 for i in range(abs(var_2) -1))
    var_3 = var_3 ** var_1
    var_3 = 1 / var_3
    print("Решение 2:", var_3)

a = int(input("Укажи целое положительно число: "))
b = int(input("Укажи целое отрицательно число: "))

my_func2(a, b)

"""
Второй код хотел сделать по короче, и часть кода сделал через генератор. Результат показывает,
что память затрачивается одинаково

Line #    Mem usage    Increment   Line Contents
================================================
    20     13.1 MiB     13.1 MiB   @profile()
    21                             def my_func2(var_1, var_2):
    22     13.2 MiB      0.0 MiB       print(f"Решение 1: {var_1} ** {var_2} =", var_1 ** var_2)
    23     13.2 MiB      0.0 MiB       var_3 = var_1
    24     13.2 MiB      0.0 MiB       for i in range(abs(var_2) - 1):
    25     13.2 MiB      0.0 MiB           var_3 *= var_1
    26     13.2 MiB      0.0 MiB       print(var_3)
    27     13.2 MiB      0.0 MiB       var_3 = 1 / var_3
    28     13.2 MiB      0.0 MiB       print("Решение 2:", var_3)
ф

Line #    Mem usage    Increment   Line Contents
================================================
    37     13.2 MiB     13.2 MiB   @profile()
    38                             def my_func2(var_1, var_2):
    39     13.2 MiB      0.0 MiB       print(f"Решение 1: {var_1} ** {var_2} =", var_1 ** var_2)
    40     13.2 MiB      0.0 MiB       var_3 = var_1
    41     13.2 MiB      0.0 MiB       mylist = (var_3 * var_1 for i in range(abs(var_2) -1))
    42     13.2 MiB      0.0 MiB       var_3 = var_3 ** var_1
    43     13.2 MiB      0.0 MiB       var_3 = 1 / var_3
    44     13.2 MiB      0.0 MiB       print("Решение 2:", var_3)


"""

# Код 2, решение 1
@profile()
def func_sum(numb):
    while numb != 'Q':

        numb = input("Добавляй числа: ").split()
        for i in range(len(numb)):
            if numb[i] == 'q' or numb[i] == 'Q':
                numb = 'Q'
                break
            else:
                m.append(int(numb[i]))
                sum(m)

        print("Получилось: ", sum(m))

    print('Работа завершена')


m = []
numb = None
print("Для выхода, нажмите - 'Q'")

func_sum(numb)

# код 2, решение 2
@profile()
def func_sum(numb, m):
    var3 = True
    while var3 != False:
        numb = input("Добавляй числа: ").split()
        exitgen = (i for i in range(len(numb)) for j in numb[i] if str(numb[i]) == 'q' or str(numb[i]) == 'Q')
        for var1 in exitgen:
            var3 = False
            return print('Выход. Получилось: ', sum(m))
        mylist = (m.append(int(numb[i])) for i in range(len(numb)) for j in numb[i] if str(numb[i]) != 'q' or str(numb[i]) != 'Q')
        for var in mylist:
            sum(m)
        print('Получилось: ', sum(m))


    print('Получилось: ', sum(m))

print('Работа завершена')

m = []
numb = None
print("Для выхода, нажмите - 'Q'")

func_sum(numb, m)

"""
Первый код кажется более приятным, второй пытался сделать тоже через генераторы, 
однако оба решения по затру помяти - одинаковы

Line #    Mem usage    Increment   Line Contents
================================================
    53     13.2 MiB     13.2 MiB   @profile()
    54                             def func_sum(numb):
    55     13.2 MiB      0.0 MiB       while numb != 'Q':
    56                             
    57     13.2 MiB      0.0 MiB           numb = input("Добавляй числа: ").split()
    58     13.2 MiB      0.0 MiB           for i in range(len(numb)):
    59     13.2 MiB      0.0 MiB               if numb[i] == 'q' or numb[i] == 'Q':
    60     13.2 MiB      0.0 MiB                   numb = 'Q'
    61     13.2 MiB      0.0 MiB                   break
    62                                         else:
    63     13.2 MiB      0.0 MiB                   m.append(int(numb[i]))
    64     13.2 MiB      0.0 MiB                   sum(m)
    65                             
    66     13.2 MiB      0.0 MiB           print("Получилось: ", sum(m))
    67                             
    68     13.2 MiB      0.0 MiB       print('Работа завершена')


Line #    Mem usage    Increment   Line Contents
================================================
    78     13.2 MiB     13.2 MiB   @profile()
    79                             def func_sum(numb, m):
    80     13.2 MiB      0.0 MiB       var3 = True
    81     13.2 MiB      0.0 MiB       while var3 != False:
    82     13.2 MiB      0.0 MiB           numb = input("Добавляй числа: ").split()
    83     13.2 MiB      0.0 MiB           exitgen = (i for i in range(len(numb)) for j in numb[i] if str(numb[i]) == 'q' or str(numb[i]) == 'Q')
    84     13.2 MiB      0.0 MiB           for var1 in exitgen:
    85     13.2 MiB      0.0 MiB               var3 = False
    86     13.2 MiB      0.0 MiB               return print('Выход. Получилось: ', sum(m))
    87     13.2 MiB      0.0 MiB           mylist = (m.append(int(numb[i])) for i in range(len(numb)) for j in numb[i] if str(numb[i]) != 'q' or str(numb[i]) != 'Q')
    88     13.2 MiB      0.0 MiB           for var in mylist:
    89     13.2 MiB      0.0 MiB               sum(m)
    90     13.2 MiB      0.0 MiB           print('Получилось: ', sum(m))
    91                             
    92                             
    93                                 print('Получилось: ', sum(m))


Windows 10 x64
Python 3.8.2
"""