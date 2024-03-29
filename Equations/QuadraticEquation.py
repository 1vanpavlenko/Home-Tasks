from Equation import Equation


class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        self.a = a
        super().__init__(b, c)

    def __str__(self):
        return f'{self.a}x^2 + {super().__str__()}'

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def solve(self):
        if self.a == 0:
            return super().solve()

        else:
            discriminant = self.discriminant()

            if discriminant < 0:
                return ()

            elif discriminant == 0:
                return (-self.b / (2 * self.a),)

            else:
                return ((-self.b + discriminant ** 0.5) / (2 * self.a),
                        (-self.b - discriminant ** 0.5) / (2 * self.a))


if __name__ == '__main__':
    e = QuadraticEquation(0, 0, 1)
    e.show()
    print(e.solve())

    e = QuadraticEquation(0, 0, 0)
    e.show()
    print(e.solve())

    e = QuadraticEquation(0, 4, 0)
    e.show()
    print(e.solve())

    e = QuadraticEquation(0, 3, 5)
    e.show()
    print(e.solve())

    e = QuadraticEquation(5, -2, 10)
    e.show()
    print(e.solve())

    e = QuadraticEquation(1, 2, 1)
    e.show()
    print(e.solve())

    e = QuadraticEquation(2, 3, -2)
    e.show()
    print(e.solve())

    e = QuadraticEquation(1, -4, 3)
    e.show()
    print(e.solve())
