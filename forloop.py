values = [25, 36, 95, 74, 624]
# initialize variabbles
sum = 0
length = 0
# start looper
for value in values:
    # add each value  to sum and count how many there are
    sum += value
    length += 1
print("the total is: " + str(sum)+" The average is : " + str(sum/length))
