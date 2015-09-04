import random
import timeit

class Hashing:
    def __init__(self):
        self.length = 1001
        self.list = [None]* self.length

    def put(self, item):
        hashed = self.hashfunction(item)
        if self.list[hashed]:
            increment = 1
            newhash = self.rehash(hashed, increment)
            while self.list[newhash]!=None and newhash!=hashed:
                increment+=1
                newhash = self.rehash(newhash, increment)
            self.list[newhash] = item
        else:
            self.list[hashed] = item

    def get(self, item):
        hashed = self.hashfunction(item)
        if self.list[hashed] == item:
            return True
        else:
            increment = 1
            newhash = self.rehash(hashed, increment)
            while newhash!=hashed:
                if self.list[newhash] == item:
                    return True
                increment+=1
                newhash = self.rehash(newhash, increment)
            return False

    def hashfunction(self, item):
        return item%self.length

    def rehash(self, hashed, increment):
        return (hashed + increment*increment)%self.length

H = Hashing()
for i in range(1000):
    H.put(random.randint(0, 10000000))

print(timeit.timeit('H.get(101)', setup="from __main__ import H", number=10000))
