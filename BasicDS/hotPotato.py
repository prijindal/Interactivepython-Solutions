from queue import Queue

def hotPotato(list, num):
    Q = Queue()
    for i in list:
        Q.enqueue(i)
    while Q.size() !=1:
        for j in xrange(num):
            Q.enqueue(Q.dequeue())
        Q.dequeue()
    return Q.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))