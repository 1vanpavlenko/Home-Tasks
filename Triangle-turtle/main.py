from Triangle import Triangle
import turtle


t = Triangle(100, 0, 0, 100)
t.draw()
t.set_position(100, -100)
t.draw()
t.set_angle(270)
t.draw()

turtle.mainloop()
