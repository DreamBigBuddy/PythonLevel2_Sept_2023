# Phonebook Program
contacts = []

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
        first_name = input("Enter a first name: ")
        last_name = input("Enter a last name: ")
        number = input("Enter a number: ")
        birthday = input("Enter a birthday: ")

        contacts.append({"first_name": first_name, "last_name": last_name, "number": number, "birthday": birthday})

    elif choice == "2":
        entry = input("Would you like to replace first_name, last_name, number, or birthday? ")
        while entry != "first_name" and entry != "last_name" and entry != "number" and entry != "birthday":
            print("Try again")
            entry = input("Would you like to replace first_name, last_name, number, or birthday? ")

        value = input(f"Enter the {entry} that you want to replace: ")
        new_value = input(f"Enter the new {entry}: ")

        for i in range(len(contacts)):
            if contacts[i][entry] == value:
                contacts[i][entry] = new_value
                break

    elif choice == "3":
        entry = input("Would you like to delete based on first_name, last_name, number, or birthday? ")
        while entry != "first_name" and entry != "last_name" and entry != "number" and entry != "birthday":
            print("Try again")
            entry = input("Would you like to delete based on first_name, last_name, number, or birthday? ")

        value = input(f"Enter the {entry} that you want to delete: ")

        for i in range(len(contacts)):
            if contacts[i][entry] == value:
                contacts.pop(i)
                break

    elif choice == "4":
        entry = input("Would you like to view based on first_name, last_name, number, or birthday? ")
        while entry != "first_name" and entry != "last_name" and entry != "number" and entry != "birthday":
            print("Try again")
            entry = input("Would you like to view based on first_name, last_name, number, or birthday? ")

        value = input(f"Enter the {entry} that you want to view: ")

        for i in range(len(contacts)):
            if contacts[i][entry] == value:
                print(contacts[i])
                break

    elif choice == "5":
        for i in range(len(contacts)):
            print(contacts[i])
