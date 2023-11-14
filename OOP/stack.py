# Мы уже говорили, что в программировании нередко необходимо
# создавать свои собственные структуры данных на основе уже существующих.
# Одной из таких базовых структур является стек.
#
# Стек — это абстрактный тип данных, представляющий собой список элементов,
# организованных по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).
#
# Простой пример: стек из книг на столе. Единственной книгой,
# обложка которой видна, является самая верхняя. Чтобы получить доступ,
# например, к третьей снизу книге, нам нужно убрать все книги,
# лежащие сверху, одну за другой.
#
# Напишите класс, который реализует стек и его
# возможности (достаточно будет добавления и удаления элемента).
#
# После этого напишите ещё один класс — «Менеджер задач».
# В менеджере задач можно выполнить команду «новая задача»,
# в которую передаётся сама задача (str) и её приоритет (int).
# Сам менеджер работает на основе стека (не наследование).
# При выводе менеджера в консоль все задачи должны быть отсортированы
# по следующему приоритету: чем меньше число, тем выше задача.
#
# Вот пример основной программы:
# manager = TaskManager()
# manager.new_task("сделать уборку", 4)
# manager.new_task("помыть посуду", 4)
# manager.new_task("отдохнуть", 1)
# manager.new_task("поесть", 2)
# manager.new_task("сдать ДЗ", 2)
# print(manager)
#
# Результат:
# 1 — отдохнуть
# 2 — поесть; сдать ДЗ
# 4 — сделать уборку; помыть посуду
# Дополнительно: реализуйте также удаление задач

class Stack:
    def __init__(self):
        self.stack = []

    def add(self, item):
        self.stack.append(item)

    def delete(self, work):
        if len(self.stack) == 0:
            return None
        return self.stack.pop(self.stack.index(work))

    def __str__(self):
        return ', '.join(self.stack)


class TaskManager:
    def __init__(self):
        self.task = dict()

    def new_task(self, work, priority):
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].add(work)

    def delete_task(self, work, priority):
        print(f"Удалили задачу {self.task[priority].delete(work)}")
        if len(str(self.task[priority])) == 0:
            self.task.pop(priority)

    def __str__(self):
        display = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append(f'{str(i_priority)} - {self.task[i_priority]};\n')
        return ''.join(display)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("сдать ДЗ", 2)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)

print(manager)
manager.delete_task("помыть посуду", 4)
print(manager)