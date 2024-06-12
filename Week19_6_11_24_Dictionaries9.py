students = {}
classes = {}

choice = ""

print("Welcome to the grade management program!")

while choice != "9":
    print('''Select an option:
1. Add a class
2. Remove a class
3. Update a class
4. View a class
5. Add a student
6. Remove a student
7. Update a student
8. View a student
9. Quit
''')

    choice = input("> ")

    if choice == "1":
        name_of_class = input("Enter the name of the class: ")
        description_of_class = input("Enter the description of the class: ")

        classes[name_of_class[:3].lower().replace(" ", "")] = {"name": name_of_class, "desc": description_of_class, "students": 0}

        print("Class created!")

    elif choice == "2":
        id_or_name = input("Remove by ID or name? ").lower().replace(" ", "")

        if "id" in id_or_name:
            class_id = input("Enter class ID: ").lower().replace(" ", "")
            classes.pop(class_id)
            print("Removed class!")

        elif "name" in id_or_name:
            name = input("Enter class name: ").lower().replace(" ", "")
            for i in classes:
                if classes[i]["name"].lower().replace(" ", "") in name:
                    classes.pop(i)
                    break

            print("Removed class!")

    elif choice == "3":
        id_or_name = input("Update by ID or name? ").lower().replace(" ", "")

        if "id" in id_or_name:
            identifier = input("Enter class ID: ").lower().replace(" ", "")

        elif "name" in id_or_name:
            identifier = input("Enter class name: ").lower().replace(" ", "")
            for i in classes:
                if classes[i]["name"].lower().replace(" ", "") in identifier:
                    identifier = i
                    break

        field_to_change = input("What field to change (name, desc): ").lower().replace(" ", "")
        while field_to_change != "name" and field_to_change != "desc":
            print("Try again")
            field_to_change = input("What field to change (name, desc): ").lower().replace(" ", "")

        value = input(f"What do you want to change the {field_to_change} to? ")

        classes[identifier][field_to_change] = value

    elif choice == "5":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        birthday = input("Enter birthday: ")
        grades = {}

        choice_grades = input("Would you like to enter grades? ").lower().replace(" ", "")
        if "yes" in choice_grades:
            pass

        students[first_name.lower()[:2] + last_name.lower()[:3]] = {
            "first_name": first_name,
            "last_name": last_name,
            "birthday": birthday,
            "grades": grades
        }
