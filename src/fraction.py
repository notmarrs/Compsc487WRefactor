from fractions import Fraction

def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

def int_to_fraction(x):
    if type(x) == int:
        return Fraction(x, 1)
    elif type(x) == Fraction:
        return x
    else:
        raise TypeError("Must be an int/Fraction")

class Fraction:
    def __init__(self, top, bottom):
        cmmn = gcd(top, bottom)
        self.num = top // cmmn
        self.den = bottom // cmmn

    def __str__(self):
        return "{:d}/{:d}".format(self.num, self.den)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num == second_num

    def __add__(self, other_fraction):
        other_fraction = int_to_fraction(other_fraction)
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __sub__(self, other_fraction):
        other_fraction = int_to_fraction(other_fraction)
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __mul__(self, other_fraction):
        other_fraction = int_to_fraction(other_fraction)
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other_fraction):
        other_fraction = int_to_fraction(other_fraction)
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        return Fraction(new_num, new_den)

    def __gt__(self, other_fraction):
        return (self.num * other_fraction.den > other_fraction.num * self.den)

    def __ge__(self, other_fraction):
        return (self.num * other_fraction.den >= other_fraction.num * self.den)

    def __lt__(self, other_fraction):
        return (self.num * other_fraction.den < other_fraction.num * self.den)

    def __le__(self, other_fraction):
        return (self.num * other_fraction.den <= other_fraction.num * self.den)

    def __ne__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num != second_num

    def __repr__(self):
        return self.__str__()

    def __radd__(self, left):
        return self + left

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def show(self):
        print(self.__str__())

x = Fraction(1, 2)
x.show()
y = Fraction(2, 3)
print(y)
assert y == Fraction(2, 3)
print(x + y)
assert x + y == Fraction(7, 6)
print(x == y)

