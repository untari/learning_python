import turtle

def balloon (t, color):
    t.speed()
    t.color(color)
    for side in range(30):
        t.forward(20)
        t.right(12)


    t.color("grey")
    t.forward(30)
    t.right(100)

t = turtle.Turtle()
t.penup()
t.back(100)
t.pendown()
balloon(t, "red")

t.penup()
t.home()
t.pendown()
balloon(t, "blue")

t.penup()
t.home()
t.forward(100)
t.pendown()
balloon(t, "purple")

t.hideturtle()