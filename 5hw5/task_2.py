"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] = 162 и [‘C’, ‘4’, ‘F’]=3151
 соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’] = 3313, произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’] = 510462.
13075
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

from collections import deque

print(int('B', 16)) # Перевод в обычное число

def mus(var):
    st = ''
    for i in var:
        st = st + i
    return st

def dec_to_base(N, base): # Переводит число в 16ю систему
    if not hasattr(dec_to_base, 'table'):
        dec_to_base.table = '0123456789ABCDEF'
    x, y = divmod(N, base)
    return dec_to_base(x, base) + dec_to_base.table[y] if x else dec_to_base.table[y]

var1 = deque(input("Введите шестнадцатеричное число: "))
var2 = deque(input("Введите второе шестнадцатеричное число: "))

print(f"числа - {var1, var2}")

print(f"Сложение = {int(mus(var1), 16) + int(mus(var2), 16)}")
print(f"Умноежние = {int(mus(var1), 16) * int(mus(var2), 16)}")

deq_var1 = int(mus(var1),16) + int(mus(var2),16)
deq_var2 = int(mus(var1), 16) * int(mus(var2), 16)
print(deque(dec_to_base(deq_var1, 16)))
print(deque(dec_to_base(deq_var2, 16)))
