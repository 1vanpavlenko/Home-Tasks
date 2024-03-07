# ___Triangle rotation animation___ #

import turtle
from Triangle import Triangle
from time import sleep

vertex_1 = [float(_) for _ in input("Enter first vertex (any two numbers): ").split()]
assert len(vertex_1) == 2
vertex_2 = [float(_) for _ in input("Enter second vertex (any two numbers): ").split()]
assert len(vertex_2) == 2
position = [float(_) for _ in input("Enter third vertex (position): ").split()]
assert len(position) == 2

a = ((vertex_1[0] - vertex_2[0]) ** 2 + (vertex_1[1] - vertex_2[1]) ** 2) ** 0.5       # position
b = ((position[0] - vertex_2[0]) ** 2 + (position[1] - vertex_2[1]) ** 2) ** 0.5       # vertex_1
c = ((position[0] - vertex_1[0]) ** 2 + (position[1] - vertex_1[1]) ** 2) ** 0.5       # vertex_2

rotation_point = ((a * position[0] + b * vertex_1[0] + c * vertex_2[0]) / (a + b + c),
                  (a * position[1] + b * vertex_1[1] + c * vertex_2[1]) / (a + c + b))

triangle = Triangle(*vertex_1, *vertex_2)
triangle.set_position(position)
triangle.set_rotation_point(rotation_point)
sleep(3)

rotation_point_draw = turtle.Turtle()
rotation_point_draw.up()
rotation_point_draw.setpos(*rotation_point)
rotation_point_draw.down()
rotation_point_draw.dot(4)
rotation_point_draw.hideturtle()
sleep(3)

for angle in range(0, 363, 3):
    triangle.set_angle(angle)
    triangle_turtle = triangle.draw()

    if angle != 360:
        triangle_turtle.clear()

turtle.mainloop()
