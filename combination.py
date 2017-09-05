input="""3
5 3 2
"""
data = input.splitlines()
N = data.pop(0)

sets = '0123456789ABCEDFGHIJKLMNOPQRSTUVWXYZ'

def combination(N, K):
    c = factorial(N) / (factorial(K) * factorial(N - K))
    return int(c)

def comb(N, K, I):
    result = []
    source = sets[0:N]

    print(source)

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


for line in data:
    test = line.split()
    N = int(test[0])
    K = int(test[1])
    I = int(test[2])
    print(comb(N,K,I ), end=' ')
    exit()


