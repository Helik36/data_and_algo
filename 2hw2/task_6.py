"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import random

def game(rand_var, chance):
    var = int(input("Введите число от 0 до 100: "))
    if var == rand_var:
        return print("Молодец, ты победил")
    elif chance < 2:
        return print(f"Ты проиграл. Загаднно число: {rand_var}.")
    elif var < 0 or var > 100:
        var = int(input("Введите число от 0 до 100: "))
        return game(rand_var, chance)
    if var > rand_var:
        return print(f"Нужно меньше. Осталось {chance - 1} шансов."), game(rand_var, chance - 1)
    elif var < rand_var:
        return print(f"Нужно больше. Осталось {chance - 1} шансов."), game(rand_var, chance - 1)


rand_var = random.randint(0, 100)
chance = 10

# print(rand_var)

print(game(rand_var, chance))