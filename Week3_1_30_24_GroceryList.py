# Grocery List
item_list = []

choice = ""

while choice != "quit" and choice != "q":
    choice = input("What would you like to do: add (a), remove (r), replace (p), view (v)? ")

    if choice == "add" or choice == "a":
        item = input("Enter the item to add: ")
        item_list.append(item)

    elif choice == "remove" or choice == "r":
        index = int(input("Enter the item's index to remove that item: "))
        item_list.pop(index-1)

    elif choice == "replace" or choice == "p":
        index_or_item = input("Index or item? ")
        if index_or_item == "index":
            item = input("Enter the item to add: ")
            index = int(input("Enter the item's index to replace that item: "))
            item_list[index-1] = item

        else:
            remove_item = input("Enter the item to remove: ")
            replace_item = input("Enter the item to replace: ")
            for i in range(len(item_list)):
                if item_list[i] == remove_item:
                    item_list[i] = replace_item

    elif choice == "view" or choice == "v":
        for i in range(len(item_list)):
            print(str(i+1) + ". " + str(item_list[i]))
