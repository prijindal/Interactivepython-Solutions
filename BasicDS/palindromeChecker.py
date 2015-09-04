from dequeue import Dequeue

def check_palindrome(text):
    D = Dequeue()
    for i in text:
        D.addBack(i)

    while D.size() > 1:
        if D.removeBack() == D.removeFront():
            return False
    return True

print(check_palindrome('AACBB'))
