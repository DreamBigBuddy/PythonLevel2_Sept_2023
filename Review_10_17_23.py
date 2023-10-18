# Word Stitcher
user_input = input("Enter some phrase/words: ")

message = ""

while user_input != "stop" and len(message) < 200:
    message += user_input + "\n"
    user_input = input("Enter some phrase/words: ")

print(message)

# While Loop Examples
password = "vaman"

user_input = input("Enter the password: ")

while user_input != password:
    print("Incorrect! Try again")
    user_input = input("Enter the password: ")

print("Correct!")

# Error Handling
try:
    a = int(input("Enter a number: "))

except:
    print("Invalid input")

# Operation Check
operations = ["+", "-", "*", "/"]
op = "e"

if op in operations:
    print("True")
else:
    print("False")

# Print Emojis
# Go to https://lingojam.com/EmojitoUnicodeConverter
# Put in an emoji and copy the unicode value (not the U+)
# Print it in Python by doing this
# print("\U000unicode") where unicode is the value you copied
# Ex: print("\U0001f603") ----> 😃
