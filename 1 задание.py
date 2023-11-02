# 1 задание
class Lifo:
    def __init__(self):
        self.stack = []

    def add_elem(self, n):
        self.stack.append(n)

    def del_elem(self):
        del (self.stack[-1])

    def result(self):
        return self.stack


class TaskManager:
    def __init__(self):
        self.stack = {}

    def new_task(self, task, priority):
        if priority in self.stack.keys():
            self.stack[priority].append(task)
        else:
            self.stack[priority] = task.split(',')

    def del_task(self):
        self.stack.popitem()

    def priority_task(self):
        keys = self.stack.keys()
        sorted_keys = sorted(keys)
        for i in range(len(sorted_keys)):
            print(sorted_keys[i], '; '.join(self.stack[sorted_keys[i]]))


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print('Результат:')
manager.priority_task()
