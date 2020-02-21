def convert_to_celcius(x):
    return (x-32)*5/9


for x in range(0, 101, 10):
    # whats  the  benefit of  string concatenation when this works?
    print(x, " In celcius is : ", convert_to_celcius(x))
