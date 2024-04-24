# Phonebook Program
contacts = {}

choice = ""

while choice != "6":
    choice = input('''What action would you like to do?
1. Add a contact
2. Update a contact
3. Remove a contact
4. View a contact
5. View all contacts
6. Quit the program

Please enter the number to make your selection: ''')

    if choice == "1":
        name = input("Enter a name: ")
        number = input("Enter a number: ")

        contacts[name] = number

    elif choice == "2":
        choice = input("Name or number: ")
        if choice == "name":            
            name = input("Enter the name you want to update: ")
            number = contacts[name]
            contacts.pop(name)
            new_name = input("Enter the new name: ")
            contacts[new_name] = number

        elif choice == "number":
            name = input("Enter the name you want to update: ")
            number = input("Enter the new number: ")
            contacts[name] = number

    elif choice == "3":
        choice = input("Name or number: ")
        if choice == "name":            
            name = input("What name to remove? ")
            contacts.pop(name)

        elif choice == "number":
            number = input("What number to remove? ")
            for i in contacts:
                if contacts[i] == number:
                    contacts.pop(i)
                    break

# Nested Dictionaries
my_dict = {"apple": {"color": "red", "tasty": 7}, "orange": {"color": "orange", "tasty": 6}}
print(my_dict["apple"])
print(my_dict["apple"]["color"])

my_dict["apple"]["location"] = "tree"
print(my_dict)

# Nested Lists and Dictionaries
nested = []
nested.append({"apple": "red"})
nested.append({"orange": "orange"})
nested.append({"banana": "yellow"})
print(nested[2])
