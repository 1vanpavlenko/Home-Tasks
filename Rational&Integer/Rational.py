from Integer import Integer


class Rational(Integer):
    def __new__(cls, a, b):
        a, b = int(a), int(b)
        assert b != 0
        if a == 0:
            return a
        d = int(Integer(a).gcd(b))
        if d != 1 and abs(b / d) == 1:
            return Integer(a / d)
        return super().__new__(cls)

    def __init__(self, a, b):
        a, b = int(a), int(b)
        if a < 0 and b < 0:
            a, b = -a, -b
        if b < 0:
            a, b = -a, -b
        d = int(Integer(a).gcd(b))
        if d != 1:
            a, b = int(a) / d, int(b) / d
        super().__init__(a)
        self.denominator = b

    def __str__(self):
        return f'{self.base}/{self.denominator}'

    def __add__(self, other):
        if type(other) is Rational:
            new_base = self.base * other.denominator + other.base * self.denominator
            new_denominator = self.denominator * other.denominator
            return Rational(new_base, new_denominator)
        else:
            try:
                other = Integer(other)
            except AssertionError:
                return NotImplemented
            new_base = self.base + other.base * self.denominator
            new_denominator = self.denominator
            return Rational(new_base, new_denominator)

    __radd__ = __add__

    def __int__(self):
        raise TypeError

    def __float__(self):
        return self.base / self.denominator

    def __neg__(self):
        return Rational(-self.base, self.denominator)

    def __pos__(self):
        return Rational(+self.base, self.denominator)

    def invert(self):
        return Rational(self.denominator, self.base)
