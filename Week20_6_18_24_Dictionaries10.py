students = {}
classes = {}

choice = ""

print("Welcome to the grade management program!")

while choice != "9":
    print(
        """Select an option:
1. Add a class
2. Remove a class
3. Update a class
4. View a class
5. Add a student
6. Remove a student
7. Update a student
8. View a student
9. Quit
"""
    )

    choice = input("> ")

    if choice == "1":
        name_of_class = input("Enter the name of the class: ")
        description_of_class = input("Enter the description of the class: ")

        classes[name_of_class[:3].lower().replace(" ", "")] = {
            "name": name_of_class,
            "desc": description_of_class,
            "students": 0,
        }

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

        field_to_change = (
            input("What field to change (name, desc): ").lower().replace(" ", "")
        )
        while field_to_change != "name" and field_to_change != "desc":
            print("Try again")
            field_to_change = (
                input("What field to change (name, desc): ").lower().replace(" ", "")
            )

        value = input(f"What do you want to change the {field_to_change} to? ")

        classes[identifier][field_to_change] = value

    elif choice == "4":
        classes_view = (
            input("What field would you like to view the class by?(name,desc):")
            .lower()
            .replace(" ", "")
        )

        key = input(f"Enter {classes_view}:").lower().replace(" ", "")

        for i in classes:
            if classes[i][classes_view] == key:
                print(classes[i])

    elif choice == "5":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        birthday = input("Enter birthday: ")
        grades = {}

        choice_grades = (
            input("Would you like to enter grades? ").lower().replace(" ", "")
        )
        if "yes" in choice_grades:
            classes_input = "sample"
            while classes_input != "":
                classes_input = (
                    input("Enter the class id or name: ").lower().replace(" ", "")
                )
                while (
                    classes_input != ""
                    and classes_input not in classes
                    and classes_input not in [classes[i]["name"] for i in classes]
                ):
                    print("Invalid class id/name")
                    classes_input = (
                        input("Enter the class id or name: ").lower().replace(" ", "")
                    )

                for i in classes:
                    if classes[i]["name"] == classes_input:
                        classes_input = i

                grade = int(input("Enter the grade: "))

                grades[classes_input] = grade
                classes[classes_input]["students"] += 1

        students[first_name.lower()[:2] + last_name.lower()[:3]] = {
            "first_name": first_name,
            "last_name": last_name,
            "birthday": birthday,
            "grades": grades,
        }

    elif choice == "6":

        entry = (
            input(
                "What field would like to remove a student with(first name,last name,birthday)?:"
            )
            .lower()
            .replace(" ", "")
        )

        while entry != "first name" and entry != "last name" and entry != "birthday":

            print("Try again!")

            entry = (
                input(
                    "What field would like to remove a student with(first name,last name,birthday)?:"
                )
                .lower()
                .replace(" ", "")
            )

        key = input(f"Enter the student's {entry}:").lower().replace(" ", "")

        student = None
        for i in students:

            if students[i][entry] == key:

                student = students.pop(i)

                break

        if student is None:
            print("Invalid student")

        else:
            for i in student["grades"]:
                classes[i]["students"] -= 1

            print("Student removed!")

    elif choice == "7":

        entry = input(
            "What field would you like to update a student with(first name,last name,birthday,grades)?"
        )

        while (
            entry != "first name"
            and entry != "last name"
            and entry != "birthday"
            and entry != "grades"
        ):

            print("Try again!")

            entry = input(
                "What field would you like to update a student with(first name,last name,birthday,grades)?"
            )

        if entry == "grades":
            student = (
                input("Enter the student to update (id or name): ")
                .lower()
                .replace(" ", "")
            )
            while student not in students and student not in [
                students[i]["name"] for i in students
            ]:
                print("Invalid student id/name")
                student = (
                    input("Enter the student to update (id or name): ")
                    .lower()
                    .replace(" ", "")
                )

            grade_choice = ""
            while grade_choice != "4":
                print(
                    """Select an option:
1. Add a grade
2. Remove a grade
3. Update a grade
4. Quit Grade Menu"""
                )

                if grade_choice == "1":
                    pass

                elif grade_choice == "2":
                    pass

                elif grade_choice == "3":
                    pass

        field = input(f"Enter the student's {entry}:")

        for i in students:

            if students[i][entry] == field:

                new = input(f"Enter new {entry}:")

                students[i][entry] = new

                break

        print("student successfully updated!")

    elif choice == "8":

        entry = input(
            "What field would you like to view a student with?(first name,last name,birthday,grades)?"
        )

        key = input(f"Enter {entry}:")

        for i in students:

            if students[i][entry] == key:

                print(students[i])

                break
