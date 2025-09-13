# for i in range(10):
#     print(i)

# list1 = [1, 2, 3]
# for i, j in enumerate(list1):
#     print(i, j)

# var1 = [i for i in input("Enter a value: ").split("*")]
# print(var1)
# One, two, three
# 1 2 3
# String*Str*Num

# list2 = ["One", "Two", "Three"]
# list2[0] = "Four"
# list2.append("Five")
# list2.insert(2, "Six")
# print(list2)

list3 = ["Num", "String", "Str", "Num"]
# list2.append(list3)
# print(list2)
# list2.extend(list3)
# print(list2)

# print(list3.remove("Num"))
# print(list3.pop())
# list3.pop(1)
# print(list3)

# print(len(list3))
# for i in range(len(list3)):
#     print(list3[i])

# del list3
# print(list3)

# print(list3.sort(reverse=True))
# print(list3)

# list4 = ["Apple", "Mango", "Bananna"]
# def Function1(parameter):
#     return parameter[-1]
# list4.sort(key=Function1)
# print(list4)

# def Function2(parameter):
#     return parameter[1]
# list4.sort(key=Function2)
# print(list4)

# print(sorted(list4))

list5 = ["1", "2", "3", "1", "2", "5", 7, 8, 9]
list6 = ["5", "7", "9"]
list5.extend(list6)
list7 = list5+list6

# string1 = "String"
# print(string1.join(list5))
# print(string1)

print(list5.count("1"))

# var2 = "Variable"
# print(var2[-1])

# tuple1 = ("String", "Str", "Num")
# tuple[0] = "Number"