from stack import Stack


def infix_to_postfix(infix_expr):
    operand_l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    operand_n = "1234567890"

    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }
    op_stack = Stack()
    expr_list = infix_expr.split()
    output = []

    for token in expr_list:
        if token in operand_l or token in operand_n:
            output.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                output.append(top_token)
                top_token = op_stack.pop()
        else:  # token is operator
            while (not op_stack.is_empty()) and \
                    (prec[op_stack.peek()] >= prec[token]):
                op_stack.push(token)
    while not op_stack.is_empty():
        expr_list.append(op_stack.pop())
    return ' '.join(output)


a = "A * B + C * D"
print(infix_to_postfix(a))
