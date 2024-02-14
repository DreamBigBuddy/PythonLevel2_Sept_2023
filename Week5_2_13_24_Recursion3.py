def reverseString(s):
    if len(s) == 1 or len(s) < 1:
        return s

    return s[-1] + reverseString(s[:-1])

string = input("Enter a phrase: ")
print(reverseString(string))
