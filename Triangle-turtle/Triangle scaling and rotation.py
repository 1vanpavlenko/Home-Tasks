from Triangle import Triangle
import turtle

vertex_1 = tuple([float(_) for _ in input("V1: ").split()])
vertex_2 = tuple([float(_) for _ in input("V2: ").split()])
position = tuple([float(_) for _ in input("POS: ").split()])
scale = float(input("SCALE: "))

triangle = Triangle(vertex_1, vertex_2)
triangle.set_position(position)
fixed_point = triangle.centroid()
triangle.set_scale_point(fixed_point)
triangle.set_rotation_point(fixed_point)
scaling_value = 1
scale_step = (scale - 1) / 120

sample_triangle = triangle.draw()
sample_triangle.hideturtle()

sample_dots = turtle.Turtle()
sample_dots.up()
sample_dots.setpos(0, 0)
sample_dots.down()
sample_dots.dot(5)
sample_dots.up()
sample_dots.setpos(fixed_point)
sample_dots.down()
sample_dots.dot(5)
sample_dots.hideturtle()

for angle in range(0, 363, 3):
    triangle.set_angle(angle)
    triangle.set_scale(scaling_value)
    drawn_triangle = triangle.draw()
    scaling_value += scale_step

    if angle < 360:
        drawn_triangle.clear()

turtle.mainloop()
