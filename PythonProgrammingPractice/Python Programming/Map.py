# power = lambda i: i**2
list1 = [1, 3, 5, 7, 2]
# list2 = list(map(power, list1))
# print(list2)

increment = lambda i: i+1
varlist = list(map(increment, list1))
print(varlist)