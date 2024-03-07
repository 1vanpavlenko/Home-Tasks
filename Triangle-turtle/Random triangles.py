# ____100 random triangles____

from Triangle import Triangle
from time import sleep
import random
from turtle import mainloop, up


def random__hex_color() -> str:
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    color = r << 16 | g << 8 | b
    hex_color = hex(color)[2:]

    if len(hex_color) < 6:
        hex_color = (6 - len(hex_color)) * '0' + hex_color

    return '#' + hex_color


if __name__ == '__main__':
    speed = 0.5
    up()
    sleep(3)

    for i in range(100):
        rand_v1 = random.randint(-200, 200), random.randint(-200, 200)
        rand_v2 = random.randint(-200, 200), random.randint(-200, 200)
        rand_px, rand_py = random.randint(-200, 200), random.randint(-200, 200)

        triangle = Triangle(*rand_v1, *rand_v2)
        triangle.set_position(rand_px, rand_py)
        triangle.drawing_speed(speed)
        rand_color = random__hex_color()
        triangle.set_color(rand_color)
        triangle.draw()

    mainloop()




