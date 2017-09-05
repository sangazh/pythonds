def listSum(numList):
    theSum = 0
    for i in numList:
        theSum += i
    return theSum

def listSum2(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSum2(numList[1:])

# a = [1,3,5,7,9]
# print(listSum(a))
# print(listSum2(a))


def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]

# print(toStr(1453, 16))

def reverse(aString):
    if len(aString) <= 1:
        return aString
    return reverse(aString[1:]) + aString[:1]

# print(reverse('abcd'))

def removeWhite(s):
    if s == '':
        return ''
    if s[0].lower() in 'abcdefghijklmnopqrtsuvwzxyz':
        return s[0] + removeWhite(s[1:])
    else:
        return removeWhite(s[1:])

def isPal(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return isPal(s[1:-1])
    else:
        return False

# print(isPal('hello'))


def recDC(coinValueList, change, knownResults):
    print(change, knownResults)
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i, knownResults)
            print(minCoins, numCoins)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins

# print(recDC([1, 5, 10, 25], 63, [0] *64))

def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found

testlist = [1,2,32,8,17,19,42,13,0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))

