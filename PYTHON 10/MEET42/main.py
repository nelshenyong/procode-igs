import turtle

pen_1 = turtle.Turtle()
pen_1.color("red")

pen_1.penup()
pen_1.goto(-300, 0)

pen_1.pendown()
for i in range(5):
    pen_1.forward(100)
    pen_1.right(144)

pen_1.penup()
pen_1.goto(300, 0)

pen_1.pendown()
for i in range(5):
    pen_1.forward(100)
    pen_1.right(144)

# s
pen_1.penup()
pen_1.goto(0, -50)
pen_1.pendown()

pen_1.forward(20)
pen_1.circle(20,180)

pen_1.circle(-20,180)
pen_1.forward(20)


    
turtle.exitonclick()