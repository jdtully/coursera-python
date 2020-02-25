def double_word(word):

    double = word + word
    length = len(double)
    doubled = double + str(length)
    return doubled


print(double_word("hello"))  # sb hellohello10
print(double_word("abc123"))  # sb abc123abc12312
print(double_word(""))  # sb 0
