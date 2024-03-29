class Figure:
    def __init__(self, *args):
        self.sides_list = list(args)
        self.dimension = 2

    def dimension(self):
        return self.dimension

    def perimeter(self):
        if self.dimension == 2:
            return sum(self.sides_list)

