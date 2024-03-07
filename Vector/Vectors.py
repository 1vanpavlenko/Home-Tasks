class Vector:
    def __init__(self, first_arg=0, *arguments):
        if isinstance(first_arg, Vector):
            assert len(arguments) == 0

            self.coordinates = first_arg.coordinates

        else:
            if isinstance(first_arg, tuple) or isinstance(first_arg, list):
                if len(first_arg) == 0:
                    coordinates = (0,)

                elif len(arguments) == 0:
                    coordinates = tuple(first_arg)

                else:
                    for crd in arguments:
                        assert isinstance(crd, int) or isinstance(crd, float)

                    coordinates = tuple(first_arg) + tuple(arguments)

                self.coordinates = coordinates

            elif isinstance(first_arg, int) or isinstance(first_arg, float):
                if len(arguments) == 0:
                    coordinates = (first_arg,)

                else:
                    for crd in arguments:
                        assert isinstance(crd, int) or isinstance(crd, float)

                    coordinates = (first_arg,) + tuple(arguments)

                self.coordinates = coordinates

    def __str__(self):
        if len(self.coordinates) == 1:
            return f'({self.coordinates[0]})'

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
        list_of_crd = list(self.coordinates)

        list_of_crd.sort()

        return list_of_crd[-1]

    def min(self):
        list_of_crd = list(self.coordinates)

        list_of_crd.sort()

        return list_of_crd[0]
