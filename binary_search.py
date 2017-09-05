import math
input="""8
13.60591678 0.40760636 558.76042440 8.53157683
"""
data = input.splitlines()
N = data.pop(0)

def cal(x):
    return A * x + B * math.sqrt(x ** 3) - C * math.exp(-x / 50) - D

def binary_search(A, B, C, D):
    start = 0
    end = 100
    target = 0

    while True:
        start, end, x, fx = helper(start, end, target)
        print(start, end, x, fx)
        if abs(fx - target) < 0.0000001:
            break

    return round(x, 10)


def helper(start, end, f_final):
    f_start = cal(start)
    f_end = cal(end)
    middle = float((start + end) / 2)

    f_middle = cal(middle)
    if f_middle < f_start or f_middle > f_end:
        return False;

    if f_final > f_middle:
        start = middle
    elif f_final < f_middle:
        end = middle

    return start, end, middle, f_middle



for line in data:
    test = line.split()
    A = float(test[0])
    B = float(test[1])
    C = float(test[2])
    D = float(test[2])
    print(binary_search(A, B, C,D), end=' ')

