from math import cos, sin, radians
import turtle


class Triangle:
    _color = '#000000'

    def __init__(self, x1, y1, x2, y2):
        self._vertex_1 = x1, y1
        self._vertex_2 = x2, y2
        self._position = 0, 0
        self._speed = 0
        self._angle = 0

    def set_position(self, new_x, new_y):
        self._position = new_x, new_y

    def drawing_speed(self, new_speed):
        assert new_speed >= 0
        self._speed = new_speed

    def set_color(self, new_color):
        self._color = new_color

    def set_angle(self, new_angle):
        self._angle = new_angle

    def add_angle(self, input_angle):
        self._angle += input_angle

    def get_position(self):
        return self._position

    def get_angle(self):
        return self._angle

    def calc_rotation(self):
        vertex_1, vertex_2 = self._vertex_1, self._vertex_2
        theta = radians(self._angle)
        rotated_vertex_1 = (vertex_1[0] * cos(theta) + vertex_1[1] * sin(theta),
                            -vertex_1[0] * sin(theta) + vertex_1[1] * cos(theta))
        rotated_vertex_2 = (vertex_2[0] * cos(theta) + vertex_2[1] * sin(theta)
                            , -vertex_2[0] * sin(theta) + vertex_2[1] * cos(theta))
        return rotated_vertex_1, rotated_vertex_2

    def calc_current_pos(self):
        vertex_1, vertex_2 = self._vertex_1, self._vertex_2
        rotated_vertex_1, rotated_vertex_2 = self.calc_rotation()

        current_vertex_1 = (rotated_vertex_1[0] + self._position[0],
                            rotated_vertex_1[1] + self._position[1])
        current_vertex_2 = (rotated_vertex_2[0] + self._position[0],
                            rotated_vertex_2[1] + self._position[1])

        return current_vertex_1, current_vertex_2

    def draw(self):
        triangle = turtle.Turtle()

        triangle.speed(self._speed)
        triangle.color(self._color)

        current_v1, current_v2 = self.calc_current_pos()

        triangle.up()
        triangle.setpos(self._position)
        triangle.down()

        triangle.goto(current_v1)
        triangle.goto(current_v2)
        triangle.setpos(self._position)

        triangle.down()
        triangle.hideturtle()

        return triangle
