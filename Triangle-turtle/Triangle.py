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
        self._scale = 1
        self._scale_point = None

    def set_position(self, new_position):
        self._position = new_position

    def drawing_speed(self, new_speed):
        assert new_speed >= 0
        self._speed = new_speed

    def set_color(self, new_color):
        self._color = new_color

    def set_angle(self, new_angle):
        self._angle = new_angle

    def set_rotation_point(self, new_rotation_point):
        self._rotation_point = new_rotation_point

    def set_scale(self, new_scale):
        assert new_scale > 0
        self._scale = new_scale

    def set_scale_point(self, new_cale_point):
        self._scale_point = new_cale_point

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

    @staticmethod
    def calc_point_scale(point, scale):
        return point[0] * scale, point[1] * scale

    def calc_current_pos(self):
        position = self._position
        vertex_1 = self._vertex_1
        vertex_2 = self._vertex_2
        scale = self._scale
        scale_point = self._scale_point
        angle = self._angle
        rotation_point = self._rotation_point

        if scale_point is None or scale_point == position:
            vertex_1 = self.calc_point_scale(vertex_1, scale)
            vertex_2 = self.calc_point_scale(vertex_2, scale)

        else:
            vector_0 = -scale_point[0], -scale_point[1]
            vector_1 = vertex_1[0] - scale_point[0], vertex_1[1] - scale_point[1]
            vector_2 = vertex_2[0] - scale_point[0], vertex_2[1] - scale_point[1]
            vector_rotation_point = ((rotation_point[0] - scale_point[0],
                                     rotation_point[1] - scale_point[1])
                                     if rotation_point is not None else None)

            scaled_vector_0 = self.calc_point_scale(vector_0, scale)
            scaled_vector_1 = self.calc_point_scale(vector_1, scale)
            scaled_vector_2 = self.calc_point_scale(vector_2, scale)
            scaled_vector_rotation_point = (self.calc_point_scale(vector_rotation_point, scale)
                                            if rotation_point is not None else None)

            scaled_scale_point = self.calc_point_scale(scale_point, scale)
            position = (scaled_vector_0[0] + scaled_scale_point[0],
                        scaled_vector_0[1] + scaled_scale_point[1])
            vertex_1 = (scaled_vector_1[0] + scaled_scale_point[0],
                        scaled_vector_1[1] + scaled_scale_point[1])
            vertex_2 = (scaled_vector_2[0] + scaled_scale_point[0],
                        scaled_vector_2[1] + scaled_scale_point[1])
            rotation_point = ((scaled_vector_rotation_point[0] + scaled_scale_point[0],
                               scaled_vector_rotation_point[1] + scaled_scale_point[1])
                              if rotation_point is not None else None)

        rotated_vertex_1 = self.calc_point_rotation(vertex_1, self._angle)
        rotated_vertex_2 = self.calc_point_rotation(vertex_2, self._angle)

        if rotation_point is None or rotation_point == position:
            current_position = position
        else:
            vector_position = position[0] - rotation_point[0], position[1] - rotation_point[1]
            rotated_vector_position = self.calc_point_rotation(vector_position, angle)
            current_position = (rotated_vector_position[0] + rotation_point[0],
                                rotated_vector_position[1] + rotation_point[1])

        current_vertex_1 = (rotated_vertex_1[0] + current_position[0],
                            rotated_vertex_1[1] + current_position[1])
        current_vertex_2 = (rotated_vertex_2[0] + current_position[0],
                            rotated_vertex_2[1] + current_position[1])

        return current_position, current_vertex_1, current_vertex_2

    def draw(self):
        triangle = turtle.Turtle()

        triangle.speed(self._speed)
        triangle.color(self._color)

        current_position, current_vertex_1, current_vertex_2 = self.calc_current_pos()

        triangle.up()
        triangle.setpos(current_position)
        triangle.down()

        triangle.goto(current_vertex_1)
        triangle.goto(current_vertex_2)
        triangle.setpos(current_position)

        triangle.down()
        triangle.hideturtle()

        return triangle
