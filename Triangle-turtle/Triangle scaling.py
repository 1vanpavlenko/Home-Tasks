import turtle
from Triangle import Triangle
from time import sleep


massage = """This program animates triangle scaling around center of mass.
To run this program enter two vertexes, point to determine triangle position and a scaling value.
"""
print(massage)

vertex_1 = tuple([float(_) for _ in input("Enter first vertex: ").split()])
assert len(vertex_1) == 2
vertex_2 = tuple([float(_) for _ in input("Enter second vertex: ").split()])
assert len(vertex_2) == 2
position = tuple([float(_) for _ in input("Enter position: ").split()])
assert len(position) == 2
scale = float(input("Enter scaling value bigger than 1: "))
assert scale > 1

triangle = Triangle(vertex_1, vertex_2)
triangle.set_scale_point(triangle.centroid())
dot = turtle.Turtle()
dot.up()
dot.setpos(triangle.centroid())
dot.down()
dot.dot(4)
dot.hideturtle()
sample_triangle = triangle.draw()

scaling_value = 1
sleep(2)

while scaling_value <= scale:
    triangle.set_scale(scaling_value)
    triangle_turtle = triangle.draw()
    triangle_turtle.hideturtle()
    scaling_value += 0.05
    sleep(0.1)

    if scaling_value <= scale:
        triangle_turtle.clear()

turtle.mainloop()
