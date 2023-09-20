# Calculator
# Operations: +, -, *, /, **
# Continuously run until the user decides to stop
# Input Validation: if the user puts in an invalid number
# or an invalid operation, tell the user an error
# message and let them input something again

def get_number_input():
    while True:
        try:
            num = int(input("Enter a number: "))
            return num

        except:
            print("Put a valid number!")

def get_operation_input():
    

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
    num = get_number_input()
    op = get_operation_input()
    num2 = get_number_input()

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
    
