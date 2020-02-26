def calc_tax(price):
    tax = price*.05
    total = price + tax
    return tax, total


print(calc_tax(25.00))
