"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""
class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

class BoardTask:
    def __init__(self):
        self.bas_queue = QueueClass() # Базовая очередь
        self.revis_queue = QueueClass() # Очередь на доработку
        self.relz = [] # Решённые

    def to_basic_queue(self, item): # Добавляем задачу в текущие
        self.bas_queue.to_queue(item)

    def basic_task(self): # Текущая задача
        return self.bas_queue.elems[len(self.bas_queue.elems) - 1]

    def to_revis_task(self):  # Отправляем текущую задачу на доработку
        task = self.bas_queue.from_queue()
        self.revis_queue.to_queue(task)

    def resovle_task(self): # Закрываем текущую задачу и добавляем в решённые
        task = self.bas_queue.from_queue()
        self.relz.append(task)

    def from_revis(self): # Возвращаем задачу из доработки в текущую очередь
        task = self.revis_queue.from_queue()
        self.bas_queue.to_queue(task)

    def bas_revis(self): # Задача в доработке:
        return self.revis_queue.elems[len(self.revis_queue.elems) - 1]

if __name__ == '__main__':
    bt = BoardTask()
    bt.to_basic_queue('task1')
    bt.to_basic_queue('task2')
    bt.to_basic_queue('task3')
    print(bt.bas_queue.elems) # Смотрим наши задачи
    print(bt.basic_task())
    bt.to_revis_task()
    bt.resovle_task()
    bt.from_revis()
    print(bt.bas_queue.elems)
    print(bt.basic_task())
    print("Решённый: ", bt.relz)

