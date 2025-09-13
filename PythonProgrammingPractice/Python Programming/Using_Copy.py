import copy

# There is two kinds of copying: Shallow copying and deep copying
# The default is shallow copy, and we have to specify to use deep copy
# Shallow copying copies the top-level elements, but not the nested elements or objects
# Deep copying copies everything (including nested objects), but when the original list is changed, it stays the same
list1 = [1, 5, "Apple", [928, 29, False], 93.25]
list2 = list1.copy()
list5 = copy.deepcopy(list1)
# print(list1)
# print(list2)
list1[1] = 9
# print(list1)
# print(list2)
list1[3][2] = True
# print(list1)
# print(list2)

# list comprehension
list3 = [id(i) for i in list1]
# print(list3)
list4 = [id(i) for i in list2]
# print(list4)

print(list1)
print(list5)