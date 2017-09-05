# 2.4 An Anagram Detection Example
# example


def anagram_solution(string1, string2):
    if len(string1) != len(string2):
        return False

    list2 = list(string2)
    list1 = list(string1)

    for i in range(0, len(string1)):
        if list2[i] not in string1:
            return False

    for i in range(0, len(string1)):
        if list1[i] not in string2:
            return False

    return True


def main():
    s1 = 'apple'
    s2 = 'pleap'
    print(anagram_solution(s1, s2))


main()
