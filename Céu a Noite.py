import turtle
from turtle import *
from random import randint

speed(0)

window = turtle.Screen()
window.bgcolor("#00008C")

def draw_circle(turtle, color, x, y, radius):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_star (turtle, color, x, y, size):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(144)
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
        turtle.forward(size)
    turtle.end_fill()
    turtle.setheading(0)

#Moon (Lua)
draw_circle(turtle, "white", 120, 80, 50)
draw_circle(turtle, "darkblue" , 100, 80 , 50)

#Star (Estrelas)
numbersOfStars = randint(10,100)

for i in range(0, numbersOfStars):
    x = randint(-180, 180)
    y = randint(-160, 160)
    size = randint(5, 20)

    draw_star(turtle, "white" , x, y, size)

#Message (Mensagem)
penup()
color("yellow")
goto(-110, -200)
write("Season's Greetings (Boas Festas)", font=("Arial" , 20 , "bold"))

window.exitonclick()

















