# func = lambda i: i % 2 != 0
# list1 = [1, 3, 4, 2, 9]
# list2 = list(filter(func, list1))
# print(list2)

# list3 = ["Fruit", "Apple", "Grape", "Orange", "String"]
# func2 = lambda i: i[-2] == "g"
# list4 = list(filter(func2, list3))
# print(list4)

# func3 = lambda i: len(i) == 5
# list5 = list(filter(func3, list3))
# for i in list5:
#     findIndex = list3.index(i)
#     list3[findIndex] = "Apple"
# print(list3)


list6 = ["One", "Ball", "Random", "Length", "Map", "Filter", "Reduce", "e"]
# func4 = lambda i: i.replace("Random", "Two")
# list7 = list(map(func4, list6))
# print(list7)

var = list(filter(lambda i: i[-1] == "e", list6))
var2 = list(map(lambda i: "Today" if i[-1] == "e" else i, list6))
print(var2)

# a = a + b
# a - b
# a == b + 2
# a.replace(1, 2)
# If Expression, use Map()
# If Equation, use Filter()