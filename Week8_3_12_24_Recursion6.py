# Spiral Code
import turtle

t = turtle.Turtle()

t.speed(0)

def spiral(length):
    if length <= 1:
        return

    t.forward(length)
    t.right(90)

    spiral(length-1)

spiral(100)

# Text Input in Turtle
import turtle

t = turtle.Turtle()
screen = turtle.Screen()

name = screen.textinput("Name", "What is your name?")

t.write(name, font=("Arial", 40, "normal"))

age = screen.numinput("Number", "Guess the Number", 0, 0, 100)

t.write(age)
