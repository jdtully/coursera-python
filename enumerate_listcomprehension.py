
def skip_elements(elements):
    z = [value for x, value in enumerate(elements) if x % 2 == 0]

    return(z)


print(skip_elements(["a", "b", "c", "d", "e", "f"]))
