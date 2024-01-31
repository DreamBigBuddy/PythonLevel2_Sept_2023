def countdown(n):
    print(n)

    if n == 0:
        return

    return countdown(n-1)

countdown(5)


def addUpNumbers(n):
    if n == 0:
        return 0

    return n + addUpNumbers(n - 1)

print(addUpNumbers(100))


def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)

print(factorial(5))
