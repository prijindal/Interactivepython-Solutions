def intToString(number, base=10):
    convertString = '0123456789ABCDEF'
    if number/base == 0:
        return convertString[number%base]
    else:
        return intToString(number/base, base) + convertString[number%base]

print(intToString(10, 2))
