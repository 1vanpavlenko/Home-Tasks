# ___Triangle rotation animation___ #

import turtle
from Triangle import Triangle
from time import sleep

massage = """This program animates triangle rotation around incenter.
To run this program enter two vertexes and a point to determine triangle position."""
print(massage)

vertex_1 = tuple([float(_) for _ in input("Enter first vertex: ").split()])
assert len(vertex_1) == 2
vertex_2 = tuple([float(_) for _ in input("Enter second vertex: ").split()])
assert len(vertex_2) == 2
position = tuple([float(_) for _ in input("Enter position: ").split()])
assert len(position) == 2

triangle = Triangle(vertex_1, vertex_2)

triangle.set_position(position)
rotation_point = triangle.incenter()
triangle.set_rotation_point(rotation_point)
sleep(3)

rotation_point_draw = turtle.Turtle()
rotation_point_draw.up()
rotation_point_draw.setpos(rotation_point)
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
