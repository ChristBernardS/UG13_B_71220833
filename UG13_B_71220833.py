import turtle
t = turtle.Turtle()
s = turtle.Screen()
t.pencolor('Cyan')
s.bgcolor('Black')
t.speed(0)

# C
t.color('Cyan')
t.penup()
t.goto(-200, 100)
t.pendown()
t.right(180)
t.forward(20)
t.circle(100, 180)
t.forward(20)
t.penup()

t.speed(10)
t.left(90)
t.forward(100)
t.right(90)
t.forward(80)

# 8
t.pendown()
t.circle(50, 360)
t.circle(-50, 360)
t.penup()

t.forward(100)
t.left(90)
t.forward(100)
t.right(90)

# 3
t.pendown()
t.circle(-50, 180)
t.right(180)
t.circle(-50, 180)
t.penup()

t.right(180)
t.forward(100)
t.left(90)
t.forward(200)
t.right(90)

# 3
t.pendown()
t.circle(-50, 180)
t.right(180)
t.circle(-50, 180)
t.penup()

# B
t.forward(-100)
t.right(90)
t.pendown()
t.forward(200)
t.right(90)
t.forward(50)
t.circle(-50, 180)
t.right(180)
t.circle(-50, 180)
t.forward(50)

turtle.done()