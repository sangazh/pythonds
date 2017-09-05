from deque import Deque

def palchecker(aString):
    charDeque = Deque()
    for ch in aString:
        charDeque.addRear(ch)

    stillEqual = True
    while charDeque.size() > 1 and stillEqual:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))