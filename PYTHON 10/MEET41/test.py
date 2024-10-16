import turtle

pen_1 = turtle.Turtle()
pen_1.color("red")

# S
pen_1.penup()
pen_1.goto(-50, 0)
pen_1.pendown()

pen_1.forward(20)
pen_1.circle(20,180)

pen_1.circle(-20,180)
pen_1.forward(20)

# O

pen_1.penup()
pen_1.goto(10, 0)
pen_1.pendown()

pen_1.forward(20)
pen_1.circle(30, 360)

# C

pen_1.penup()
pen_1.goto(100, 0)
pen_1.pendown()

pen_1.circle(30,-180)
pen_1.forward(20)

turtle.exitonclick()