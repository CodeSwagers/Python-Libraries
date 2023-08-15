import turtle

#screen for output
screen = turtle.Screen()

# Defining a turtle Instance
tur = turtle.Turtle()
tur.speed(40)

# initially penup()
tur.penup()
tur.goto(-400, 250)
tur.pendown()

# Orange Rectangle
tur.color("orange")
tur.begin_fill()
tur.forward(800)
tur.right(90)
tur.forward(167)
tur.right(90)
tur.forward(800)
tur.end_fill()
tur.left(90)
tur.forward(167)

# Green Rectangle
tur.color("green")
tur.begin_fill()
tur.forward(167)
tur.left(90)
tur.forward(800)
tur.left(90)
tur.forward(167)
tur.end_fill()

# Sudarsan Chakar
tur.color("#054187")
tur.penup()
tur.goto(0, 0)
tur.pendown()
tur.pensize(2)
for i in range(24):
    tur.forward( 75)
    tur.backward( 75)
    tur.left(15)
tur.penup()
tur.goto(75, 0)
tur.pendown( )
tur.pensize(5)
tur.circle( 75, 360)
tur.pendown()

word = "Happy Independence Day"
font_size = 18
font_style = ("Arial", font_size, "bold")
tur.penup()
tur.goto(0, -280)  # Starting position for writing
tur.pendown()
tur.write(word, font=font_style, align="center")
turtle.done()
