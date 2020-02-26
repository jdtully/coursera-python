def convert_to_celcius(x):
    return (x-32)*5/9


for x in range(0, 101, 10):
    # whats  the  benefit of  string concatenation when this works?
    print("{:>3}F | {:>6.5f}C ".format(x, convert_to_celcius(x)))
