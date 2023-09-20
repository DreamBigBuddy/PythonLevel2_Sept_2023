def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")

greet("Vaman", "Rajagopal")

def add(x, y):
    return x+y

num = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

sum_of_two = add(num, num2)

print(sum_of_two)

string = "Hello World"
print(string[::2])

my_list = ["a", "b", 3, 4, "e"]
print(my_list[::2])

def reverse_string(string):
    # Put your reverse code here

user_string = input("Enter a string: ")
reversed_string = reverse_string(user_string)
print(f"Your reversed string: {reversed_string}")
