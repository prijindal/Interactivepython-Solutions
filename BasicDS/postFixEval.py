from stack import Stack

def evalPostfix(text):
    S = Stack()
    for i in text:
        if i not in '+-*/':
            S.push(int(i))
        else:
            A = S.pop()
            B = S.pop()
            if i == '+':
                S.push(A+B)
            elif i == '-':
                S.push(A-B)
            elif i == '*':
                S.push(A*B)
            elif i == '/':
                S.push(A/B)    
            else:
                print('Invalid Operator')

    return S.pop()

print(evalPostfix('123*+4+'))