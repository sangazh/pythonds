from stack import Stack


def divide_by2(decimal):
    rem_stack = Stack()

    while decimal > 0:
        rem = decimal % 2
        rem_stack.push(rem)
        decimal = decimal // 2

    binary = ''
    while not rem_stack.is_empty():
        binary = binary + str(rem_stack.pop())

    return binary


def base_converter(decimal, base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()

    while decimal > 0:
        rem = decimal % base
        rem_stack.push(rem)
        decimal = decimal // base

    new_string = ''
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string


def main():
    print(divide_by2(42))
    print(divide_by2(233))


def main1():
    print(base_converter(25, 2))
    print(base_converter(31, 16))
    print(base_converter(25, 8))
    print(base_converter(256, 16))
    print(base_converter(26, 26))


main1()
