

def first_last(message):
    if (len(message) > 0):
        if message[0] == message[-1]:
            return True
        else:
            return False
    return True


print(first_last("else"))
print(first_last("tree"))
print(first_last("I"))
print(first_last(""))
