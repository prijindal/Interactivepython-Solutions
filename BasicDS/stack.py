class Stack:

    def __init__(self):
        self.list = []

    def pop(self):
        return self.list.pop()

    def push(self, item):
        self.list.append(item)

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.list[-1]

    def isEmpty(self):
        return self.list == []

    def size(self):
        return len(self.list)

