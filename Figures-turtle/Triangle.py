from Figure import Figure


class Triangle(Figure):
    def __init__(self, vertex_1, vertex_2):
        self._vertex_1 = vertex_1
        self._vertex_2 = vertex_2
        super().__init__()

    def draw(self):
        pass
