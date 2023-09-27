# String splicing
string = "Hello World"
print(string[1:9:2]) # Prints el o
## Similar to the range function
## range(start, stop, step)
## string[start:stop:step]

# List splicing
# Same as string splicing

# Function
def double(number):
    return number*2

num = int(input("Enter a number: "))
doubled_num = double(num)
print(f"Your doubled number is {doubled_num}")

# Reverse String
def reverse_string(string):
    return string[::-2]

user_string = input("Enter a string: ")
reversed_string = reverse_string(user_string)
print(f"Your reversed string is: {reversed_string}")

# For Loop
for i in range(10):
    print(i)

print(list(range(5, 10, 2)))

# Appending numbers to a list
numbers = []
for i in range(10):
    numbers.append(i)

# Replacing values in a list
for i in range(len(numbers)):
    if numbers[i] == 5:
        numbers[i] = "Hello"

print(numbers)
