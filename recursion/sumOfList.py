def listsum(numList):
    if numList == []:
        return 0
    else:
        return numList[0] + listsum(numList[1:])

print(listsum([1, 2, 3, 4]))
