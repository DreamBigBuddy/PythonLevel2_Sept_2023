# Syntax Errors
print(")
print())

# Index Error
my_list = [1, 2, 3, 4]
print(my_list[-4])

# Value Error
my_input = int(input("Enter a number: "))
# If the user puts in anything other than a number,
# it will throw a value error because the value cannot
# be converted to a number

# Division By Zero Error
print(1/0)

# Name Error
print(name) # Variable does not exist

# Catching errors
try:
    grade = float(input("Enter a grade: "))

except:
    print("Invalid input")


# Grade Calculator 
grades = []
total = 0
grade = 0

while grade >= 0:
    try:
        grade = float(input("Enter a grade: "))
        total += grade
        grades.append(grade)

    except:
        print("Invalid input")
        grade = 0

average = total/len(grades)

above_90 = []
for i in grades:
    if i >= 90:
        above_90.append(i)

print(f"Average: {average}")
print(f"A Grades: {above_90}")
