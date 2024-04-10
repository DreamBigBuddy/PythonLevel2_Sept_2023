def print_items_in_store():
    for i in grocery_store_items:
        print(f"Item: {i}, Price: ${grocery_store_items[i]}")

def print_items_in_cart():
    if len(shopping_cart) == 0:
        print("No items in cart")
        return
    
    for i in shopping_cart:
        print(f"Item: {i}, Quantity: {shopping_cart[i]}")

grocery_store_items = {"apples": 1.50, "oranges": 1.25, "bananas": 1.75, "cookies": 2, "pizza": 3.50}
shopping_cart = {}

option = ""
while option != "4":
    print("Welcome to the Grocery Store!")
    print("Here are your options:")
    print("1 - Add an item to your list")
    print("2 - Remove an item from your list")
    print("3 - Display items in list")
    print("4 - Exit the Grocery Store")

    option = input("Enter your choice: ")

    print("\n")

    if option == "1":
        print_items_in_store()

        item = input("What item are you purchasing? ")
        while item not in grocery_store_items:
            item = input("Invalid item. What item are you purchasing? ")

        quantity = int(input(f"How many {item}? "))

        shopping_cart[item] = quantity

    elif option == "2":
        print_items_in_cart()

        item = input("What item are you removing? ")
        while item not in shopping_cart:
            item = input("You do not have this item. What item are you removing? ")

        shopping_cart.pop(item)

    elif option == "3":
        print_items_in_cart()

    print("\n")

total = 0
for i in shopping_cart:
    total += shopping_cart[i] * grocery_store_items[i]
    print(f"Item: {i}, Quantity: {shopping_cart[i]}, Price: ${shopping_cart[i] * grocery_store_items[i]}")

print(f"Your final cost is ${total}")
