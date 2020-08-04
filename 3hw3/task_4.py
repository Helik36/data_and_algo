"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from uuid import uuid4
import  hashlib

def hash_url_str(str_url, q):

    in_url = input("0 для выхода. Введите адрес: ")
    if in_url == '0':
        return print(f"Выход \n {str_url}")
    else:
        res = hashlib.sha256(salt.encode() + in_url.encode()).hexdigest()
        print(res)
        if res in str_url:
            print("Такой хэш уже есть")
            return hash_url_str(str_url, q)
        else:
            print(f"Такого хэша нет. Добавил. {str_url.append(res)}")
            return hash_url_str(str_url, q)

str_url = []
salt = uuid4().hex
print(hash_url_str(str_url, salt))
