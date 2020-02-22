
def is_seven(x):
    if(x % 7 == 0):
        return True
    else:
        return False


def list_numbers():
    for x in range(0, 100):
        if(is_seven(x)):
            print(x)


list_numbers()
