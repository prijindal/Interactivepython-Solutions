from stack import Stack

def infixToPostfix(text):
    S = Stack()
    answer = []
    operands = 'qwertyuiopasdfghjklzxcvbnm'.upper()
    operators = '/*+-'
    precedence = {
            '+':0,
            '-':0,
            '*':1,
            '/':1
        }
    for i in text:
        print(i)
        if i in operands:
            answer.append(i)
        elif i == '(':
            S.push(i)
        elif i == ')':
            while S.peek() != '(':
                answer.append(S.pop())
            S.pop()
        elif i in operators:
            if not S.isEmpty() and S.peek()!='(':
                if precedence[i] < precedence[S.peek()]:
                    answer.append(S.pop())
            S.push(i)

        print(S.list)
        print(answer)
        print('')

    while not S.isEmpty():
        answer.append(S.pop())
    return ''.join(answer)

print(infixToPostfix('(A + B) * C - (D - E) * (F + G)'))