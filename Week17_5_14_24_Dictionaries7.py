# Grade Management Program

students = []
classes = {}

choice = ""

print("Welcome to the grade management program!")

while choice != "9":
    print('''Select an option:
1. Add a student
2. Remove a student
3. Update a student
4. View a student
5. Add a class
6. Remove a class
7. Update a class
8. View a class
9. Quit
''')

    choice = input("> ")

    if choice == "1":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        birthday = input("Enter birthday: ")
        grades = {}

        choice_grades = input("Would you like to enter grades? ").lower().replace(" ", "")
        if "yes" in choice_grades:
            pass

        students.append({
            "first_name": first_name,
            "last_name": last_name,
            "birthday": birthday,
            "grades": grades
        })
