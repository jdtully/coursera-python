def first_last(message):
    try:
        if message[0] == message[-1]:
            return True
        else:
            return False
    except IndexError:
        return True


print(first_last("else"))
print(first_last("tree"))
print(first_last("I"))
print(first_last(""))
