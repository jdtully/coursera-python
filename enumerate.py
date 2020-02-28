def skip_elements(elements):
    list = []

    for index, value in enumerate(elements):

        if (index % 2 == 0):
            list.append(value)
    return list

# return [x for x in elements if elements.index(x) % 2 == 0]


# def skip_elements(elements):
#     y = []
#     for index, obj in enumerate(elements):
#         if (index % 2 == 0):
#             y.append(obj)
#     return y


# Should be ['a', 'c', 'e', 'g']
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))
