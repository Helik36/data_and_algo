"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def equality(var, var1, s):
    if s != var*(var+1)//2:
        var1= var1 + 1
        s += var1
        return equality(var, var1, s)
    var2 = var*(var+1)//2
    return print(f" 1+2+...+n = n(n+1)/2 \n"
                 f"{s} = {var2}")

var = int(input("Введите целое положительное число: "))
var1 = 1
s = 1
print(equality(var, var1, s))