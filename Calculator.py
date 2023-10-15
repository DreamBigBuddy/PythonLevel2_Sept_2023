# Calculator

# Operations: +, -, *, /, **

# Continuously run until the user decides to stop

# Input Validation: if the user puts in an invalid number

# or an invalid operation, tell the user an error

# message and let them input something again



again = ""



print('''Welcome to the Calculator!

You may do the following operations:

- Addition (+)

- Subtraction (-)

- Multiplication (*)

- Division (/)

- Exponent (**)

''')



while again == "":

    num = int(input("Enter a number: "))

    op = input("Enter an operation: ")

    num2 = int(input("Enter another number: "))



    if op == "+":

        print(f"{num} + {num2} = {num+num2}")



    if op == "-":

        print(f"{num} - {num2} = {num-num2}")



    if op == "*":

        print(f"{num} * {num2} = {num*num2}")



    if op == "/":

        print(f"{num} / {num2} = {num/num2}")



    if op == "**":

        print(f"{num} ** {num2} = {num**num2}")



    again = input("Press enter to rerun: ")
