def is_palindrome(input):
    new_string = ""
    reversed_string = ""
    wordlist = input.split()
    new_string = new_string.join(wordlist)
    new_string = new_string.lower()
    for letter in new_string:
        reversed_string = letter + reversed_string

    if new_string == reversed_string:
        return True

    return False


print(is_palindrome("a rat in the house"))
print(is_palindrome("a man a Plan a canal panama"))
print(is_palindrome("abc"))
