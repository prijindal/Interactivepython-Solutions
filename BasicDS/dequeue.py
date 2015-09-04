class Dequeue :
    def __init__(self):
        self.list = []

    def addFront(self, item):
        self.list.insert(item, 0)

    def addBack(self, item):
        self.list.append(item)

    def removeFront(self):
        return self.list.pop(0)

    def removeBack(self):
        return self.list.pop()

    def size(self):
        return len(self.list)

    def isEmpty(self):
        return self.list == []
