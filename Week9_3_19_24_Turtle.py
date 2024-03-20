# Guess the Number
import turtle, random

t = turtle.Turtle()
screen = turtle.Screen()

t.penup()
t.goto(-450, 0)
t.pendown()

tries = 7

answer = random.randint(1, 100)

guess = screen.numinput("Guess the number", "Number", 1, 1, 100)

while guess != answer and tries > 0:
    tries -= 1
    if guess > answer:
        t.write(f"Too High! You have {tries} tries left", font=("Arial", 50, "normal"))
    
    elif guess < answer:
        t.write(f"Too Low! You have {tries} tries left", font=("Arial", 50, "normal"))
    
    guess = screen.numinput("Guess the number", "Number", 1, 1, 100)

    t.clear()

if guess == answer:
    t.write(f"Correct! You guessed it in {7-tries} tries", font=("Arial", 50, "normal"))

else:
    t.write(f"You ran out of tries! The correct answer is {answer}", font=("Arial", 50, "normal"))

# Calculator
num = screen.numinput("Enter a number", "First Number")
op = screen.textinput("Enter an operation", "+, -, *, /")
num2 = screen.numinput("Enter another number", "Second Number")

if op == "+":
    t.write(f"{num} + {num2} = {num+num2}", font=("Arial", 50, "normal"))

# Error Handling
# TypeError
num = 10

print("hello" + num)

# Syntax and Indentation Error
num = 10

if num = 10:
print("num is 10")

# IndexError
my_list = [1, 2, 3, 4]
print(my_list[4])

# Catch the IndexError and provide proper output
my_list = [1, 2, 3, 4]

try:
    print(my_list[4])

except:
    print("Index 4 does not exist")

# Catch the TypeError and provide proper output
num = 10
string = "hello"

try:
    print(num + string)

except:
    print("Invalid data types")
