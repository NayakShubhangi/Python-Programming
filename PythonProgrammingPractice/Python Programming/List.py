# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = list1[10:3:-1]
# print(list2)
# print(list2[0:])
# print(list1[::-1])
# var = "string"
# var2 = var[::-1]
# if(var == var2):
#     print("This is a palindrome")
# else:
#     print("This is not a palindrome")
var3 = 172
list3 = []
while(var3 != 0):
    lastdigit = var3%10
    list3.append(lastdigit)
    var3 = var3//10
if(list3 == list3[::-1]):
    print("This is a palindrome")
else:
    print("This is not a palindrome")