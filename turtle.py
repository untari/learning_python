import turtle
sides = 5
length = 100
t = turtle.Turtle()
t.color("orange")
for side in range(sides):
    t.forward(length)
    t.right(360 / sides)

import turtle
t = turtle.Turtle()
t.color("cyan")

for side in range(19):
    t.forward(side*10)
    t.right(120)