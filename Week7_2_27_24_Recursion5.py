# Fibonacci Sequence
def f(n):
    if n <= 1:
        return n

    return f(n-1) + f(n-2)

number = int(input("Enter the position of the sequence you want to find: "))
print(f(number))

# Recursive Square
import turtle

t = turtle.Turtle()

def square(sides, length):
    if sides == 0:
        return

    t.forward(length)
    t.right(90)

    square(sides-1, length)

square(4, 100)
