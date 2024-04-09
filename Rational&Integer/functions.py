def gcd(a: int, b: int):
    if b > a:
        a, b = b, a
    if a < 0:
        a = abs(a)
    if b < 0:
        b = abs(b)
    if b == 0:
        return a

    return gcd(b, a % b)


def int_float(n: float):
    return n == int(n)


if __name__ == '__main__':
    print(gcd(-2, 6))
