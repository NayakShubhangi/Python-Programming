# def returnValues(list):
#     for i in list:
#         return i
list1 = [1, 2, 3, 5, 8]
# print(returnValues(list1))


# returnvalues = lambda i: i[0]
# print(returnvalues(list1))
def incrementOne(lst):
    return list(map(lambda i: i + 1, lst))
var = incrementOne(list1)
print(var)