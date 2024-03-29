from functions import gcd


class Rational:
    def __init__(self, a: int, b: int):
        assert b != 0

        if gcd(a, b) > 1:
            d = gcd(a, b)
            a //= d
            b //= d

        if a < 0 and b < 0:
            a, b = abs(a), abs(b)

        self._a = a
        self._b = b

    def __str__(self):
        if abs(self._b) == 1:
            return f'{self._b * self._a}'

        return f"{self._a}/{self._b}"

    def show(self):
        print(self)

    def __add__(self, other):
        new_a = self._a * other._b + other._a * self._b
        new_b = self._b * other._b

        return Rational(new_a, new_b)


if __name__ == '__main__':
    while True:
        n, m = [int(i) for i in input().split()]
        r = Rational(n, m)
        r.show()

