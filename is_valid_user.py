def calculate_cubes(n):
    result = 0

    for x in range(0, n):
        result = x**3
    return result


for n in range(10):
    print(calculate_cubes(n))
