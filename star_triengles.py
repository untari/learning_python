import turtle
def triangles(color, start):
    tri = turtle.Turtle()
    tri.color(color)
    tri.speed(0)
    tri.width(5)
    tri.right(start)
    for shape in range(6):
        for side in range(3):
            tri.forward(100)
            tri.right(120)
        tri.right(15)
    tri.hideturtle()


triangles("red", 0)
triangles("yellow", 140)
triangles("blue", 240)
