

import turtle
t = turtle.Pen()
t.speed(6)
t.pencolor(0.2, 0.8, 0.55)
t.pensize(1)
number_of_circles = int(turtle.numinput("Circles:","Insert the number of circles",6))

for x in range(number_of_circles) :
    t.circle(100)
    t.left(360/number_of_circles)