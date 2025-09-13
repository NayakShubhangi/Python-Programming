# tuple1 = (1, "Two", True)
# list1 = [2, "Three", False]
# a = 1,
# print(type(a))

tuple2 = ("Apple", "Bananna", "Apple", "Orange")
def FindDuplicate(parameter):
    list1 = []
    for i in range(len(parameter)):
        if (parameter.count(parameter[i])>1):
            list1.append(parameter[i])
    return list1
print(FindDuplicate(tuple2))

# print(tuple2.count("Apple"))