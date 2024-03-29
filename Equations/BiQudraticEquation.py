from QuadraticEquation import QuadraticEquation


class BiQuadraticEquation(QuadraticEquation):
    def __str__(self):
        return f"{self.a}x^4 + {self.b}x^2 + {self.c} = 0"

    def solve(self):
        solution_quadratic = super().solve()
        solution_bi_quadratic = set()

        if solution_quadratic == () or solution_quadratic == self.INF:
            return solution_quadratic

        for solution in solution_quadratic:
            if solution >= 0:
                solution_bi_quadratic.add(solution**0.5)
                solution_bi_quadratic.add(-solution**0.5)

        return tuple(solution_bi_quadratic)


if __name__ == "__main__":
    e = BiQuadraticEquation(0, 0, 1)
    e.show()
    print(e.solve())

    e = BiQuadraticEquation(0, 0, 0)
    e.show()
    print(e.solve())

    e = BiQuadraticEquation(0, 4, 0)
    e.show()
    print(e.solve())

    e = BiQuadraticEquation(0, 3, 5)
    e.show()
    print(e.solve())

    e = BiQuadraticEquation(5, -2, 10)
    e.show()
    print(e.solve())

    e = BiQuadraticEquation(1, 2, 1)
    e.show()
    print(e.solve())

    e = BiQuadraticEquation(2, 3, -2)
    e.show()
    print(e.solve())

    e = BiQuadraticEquation(1, -4, 3)
    e.show()
    print(e.solve())
