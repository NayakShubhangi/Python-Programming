# list1 = ["Text", 4, 6.5, True, 3+4j]
# result = str(list1)
# print(result)
# print(len(result))
# print(list(result))
# "['Text', 4, 6.5, True, (3+4j)]"
# 30


# list2 = [1, 2, 3, 4, 5]
# for i in list2:
#     list2.remove(i)
#     print(list2)
# [2, 3, 4, 5]
# [2, 4, 5]
# [2, 4]


# list3 = [1, 2, 3]
# list4 = list3       # list4 is a copy of list3 (equivalent to list4 = list3.copy())
# print(list3 is list4)     # True
# print(list3 == list4)     # True
# list5 = list3[:]    # list5 just has the values from list3 (is not a copy)
# print(list5 is list3)     # False
# print(list5 == list3)     # True
# list3.append(4)
# print(list4)     # [1, 2, 3, 4] (Same address, is a copy)
# print(list5)     # [1, 2, 3]    (Not same address, not a copy)


# print(bool([]))     # False
# print(bool(""))     # False
# print(bool(0))      # False
# print(bool(None))   # False
# print(bool(False))  # False
# print(bool("True")) # True


# def append_list(x, list=[]):
#     list.append(x)
#     return list

# print(append_list(1))     # [1]
# print(append_list(2))     # [1, 2]
# print(append_list(3, [])) # [3]
# print(append_list(4))     # [1, 2, 4]


# x = [[0]*3]*3
# x[0][0] = 1
# print(x)     # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# print((False or False) and True)     # False
# print(False or (False and True))     # False


# TASK ONE:
print("Hello"*3*0)
print("Hello"*(3*0))
# expected output and why:
# *nothing
# *nothing
# The first line is because you get "HelloHelloHello" with "Hello"*3, but then that result *0 = 0
# The second line is because 3*0 = 0, so Hello gets printed 0 times

# TASK TWO:
class teSt:
    var = 10
    def __init__(self):
        self.var = 20

# print(teSt().var, teSt.var)
# expected output and why:
# 20 10
# teSt().var refers to/calls the class, so the constructor's variable is called, while teSt.var refers to the class's variable

# TASK THREE in inheritance.py

# TASK FOUR:
# create a function that prints the current datetime              |
# it should be scheduled to print every 15 minutes of the day     V
                                                            # NOTE:
                                                            # import datetime module
                                                            # datetime.now
import datetime
import schedule

def printDatetime():
    print("Current Date and Time:", datetime.datetime.now())

schedule.every(15).minutes.do(printDatetime)
while True:
    schedule.run_pending()

# TASK FIVE:
# dunder method (__something__) and dunder variables
# Give 5 dunder methods and variables
# Dunder Methods:
# 1: __init__ (the constructor of a class) (initializes the object's attributes)
# 2: __repr__ (returns string representation of the object which can be used to recreate it)
# Dunder Variables:
# 3: __name__ (where the name of a class or function is stored)
# 4: __dict__ (where the attributes of the class of function is stored)
# 5: __class__ (where the class of the object's attribute is stored)

# TASK SIX in Application.py -> Controller.py


