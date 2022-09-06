import turtle
# Initialization of the turtle
def stairs(size, nb ):
    for i in range(0, nb):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(90)
    t.forward(size)

t = turtle.Turtle()


stairs(38, 5)

turtle.done()