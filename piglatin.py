def pig_latin(text):
    say = ""
    words = text.split()

    for word in words:
        cropped = word[1:] + word[0] + "ay "

        say += cropped
    return str(say)


print(pig_latin("hello how are you"))
