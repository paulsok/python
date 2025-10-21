# Базовый цикл событий мог бы выглядеть следующим образом:
# Данный код — всего лишь условность, реальный цикл событий будет выглядеть куда длиннее и запутаннее.
class SimpleEventLoop:
    def __init__(self):
        self.tasks = []               # Очередь задач

    def add_task(self, task):
        self.tasks.append(task)       # Добавление задачи в очередь

    def run_forever(self):
        while self.tasks:             # Выполнять, пока есть задачи
            task = self.tasks.pop(0)  # Получить первую задачу
            task()                    # Выполнить задачу


def task1():
    print("Выполняется задача 1")


def task2():
    print("Выполняется задача 2")


loop = SimpleEventLoop()
loop.add_task(task1)  # Добавить задачу 1 в цикл событий
loop.add_task(task2)  # Добавить задачу 2 в цикл событий
loop.run_forever()    # Запустить цикл событий