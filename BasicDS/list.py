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

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def search(self, item):
        temp = self.head
        while temp!= None:
            if temp.getData() == item:
                return True
            temp = temp.getNext()
        return False

    def size(self):
        temp = self.head
        i = 0
        while temp!= None:
            i+=1
            temp = temp.getNext()
        return i

    def append(self, item):
        temp = self.head
        while temp.getNext()!= None:
            temp = temp.getNext()
        newItem = Node(item)
        temp.setNext(newItem)


    def index(self, item):
        temp = self.head
        i = 0
        while temp!= None:
            if(temp.getData() == item):
                return i
            i+=1
            temp = temp.getNext()
        return -1

    def popFirst(self):
        temp = self.head
        self.head = temp.getNext()
        return temp.getData()

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

    def insert(self, pos, item):
        previous = None
        current = self.head
        i = 0
        if pos==0:
            self.add(item)
            return
        elif pos==self.size():
            self.append(item)
        while current!=None:
            if i==pos:
                temp = Node(item)
                previous.setNext(temp)
                temp.setNext(current)
            previous = current
            current = current.getNext()
            i+=1

    def pop(self, pos=0):
        previous = None
        current = self.head
        i = 0
        if pos==0:
            return self.popFirst()
        while current!=None:
            if i==pos:
                previous.setNext(current.getNext())
                return current.getData()
            previous = current
            current = current.getNext()
            i+=1

L = List()
L.add(50)
L.add(24)
L.add(12)
L.insert(3, 100)
print(L.index(12))
print(L.index(24))
print(L.index(50))
print(L.index(100))
print(L.pop(0))

print(L.index(12))
print(L.index(24))
