from Figure import Figure


class Rectangle(Figure):
    def __init__(self, vertex):
        super().__init__()
        self._vertex_main = vertex

    def draw(self):
        pass
