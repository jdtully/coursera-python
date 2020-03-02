import timeit
list_test = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]", number=1000)

print("List time:", list_test)
