def initials(phrase):
    if len(str(phrase)) > 0:
        words = phrase.split()
        result = ""
        for word in words:
            result = result + word[0]
        return result.upper()


print(initials("Universal Serial Bus"))
print(initials("local area network"))
print(initials("Operating System"))
