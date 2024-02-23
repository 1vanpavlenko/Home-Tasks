class Vector:
    def __init__(self, first_arg, *arguments):
        if isinstance(first_arg, Vector):
            assert len(arguments) == 0

            self.coordinates = first_arg.coordinates

        else:
            assert isinstance(first_arg, int) or isinstance(first_arg, float)

            for arg in arguments:
                assert isinstance(arg, int) or isinstance(arg, float)

            coordinates = (None, first_arg) + arguments

            self.coordinates = coordinates[1:]

    def __str__(self):
        return f'{self.coordinates}'

    def dimension(self):
        return len(self.coordinates)

    def length(self):
        res = 0

        for crd in self.coordinates:
            res += crd ** 2

        return res ** 0.5

    def arithmetic_mean(self):
        return sum(self.coordinates) / len(self.coordinates)

    def max(self):
        maximum = self.coordinates[0]

        for crd in self.coordinates[1:]:
            if maximum < crd:
                maximum = crd

        return maximum

    def min(self):
        if len(self.coordinates) == 1:
            return self.coordinates[0]

        minimum = self.coordinates[0]

        for crd in self.coordinates[1:]:
            if minimum > crd:
                minimum = crd

        return minimum
