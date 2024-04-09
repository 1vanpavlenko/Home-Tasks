class Integer:
    def __init__(self, a):
        if type(a) is Integer:
            a = a.base
        else:
            a = int(a)
        self.base = a

    def __str__(self):
        return f'{self.base}'

    def __add__(self, other):       # x + y
        if type(other) is not int or type(other) is not float or type(other) is not Integer:
            return NotImplemented
        other = Integer(other)
        return Integer(self.base + other.base)

    __radd__ = __add__

    def __sub__(self, other):       # x - y
        other = Integer(other)
        return Integer(self.base - other.base)

    def __rsub__(self, other):
        other = Integer(other)
        return Integer(other.base - self.base)

    def __mul__(self, other):       # x * y
        other = Integer(other)
        return Integer(self.base * other.base)

    __rmul__ = __mul__

    def __neg__(self):              # -x
        return self * (-1)

    def __pos__(self):              # +x
        return self

    def __pow__(self, power):       # x ** y
        power = Integer(power)
        return Integer(self.base ** power.base)

    def __truediv__(self, other):   # x / y
        other = Integer(other)
        return self.make_rat(self.base, other.base)

    def __rtruediv__(self, other):
        pass

    def __floordiv__(self, other):  # x // y
        other = Integer(other)
        return Integer(self.base // other.base)

    def __mod__(self, other):       # x % y
        other = Integer(other)
        return Integer(self.base % other.base)

    def __eq__(self, other):        # x == y
        other = Integer(other)
        return self.base == other.base

    def __ne__(self, other):        # x != y
        other = Integer(other)
        return self.base != other.base

    def __gt__(self, other):        # x > y
        other = Integer(other)
        return self.base > other.base

    def __ge__(self, other):        # x >= y
        other = Integer(other)
        return self.base >= other.base

    def __lt__(self, other):        # x < y
        other = Integer(other)
        return self.base < other.base

    def __le__(self, other):        # x <= y
        other = Integer(other)
        return self.base <= other.base

    def __abs__(self):              # abs(x)
        return abs(self.base)

    def __int__(self):              # int(x)
        return self.base

    def __float__(self):            # float(x)
        return float(self.base)

    def gcd(self, other):
        a = self
        b = Integer(other)
        if a < b:
            a, b = b, a
        if a < 0:
            a = -a
        if b < 0:
            b = -b
        while b > 0:
            d = a % b
            a = b
            b = d
        return Integer(a)

    @staticmethod
    def is_rat(other):
        from Rational import Rational
        return type(other) is Rational

    @staticmethod
    def make_rat(a, b):
        from Rational import Rational
        return Rational(a, b)

    def invert(self):
        from Rational import Rational
        return Rational(1, self.base)


if __name__ == '__main__':
    t1 = Integer(10)
    t2 = Integer(12.0)
    print(2 - t1)
