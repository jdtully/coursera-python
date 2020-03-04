tmp = input("what is  the temp?")
temp = int(tmp)


def is_hot(tmp):
    if temp > 70:
        return(" its hot")
    else:
        return("its not")


print(is_hot(input))
