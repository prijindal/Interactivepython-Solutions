from stack import Stack

def check_symbols(text):
    opening = '({['
    closing = ')}]'
    S = Stack()
    for i in text:
        if i in opening:
            S.push(i)
        elif i in closing:
            if not S.isEmpty():
                ch = S.pop()
                if closing.index(i) != opening.index(ch):
                    return False
            else:
                return False
    if not S.isEmpty():
        return False
    else:
        return True

print(check_symbols('{{[[{{[{[(({[(())]}))]}]}}]]}}'))