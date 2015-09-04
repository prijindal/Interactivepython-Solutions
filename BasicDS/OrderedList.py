class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def setData(self, newdata):
        self.data = initdata

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, newnext):
        self.next = newnext

class List:

    def __init__(self):
        self.head = None

    def add(self, item):
        pass

    def remove(self, item):
        previous = self.head
        current = previous.getNext()
        if previous.getData() == item :
            self.head = current
        while current!=None:
            if current.getData() == item:
                previous.setNext(current.getNext())
            previous = current
            current = current.getNext()



    def search(self, item):
        pass

    def isEmpty(self, item):
        return self.head == None

    def size(self):
        pass

    def index(self, item):
        pass

    def pop(self, pos=0):
        pass
L = List()
L.add(50)
