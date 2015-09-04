from stack import Stack

def check_balanced(text):
    S = Stack()
    for i in text:
        if i == '(':
            S.push(i)
        elif i == ')':
            if not S.isEmpty():
                S.pop()
            else:
                return False
    if not S.isEmpty():
        return False
    else:
        return True

print(check_balanced('()'))