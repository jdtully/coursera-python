def sort_animals(group, animals):
    pets = ", ".join(animals)
    return group + ":" + pets


print(sort_animals("dogs", ["benjamin", "cali",  "ella"]))
print(sort_animals("cats", ["fluffy", "opal", "misty"]))
