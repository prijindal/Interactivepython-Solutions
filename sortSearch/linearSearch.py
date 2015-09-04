import random
import timeit

def linearSearch(numList, item):
    for i in numList:
        if i == item:
            return True
    return False

L = [random.randint(0, 10000000) for i in range(1000)]
print(timeit.timeit('linearSearch(L, 101)', setup="from __main__ import linearSearch, L", number=10000))
