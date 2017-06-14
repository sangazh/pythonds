# 1.13
class Fraction:
    def __init__(self, top, bottom):
        try:
            if type(top) is not int:
                raise RuntimeError("Error: Top of Fraction should be integer")

            if type(bottom) is not int:
                raise RuntimeError("Error: Bottom of Fraction should be integer")
        except Exception as e:
            exit(e)

        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num == second_num

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __gt__(self, other):
        return self.num * other.den > self.den * other.num

    def __ge__(self, other):
        return self.num * other.den >= self.den * other.num

    def __lt__(self, other):
        return self.num * other.den < self.den * other.num

    def __le__(self, other):
        return self.num * other.den <= self.den * other.num

    def __ne__(self, other):
        return self.num * other.den != self.den * other.num

    def __repr__(self) -> str:
        return 'Fraction(%s, %s)' % (self.num, self.den)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den


def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn =
        m = oldn
        n = oldm % oldn
    return n


f1 = Fraction(3, 5)
print(f1)

print("I ate", f1, "of the pizza")

f2 = Fraction(1, 5)
a = f1 + f2
print(a)

f4 = Fraction(6, 10)
print(f4 == f1)

f3 = Fraction(2, -10)
print(f3)

f2 += f1
print(f2)

print(repr(f1))
