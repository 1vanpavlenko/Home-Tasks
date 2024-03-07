import turtle
from math import sin, cos, radians
from ClockNumber import ClockNumber
from ClockArrow import ClockArrow


class ClockFace:
    numbers = [i for i in range(1, 13)]
    digits_list = [ClockNumber() for _ in numbers]
    one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve = digits_list
    one.one(), two.two(), three.three(), four.four(), five.five(), six.six(), seven.seven()
    eight.eight(), nine.nine(), ten.ten(), eleven.eleven(), twelve.twelve()
    clock_numbers = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve]

    def __init__(self, radius):
        self._outer_radius = radius
        self._inner_radius = radius - radius / 25
        self._center = (0, 0)
        self._font_size = radius // 10
        self._numbers_position = []
        self._markings_position = []

    @staticmethod
    def calc_rotation(point, angle):
        x, y = point
        theta = radians(angle)
        return cos(theta) * x + sin(theta) * y, -sin(theta) * x + cos(theta) * y

    def calc_numbers_position(self):
        start_position = 0, self._outer_radius - (self._outer_radius - self._inner_radius) * 3
        angle = 30

        for number in self.numbers:
            new_position = self.calc_rotation(start_position, angle * number)
            self._numbers_position.append(new_position)

    def calc_markings_position(self):
        start_position = 0, self._outer_radius
        angle = 6

        for i in range(1, 61):
            new_position = self.calc_rotation(start_position, angle * i)
            self._markings_position.append(new_position)

    def draw(self):
        clock_face = turtle.Turtle()

        clock_face.speed(0)

        self.calc_numbers_position()
        self.calc_markings_position()

        outer_circle_pos = (0, -self._outer_radius)
        inner_circle_pos = (0, -self._inner_radius)

        clock_face.up()
        clock_face.setpos(self._center)
        clock_face.setpos(outer_circle_pos)
        clock_face.down()

        clock_face.circle(self._outer_radius)

        clock_face.up()
        clock_face.setpos(inner_circle_pos)
        clock_face.down()

        clock_face.circle(self._inner_radius)

        clock_face.up()
        clock_face.setpos(self._center)
        clock_face.down()

        small_marking = self._outer_radius - self._inner_radius
        large_marking = small_marking * 2

        for step in range(60):
            if (step + 1) % 5 == 0:
                marking = ClockArrow(large_marking)
            else:
                marking = ClockArrow(small_marking)

            marking.set_position(*self._markings_position[step])
            marking.set_angle(180 + (step + 1) * 6)
            marking.draw()

        for i in range(12):
            digit = self.digits_list[i]
            digit.set_scale(self._outer_radius / 350)
            digit.set_position(*self._numbers_position[i])

            if i < 9:
                digit.draw()

            else:
                digit.draw_two_digit()

        clock_face.up()
        clock_face.setpos(self._center)
        clock_face.down()

        clock_face.dot(10)

        return clock_face
