def guest_list(guests):
    for name, age, position in guests:

        print("{} is {} years old and works as {}".format(
            name, age, position))


guest_list([("ken", 30, "Chef"), ("Pat", 25, "Nightgirl")])
