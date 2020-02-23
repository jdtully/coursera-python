def factorial(n):
    print("factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning " + str(result) + " for the factorial of " + str(n))
    return result


factorial(4)
