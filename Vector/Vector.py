class Vector:
    def __init__(self, *args):
        assert len(args) > 0

        if isinstance(args[0], Vector):
            assert len(args) == 1
            vector = args[0]

            self.__coordinates = vector.__coordinates
            self.__dimension = vector.__dimension

        else:
            for arg in args:
                assert isinstance(arg, (int, float))

            self.__coordinates = args
            self.__dimension = len(args)

    def __str__(self):
        if self.__dimension == 1:
            return f"({self.__coordinates[0]})"

        return f"{self.__coordinates}"

    def __add__(self, other):
        assert self.__dimension == other.__dimension
        new_vector = []

        for index in range(self.__dimension):
            new_vector.append(self.__coordinates[index] + other.__coordinates[index])

        return Vector(*new_vector)

    def __sub__(self, other):
        assert self.__dimension == other.__dimension
        new_vector = []

        for index in range(self.__dimension):
            new_vector.append(self.__coordinates[index] - other.__coordinates[index])

        return Vector(*new_vector)

    def __mul__(self, value):
        assert isinstance(value, (int, float, Vector))

        if isinstance(value, (int, float)):
            scalar = value
            new_vector = []

            for index in range(self.__dimension):
                new_vector.append(self.__coordinates[index] * scalar)

            return Vector(*new_vector)

        elif isinstance(value, Vector):
            other = value
            assert self.__dimension == other.__dimension
            scalar = 0

            for index in range(self.__dimension):
                scalar += self.__coordinates[index] * other.__coordinates[index]

            return scalar

    def dimension(self):
        return self.__dimension

    def length(self):
        sum_of_squares = 0

        for element in self.__coordinates:
            sum_of_squares += element ** 2

        return sum_of_squares ** 0.5

    def arithmetic_mean(self):
        summ = 0

        for element in self.__coordinates:
            summ += element

        return summ / self.__dimension

    def max(self):
        return max(self.__coordinates)

    def min(self):
        return min(self.__coordinates)
