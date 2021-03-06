"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""

from collections import defaultdict, namedtuple

var = int(input("Введите количество предприятий для расчета прибыли: "))
new_dict = defaultdict(str)

for i in range(1, var + 1):
    new_dict[f'Компания {i}'] = input("Введите название компании: ")
    new_dict[f'Прибыль компании {i}'] = input(
        "Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4): ").split()


all_midle_cash = 0.0  # прибыль всех компаний
max_cash_comp = ''  # у кого больше средней
min_cash_comp = ''  # у кого меньше средней

for i in range(1, var + 1):
    new_dict.update({f'Сумма прибыли {i}': int(0)})
    for j in new_dict[f'Прибыль компании {i}']:
        all_midle_cash += int(j)
        new_dict[f'Сумма прибыли {i}'] += int(j)

all_midle_cash = all_midle_cash // var

for i in range(1, var + 1):
    if int(new_dict[f'Сумма прибыли {i}']) > all_midle_cash:
        max_cash_comp += new_dict[f'Компания {i}'] + " "
    if int(new_dict[f'Сумма прибыли {i}']) < all_midle_cash:
        min_cash_comp += new_dict[f'Компания {i}'] + " "

print(f'Средняя прибыль для всех компаний: {all_midle_cash}')
print(f'Компании, у которых значение больше среднего: {max_cash_comp}')
print(f'Компании, у которых значение меньше среднего: {min_cash_comp}')

print(new_dict)
