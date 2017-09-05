class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def rev_string(my_str):
    lst = list(my_str)

    s = Stack()
    for i in range(len(my_str)):
        s.push(lst[i])

    rev = []
    for i in range(len(my_str)):
        rev.append(s.pop())

    rev = ''.join(rev)
    return rev


def matches(o, close):
    opens = "([{"
    closers = ")]}"
    return opens.startswith(o) == closers.startswith(close)


def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False


def main0():
    s = Stack()
    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())


def main():
    print(rev_string('abcde'))


def main1():
    print(par_checker('(()())'))
    print(par_checker('(())'))
    print(par_checker('())'))
    print(par_checker('(()'))
    print(par_checker('{{([][])}()}'))
    print(par_checker('{{([][])}()}'))
    print(par_checker('[{()]'))
