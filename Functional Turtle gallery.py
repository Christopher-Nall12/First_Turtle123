


import turtle


size = 0

turtle.speed(10000)
turtle.penup()

turtle.goto(-200, 200)
turtle.pendown()
turtle.color("orange")

def star(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

star(turtle, 75)

for i in range(50):
    star(turtle, 75)
    turtle.right(5)
    size += 3

turtle.color("blue")
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

def square(turtle,side):
    for i in range(4):
        turtle.right(90)
        turtle.forward(100)



for i in range(72):
    square(turtle,75)
    turtle.left(5)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
size = 0


def square(turtle, side):
    for i in range(5):
        turtle.forward(size)
        turtle.right(90)


square(turtle, 75)

for i in range(50):
    square(turtle, 75)
    turtle.right(5)
    size += 3

turtle.penup()
turtle.color("firebrick")
turtle.goto(200, -200)
turtle.pendown()


def star(turtle,side):
    for i in range(5):
        turtle.right(144)
        turtle.forward(100)


for i in range(30):
    star(turtle,75)
    turtle.left(5)


turtle.exitonclick()