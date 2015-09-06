import random
import timeit

def binarySearch(numList, item):
    start = 0
    last = len(numList)
    while start<last:
        mid = (start+last)//2
        if numList[mid] < item:
            start = mid+1
        elif numList[mid] > item:
            last = mid
        else:
            return True
    return False

L = [random.randint(0, 10000) for i in range(10000)]
print(timeit.timeit('binarySearch(L, 556)', setup="from __main__ import binarySearch, L", number=10000))
