def convert_distance(miles):
    km = miles*1.6
    result = "{} miles equals {:0.1f} km".format(miles, km)
    return result


print(convert_distance(12))
