class Vector:
    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def __str__(self):
        return f'{self.coordinates}'

    def dimension(self):
        return len(self.coordinates)

    def length(self):
        res = 0

        for c in self.coordinates:
            res += c ** 2

        return res ** 0.5

    def arithmetic_mean(self):
        return sum(self.coordinates) / len(self.coordinates)

    def max(self):
        maximum = self.coordinates[0]

        for c in self.coordinates[1:]:
            if maximum < c:
                maximum = c

        return maximum

    def min(self):
        if len(self.coordinates) == 1:
            return self.coordinates[0]

        minimum = self.coordinates[0]

        for c in self.coordinates[1:]:
            if minimum > c:
                minimum = c

        return minimum
