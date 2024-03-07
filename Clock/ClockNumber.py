import turtle


class ClockNumber:
    def __init__(self):
        self._position = (0, 0)
        self._scale = 1
        self._one_digit_skeleton = []
        self._two_digit_skeleton = []

    def set_position(self, x, y):
        self._position = x, y

    def set_scale(self, new_scale):
        self._scale = new_scale

    def calc_pos(self):
        scaled_skeleton = []
        new_sceleton = []

        for k in range(len(self._one_digit_skeleton)):
            scaled_skeleton.append([self._one_digit_skeleton[k][0] * self._scale,
                                    self._one_digit_skeleton[k][1] * self._scale])

        for i in range(len(self._one_digit_skeleton)):
            new_sceleton.append([scaled_skeleton[i][0] + self._position[0],
                                 scaled_skeleton[i][1] + self._position[1]])

        return new_sceleton

    def get_skeleton(self):
        return self._one_digit_skeleton

    def draw(self):
        assert len(self._one_digit_skeleton) > 0

        skeleton = self.calc_pos()

        turtle.up()
        turtle.setpos(*skeleton[0])
        turtle.down()

        for point in skeleton[1:]:
            turtle.goto(*point)

        turtle.up()
        turtle.setpos(self._position)
        turtle.down()

    def draw_two_digit(self):
        assert len(self._two_digit_skeleton) > 0

        digit_a, digit_b = self._two_digit_skeleton
        digit_a.set_position(self._position[0] - 5 * self._scale, self._position[1])
        digit_b.set_position(self._position[0] + 5 * self._scale, self._position[1])
        digit_a.draw()
        digit_b.draw()

    def zero(self):
        self._one_digit_skeleton = [[5, 10], [5, -10], [-5, -10], [-5, 10], [5, 10]]

    def one(self):
        self._one_digit_skeleton = [[0, 10], [0, -10]]

    def two(self):
        self._one_digit_skeleton = [[-5, 10], [5, 10], [5, 0], [-5, 0], [-5, -10], [5, -10]]

    def three(self):
        self._one_digit_skeleton = [[-5, 10], [5, 10], [5, 0], [0, 0], [5, 0], [5, -10], [-5, -10]]

    def four(self):
        self._one_digit_skeleton = [[-5, 10], [-5, 0], [5, 0], [5, 10], [5, -10]]

    def five(self):
        self._one_digit_skeleton = [[5, 10], [-5, 10], [-5, 0], [5, 0], [5, -10], [-5, -10]]

    def six(self):
        self._one_digit_skeleton = [[5, 10], [-5, 10], [-5, 0], [5, 0], [5, -10], [-5, -10], [-5, 0]]

    def seven(self):
        self._one_digit_skeleton = [[-5, 10], [5, 10], [5, -10]]

    def eight(self):
        self._one_digit_skeleton = [[-5, 0], [-5, 10], [5, 10], [5, 0], [-5, 0], [-5, -10], [5, -10], [5, 0]]

    def nine(self):
        self._one_digit_skeleton = [[5, 0], [5, 10], [-5, 10], [-5, 0], [5, 0], [5, -10], [-5, -10]]

    def ten(self):
        digit_1, digit_0 = ClockNumber(), ClockNumber()
        digit_1.one(), digit_0.zero()

        self._two_digit_skeleton = [digit_1, digit_0]

    def eleven(self):
        digit_a, digit_b = ClockNumber(), ClockNumber()
        digit_a.one(), digit_b.one()

        self._two_digit_skeleton = [digit_a, digit_b]

    def twelve(self):
        digit_1, digit_2 = ClockNumber(), ClockNumber()
        digit_1.one(), digit_2.two()

        self._two_digit_skeleton = [digit_1, digit_2]


