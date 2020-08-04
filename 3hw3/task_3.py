"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а

"""

import hashlib

string = input("Введите строку: ")

sum_str = set()

for i in range(len(string)):
    for j in range(len(string), i, -1):
        hast_str = hashlib.sha256(string[i:j].encode()).hexdigest()
        sum_str.add(hast_str)
print(f'{len(sum_str) -1} различных подсрок в строке {string}')