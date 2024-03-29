class Equation:
    def __init__(self, b: int, c: int):
        self.b = b
        self.c = c

    def __str__(self):
        return f'{self.b}x + {self.c} = 0'

    def show(self):
        print(self)

    INF = "infinity"

    def solve(self):
        if self.b == 0:
            if self.c == 0:
                return Equation.INF

            else:
                return ()

        else:
            return (-self.c / self.b,)


if __name__ == '__main__':
    e = Equation(0, 1)
    e.show()
    print(e.solve())

    e = Equation(0, 0)
    e.show()
    print(e.solve())

    e = Equation(4, 0)
    e.show()
    print(e.solve())

    e = Equation(3, 5)
    e.show()
    print(e.solve())

