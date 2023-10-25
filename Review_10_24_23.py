# Calculator

# Operations: +, -, *, /, **

# Continuously run until the user decides to stop

# Input Validation: if the user puts in an invalid number

# or an invalid operation, tell the user an error

# message and let them input something again


operations_list = ["+", "-", "*", "/", "**"]

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
    isValid = False

    while not isValid:
        try:
            num = int(input("Enter a number: "))
            isValid = True

        except:
            print("Invalid number")

    op = input("Enter an operation: ")
    while op not in operations_list:
        print("Invalid operation")
        op = input("Enter an operation: ")

    isValid = False

    while not isValid:
        try:
            num2 = int(input("Enter another number: "))
            isValid = True

        except:
            print("Invalid number")


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
