# List Basics
my_list = ["a", "b", "c", "d", "e", "f", "g", "h"]

# Append to list
my_list.append("i")
print(my_list)

# Remove from list
my_list.remove("b")
print(my_list)

# Index value from list
print(my_list[3])

# Replace value in list
my_list[1] = 0

# Print out indexes and values in list
for i in range(len(my_list)):
    print(i, my_list[i])

# Even Number Replacer (Student Code)
my_list = []
while len(my_list) != 10:
    number = int(input("Enter a number: "))
    my_list.append(number)

even_list = []
for i in my_list:
    if i % 2 == 0:
        even_list.append("even")
    if i % 2 != 0:
        even_list.append(i) 
          
print(even_list)

# Even Number Replacer (Official For Loop Code)
my_list = []
for i in range(10):
    num = int(input("Enter a number: "))
    my_list.append(num)

for i in range(len(my_list)):
    if my_list[i] % 2 == 0:
        my_list[i] = "even"

print(my_list)

# Even Number Replacer (Official While Loop Code)
numbers = []
num = int(input("Enter a number: "))
while num > 0:
    numbers.append(num)
    num = int(input("Enter a number: "))

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = "even"

print(numbers)
