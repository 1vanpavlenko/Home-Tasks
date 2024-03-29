from Equation import Equation
from QuadraticEquation import QuadraticEquation
from BiQudraticEquation import BiQuadraticEquation


def read(file: str):
    with open(file) as file:
        raw_lines = file.readlines()
        equations = []

        for raw_line in raw_lines:
            clean_line = list(map(int, raw_line.split()))

            if len(clean_line) == 2:
                equations.append(Equation(clean_line[0], clean_line[1]))

            elif len(clean_line) == 3:
                equations.append(QuadraticEquation(clean_line[0], clean_line[1], clean_line[2]))

            elif len(clean_line) == 5:
                equations.append(BiQuadraticEquation(clean_line[0], clean_line[2], clean_line[4]))

        return equations


def solve(equations: list):
    solutions = []

    for equation in equations:
        solutions.append(equation.solve())

    return solutions


def find_unsolved(equations: list):
    solutions = solve(equations)
    unsolved = []

    for solution in solutions:
        if len(solution) == 0:
            index = solutions.index(solution)
            unsolved.append(equations[index])

    return unsolved


def find_with_one_solution(equations: list):
    solutions = solve(equations)
    with_one_sol = []

    for solution in solutions:
        if len(solution) == 1:
            index = solutions.index(solution)
            with_one_sol.append(equations[index])

    return with_one_sol


def find_with_two_solutions(equations: list):
    solutions = solve(equations)
    with_two_sol = []

    for solution in solutions:
        if len(solution) == 2:
            index = solutions.index(solution)
            with_two_sol.append(equations[index])

    return with_two_sol


def find_with_three_solutions(equations: list):
    solutions = solve(equations)
    with_three_sol = []

    for solution in solutions:
        if len(solution) == 3:
            index = solutions.index(solution)
            with_three_sol.append(equations[index])

    return with_three_sol


def find_with_four_solutions(equations: list):
    solutions = solve(equations)
    with_four_sol = []

    for solution in solutions:
        if len(solution) == 4:
            index = solutions.index(solution)
            with_four_sol.append(equations[index])

    return with_four_sol


def find_with_infinite_solutions(equations: list):
    solutions = solve(equations)
    with_inf_sol = []

    for solution in solutions:
        if solution == "infinity":
            index = solutions.index(solution)
            with_inf_sol.append(equations[index])

    return with_inf_sol


if __name__ == '__main__':
    eq = read('input01.txt')
    print(solve(eq))

