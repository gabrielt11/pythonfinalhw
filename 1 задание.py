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
        self.stack = []

    def new_task(self, s, n):
        tpr = (s, n)
        if tpr not in self.stack:
            self.stack.append(tpr)

    def del_task(self):
        del (self.stack[-1])

    def priority_task(self):
        res = []
        l = []
        if len(self.stack) > 0:
            for i in range(len(self.stack)):
                res.append(self.stack[i][1])
        res.sort()
        resl = list(set(res))
        for i in range(len(resl)):
            for k in range(len(self.stack)):
                if resl[i] == self.stack[k][1]:
                    tpf = (self.stack[k][0], resl[i])
                    l.append(tpf)
        for i in range(len(l)):
            print(l[i][1], l[i][0])


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print('Результат:')
manager.priority_task()
