import turtle
turtle.hideturtle()
turtle.penup()
turtle.pensize(10)

# head
turtle.goto(0, -145)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(168)
turtle.end_fill()
turtle.fillcolor("black")
turtle.penup()

# Eye 1
turtle.goto(-50, 5)
turtle.pendown()
turtle.begin_fill()
turtle.circle(42)
turtle.end_fill()
turtle.penup()

# Eye 2
turtle.goto(50, 5)
turtle.pendown()
turtle.begin_fill()
turtle.circle(42)
turtle.end_fill()
turtle.penup()

# Mouth 
mouthRadius = 180 * 0.6

turtle.goto(0, -mouthRadius)
turtle.pendown()
turtle.circle(mouthRadius, 70)
turtle.penup()
turtle.setheading(0)

turtle.goto(0, -mouthRadius)
turtle.pendown()
turtle.circle(mouthRadius, -70)
turtle.penup()

turtle.done()