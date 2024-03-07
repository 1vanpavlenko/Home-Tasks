# ___Triangle rotation animation___ #
import turtle
from turtle import mainloop
from Triangle import Triangle
from time import sleep

vertex_1 = [float(_) for _ in input("Enter first vertex (any two numbers): ").split()]
assert len(vertex_1) == 2
vertex_2 = [float(_) for _ in input("Enter second vertex (any two numbers): ").split()]
assert len(vertex_2) == 2
position = [float(_) for _ in input("Enter third vertex (position): ").split()]
assert len(position) == 2

triangle = Triangle(*vertex_1, *vertex_2)
triangle.set_position(*position)
sample = triangle.draw()
sleep(3)
sample.clear()

for angle in range(0, 363, 3):
    triangle.set_angle(angle)
    triangle_turtle = triangle.draw()

    if angle != 360:
        sleep(0.5)
        triangle_turtle.clear()

mainloop()
