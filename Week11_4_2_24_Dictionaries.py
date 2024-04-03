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

# Grocery Store Template
def print_items():
    for i in grocery_store_items:
        print(f"Item: {i}, Price: ${grocery_store_items[i]}")

grocery_store_items = {"apples": 1.50, "oranges": 1.25}
shopping_cart = {}

option = ""
while option != "4":
    print("Welcome to the Grocery Store!")
    print("Here are your options:")
    print("1 - Add an item to your list")
    print("2 - Remove an item from your list")
    print("3 - Display items in list")
    print("4 - Exit the Grocery Store")

    option = int(input("Enter your choice: "))

    if option == 1:
        print_items()
        # Ask the user what item they want
        # Check to make sure item exists in store
        # Let user select new item if it doesn't
        # Ask user for quantity of items
        # Add item and quantity to shopping_cart

    elif option == 2:
        # Ask the user what item to remove
        # Check to make sure item exists in cart
        # Let user select new item if it doesn't
        # Remove item from shopping_cart

    elif option == 3:
        print_items()
