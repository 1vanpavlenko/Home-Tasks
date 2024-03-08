import turtle
from Triangle import Triangle

triangle = Triangle(50, 0, 0, 50)
triangle.draw()
triangle.set_scale(2)
triangle.set_scale_point((25, 25))
triangle.draw()
turtle.mainloop()
