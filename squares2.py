def squares(start, end):
    end1 = end + 1
    nums = []

    for x in list(range(start, end1)):
        nums.append(str(x))

    return(x)


print(squares(2, 3))  # Should be [4, 9]

print(squares(1, 5))  # Should be [1, 4, 9, 16, 25]

# Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(squares(0, 10))
