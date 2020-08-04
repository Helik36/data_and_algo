"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""
from uuid import uuid4   # соль-часть хэша
import hashlib

psw = input("Введите пароль: ")

salt = uuid4().hex
res = hashlib.sha256(salt.encode() + psw.encode()).hexdigest()
print(res)
psw_rep = input("Введите пароль повторно: ")
res_rep = hashlib.sha256(salt.encode() + psw_rep.encode()).hexdigest()
if res == res_rep:
    print('Доступ разрешён!')
else:
    print("Пароли не совпадают!!!")


#hash_object = hashlib.sha256(psw.encode())
# print(hash_object.hexdigest())
#hex_dig_res = hash_object.hexdigest()
# print(hex_dig_res)