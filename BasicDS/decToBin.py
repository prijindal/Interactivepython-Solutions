from stack import Stack

def convert(num, base = 2):
    S = Stack()
    new = []
    while num > 0:
        S.push(str(num%base))
        num = num//base
    while not S.isEmpty():
        new.append(S.pop())
    return ''.join(new)

print(convert(100, 8))