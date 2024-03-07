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
        self._rotation_point = None

    def set_position(self, new_x, new_y):
        self._position = new_x, new_y

    def drawing_speed(self, new_speed):
        assert new_speed >= 0
        self._speed = new_speed

    def set_color(self, new_color):
        self._color = new_color

    def set_angle(self, new_angle):
        self._angle = new_angle

    def set_rotation_point(self, new_rotation_point):
        self._rotation_point = new_rotation_point

    def add_angle(self, input_angle):
        self._angle += input_angle

    def get_position(self):
        return self._position

    def get_angle(self):
        return self._angle

    @staticmethod
    def calc_point_rotation(point, angle):
        theta = radians(angle)
        rotated_vertex = (point[0] * cos(theta) + point[1] * sin(theta),
                          -point[0] * sin(theta) + point[1] * cos(theta))

        return rotated_vertex

    def calc_current_pos(self):
        rotated_vertex_1 = self.calc_point_rotation(self._vertex_1, self._angle)
        rotated_vertex_2 = self.calc_point_rotation(self._vertex_2, self._angle)

        if self._rotation_point == None or self._rotation_point == self._position:
            current_position = self._position
        else:
            vector = (self._position[0] - self._rotation_point[0],
                               self._position[1] - self._rotation_point[1])
            rotated_vector = self.calc_point_rotation(vector, self._angle)
            current_position = (rotated_vector[0] + self._rotation_point[0],
                                rotated_vector[1] + self._rotation_point[1])

        current_vertex_1 = (rotated_vertex_1[0] + current_position[0],
                            rotated_vertex_1[1] + current_position[1])
        current_vertex_2 = (rotated_vertex_2[0] + current_position[0],
                            rotated_vertex_2[1] + current_position[1])

        return current_vertex_1, current_vertex_2, current_position

    def draw(self):
        triangle = turtle.Turtle()

        triangle.speed(self._speed)
        triangle.color(self._color)

        current_vertex_1, current_vertex_2, current_position = self.calc_current_pos()

        triangle.up()
        triangle.setpos(current_position)
        triangle.down()

        triangle.goto(current_vertex_1)
        triangle.goto(current_vertex_2)
        triangle.setpos(current_position)

        triangle.down()
        triangle.hideturtle()

        return triangle
