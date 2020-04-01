import turtle


def star(color, sides, length, angle, distance):
    galileo = turtle.Turtle()
    galileo.color(color)
    galileo.width(5)
    galileo.speed(8)
    galileo.penup()
    galileo.left(angle)
    galileo.forward(distance)
    galileo.pendown()
    for side in range(sides):
        galileo.forward(length)
        galileo.left(720 / sides)
    galileo.hideturtle()

for angle in [315, 270, 225, 180, 135, 90, 45, 0]:
    star("violet", 5, 50, angle, 100)

for angle in [315, 270, 225, 180, 90, 45, 0]:
    star("white", 5, 30, angle, 60)

