import turtle
from math import sin, cos, radians


class ClockArrow:
    def __init__(self, length):
        self._head = (0, length)
        self._position = (0, 0)
        self._angle = 0

    def set_angle(self, angle):
        self._angle = angle

    def set_position(self, x, y):
        self._position = x, y

    @staticmethod
    def calc_rotation(point, angle):
        angle = radians(angle)
        x, y = point
        return cos(angle) * x + sin(angle) * y, -sin(angle) * x + cos(angle) * y

    def calc_abs_pos(self):
        rotated_head = ClockArrow.calc_rotation(self._head, self._angle)
        head = rotated_head[0] + self._position[0], rotated_head[1] + self._position[1]
        return head

    def draw(self, return_as_turtle=True):
        arrow = turtle.Turtle()
        arrow.speed(0)

        head = self.calc_abs_pos()

        arrow.up()
        arrow.setpos(self._position)
        arrow.down()

        arrow.goto(head)
        arrow.setpos(self._position)
        arrow.up()

        arrow.hideturtle()

        return arrow if return_as_turtle else None
