# ___Triangle rotation animation___ #

import turtle
from Triangle import Triangle
from time import sleep
from functions import calc_length

vertex_1 = [float(_) for _ in input("Enter first vertex (any two numbers): ").split()]
assert len(vertex_1) == 2
vertex_2 = [float(_) for _ in input("Enter second vertex (any two numbers): ").split()]
assert len(vertex_2) == 2
position = [float(_) for _ in input("Enter position: ").split()]
assert len(position) == 2

triangle = Triangle(*vertex_1, *vertex_2)

current_vertex_1 = vertex_1[0] + position[0], vertex_1[1] + position[1]
current_vertex_2 = vertex_2[0] + position[0], vertex_2[1] + position[1]

a = calc_length(current_vertex_1, current_vertex_2)
b = calc_length(position, current_vertex_2)
c = calc_length(position, current_vertex_1)
# a - position, b - vertex_1, c - vertex_2
# rotation point - точка перетину бісектрис
rotation_point = ((a * position[0] + b * current_vertex_1[0] + c * current_vertex_2[0]) / (a + b + c),
                  (a * position[1] + b * current_vertex_1[1] + c * current_vertex_2[1]) / (a + b + c))

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
