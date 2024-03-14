def gcd(a: int, b: int):
    if b > a:
        a, b = b, a

    if b == 0:
        return a

    return gcd(b, a % b)


if __name__ == '__main__':
    print(gcd(5, 5))
    print(gcd(6, 4))
    print(gcd(4, 6))
    print(gcd(10, 0))
    print(gcd(0, 10))
    print(gcd(13, 12))
    print(gcd(12, 13))
