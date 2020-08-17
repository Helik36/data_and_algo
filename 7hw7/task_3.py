"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
import  random
import statistics


m = int(input("Введите число: "))

def gnome(data): # принимается массив
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    center = len(data) // 2

    return print(f'Отсортированный список {data}. \nМедиана с помощью гномья метода: {data[center]}')


new_lst = [random.randint(1, 51) for i in range(1, (2 * m + 1) + 1)]
print(new_lst)
print(gnome(new_lst))

print(f'Встренная функция: {statistics.median(new_lst)}')