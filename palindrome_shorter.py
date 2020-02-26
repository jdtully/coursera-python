def is_palindrome(input):
    new_string = ""
    reversed_string = ""
    new_string = input.replace(" ", "")
    new_string = new_string.lower()
    reversed_string = new_string[::-1]

    if new_string == reversed_string:
        return True

    return False


print(is_palindrome("a rat in the house"))
print(is_palindrome("a man a Plan a canal panama"))
print(is_palindrome("abc"))
