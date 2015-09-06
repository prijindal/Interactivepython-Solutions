import timeit

class Hashing:
    def __init__(self):
        self.length = 26
        self.list = [False] * self.length

    def put(self, item):
        hashed = self.hashfunction(item)
        self.list[hashed] = True

    def get(self, item):
        hashed = self.hashfunction(item)
        return self.list[hashed]

    def hashfunction(self, item):
        return ord(item)%self.length

H = Hashing()
A = 'mcowncwcCqcnqlcwhbauickqcbqickqhu'
for i in A:
    H.put(i)

print(timeit.timeit("H.get('a')", setup='from __main__ import H', number=10000))
