# Calculator with Error Handling
again = ""
while again == "":
    try:
        num = int(input("Enter a number: "))

    except:
        print("Invalid integer")
        continue
        
    operation = input("Enter an operation: ")

    try:
        num2 = int(input("Enter a number: "))

    except:
        print("Invalid integer")
        continue

    if operation == "+":
        print(f"{num} + {num2} = {num + num2}")

    again = input("Press enter to run the program again: ")

# Continue Statement
for i in range(10):
    if i == 5:
        continue

    print(i)

# Dictionary Methods
my_dict = {"a": 1, "b": 2, "c": 3}

# Indexing Dictionary
print(my_dict["b"])

# Replacing Value in Dictionary
my_dict["c"] = 4

# Removing Value in Dictionary
my_dict.pop("c")

# Getting a Value in Dictionary
print(my_dict.get("a"))

# Getting All Items in Dictionary (Keys and Values)
print(list(my_dict.items()))

# Iterating Through Dictionary
for i in my_dict:
    print(i, my_dict[i])
