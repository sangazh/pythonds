input="""4
20
"""
data = input.split()
N = data.pop(0)

def trial_division(n):
    if n < 2:
        return []
    prime_factors = []
    sieve = prime_sieve(n)

    for p in sieve:
        if p * p > n:
            break
        while n % p == 0:
            prime_factors.append(p)
            n //= p

    if n > 1:
        prime_factors.append(n)
    return list(set(prime_factors))

# n means length of prime list is n
def prime_sieve(n):
    result = [2,3]
    i = 10
    lst = []
    while n > len(result):
        result = sieve_helper(i, lst, result)
        i += 10
        lst = result
        print(result)

    return result


def sieve_helper(n, lst, factor):
    if lst == []:
        lst = list(range(2, n))

    for i in range(0, int(n**0.5)):
        if lst != [] and lst[0] not in factor:
            factor.append(lst[0])
        lst = [x for x in lst if x % lst[0] != 0]
    return factor


def prime_list(n):
    primes = [2, 3]
    i = 4
    if n <= len(primes):
        return primes[n-1]

    while n != len(primes):
        if i % 2 == 0 or i % 3 == 0:
            i += 1
            continue

        if i < 10:
            primes.append(i)
            i += 1
            continue

        sqrt = n**0.5
        for p in primes[2:]:
            if p > sqrt:
                if i % p == 0:
                    break
                if i not in primes:
                    primes.append(i)
        i += 1
    print(primes)
    return primes[-1]

def primes(n):
    if n < 2:
        return 2
    primes = prime_sieve(n)
    print(primes)
    if n <= len(primes):
        return primes[n-1]

    print(n, len(primes))
    exit()


    i = 1
    while n > len(primes):
        b = int((10 * i/10) * n)
        primes += prime_sieve(a, b)
        i += 1
        a = b
        print(n, len(primes))

    return primes[n-1]


for i in data:
    # print(primes(int(i)), end=' ')
    # a = 10
    print(prime_sieve(30))


