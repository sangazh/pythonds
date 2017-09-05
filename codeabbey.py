import math
input="""2
10220 6839 84070
1257 114 670143
3 5 4
"""
data = input.splitlines()
N = int(data.pop(0))
precision = 0.0000001

def printers(X, Y, N):
    T = N * X * Y / (X + Y)
    T = math.ceil(T)
    if T % X != 0 or T % Y != 0:
        T1 = T
        m1 = T % X
        m2 = T % Y
        T += min(m1, m2)
        T2 = T
        print(m1, m2, T1, T2)

    # T = 344454880
    N_expect = T / X + T / Y
    print('expect:', N_expect)
    print('T: ', T)
    print('T / X', T/X)
    print('T / Y', T/Y)
    return math.ceil(T)


for line in data:
    number = line.split()
    X = float(number[0])
    Y = float(number[1])
    N = float(number[2])
    print(printers(X, Y, N), end= ' ')
    exit()



