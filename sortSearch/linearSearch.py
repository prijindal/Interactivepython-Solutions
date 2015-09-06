import random
import timeit

def linearSearch(numList, item):
    for i in numList:
        if i == item:
            return True
    return False

L = [random.randint(0, 10000) for i in range(10000)]
print(timeit.timeit('linearSearch(L, 556)', setup="from __main__ import linearSearch, L", number=10000))
