# TEST 1
# Write a program to find whether the given strings are anagram or not
# str = "care"
# str2 = "race"
# str1 = input("Enter a first string: ").lower()
# str2 = input("Enter a second string: ").lower()
# if sorted(str1) == sorted(str2):
#     print("The two strings are anagrams.")
# else:
#     print("The two strings are not anagrams.")

# TEST 2
# Write a program to transpose the given matrix
# x = [[5, 9, 11, 12], 
#      [3, 6, 14, 15],
#      [9, 12, 11, 24]]
# output = [[5, 3, 9],
#           [9, 6, 12]]
# helper = [[0, 0, 0],
#           [0, 0, 0], 
#           [0, 0, 0],
#           [0, 0, 0]]
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         helper[j][i] = x[i][j]
# for i in helper:
#     print(i)

# TASK ONE:
# Write a program to multiply the given matrixes
# x = [[5, 9, 11], 
#      [3, 6, 14],
#      [9, 12, 11]]
# y = [[10, 5, 11], 
#      [4, 6, 13],
#      [9, 12, 41]]
# output2 = [[0, 0, 0], 
#            [0, 0, 0],
#            [0, 0, 0]]
# # (5 x 10) + (9 x 4) + (11 x 9) * should replace 10 in output2*
# # (5x5) + (9x6) + (11x12)
# for i in range(len(x)):
#     for j in range(len(y[0])):
#         for k in range(len(y)):
#             output2[i][j] += x[i][k] * y[k][j]
# for i in output2:
#     print(i)
# Formula for the first one is (x[0][0]*y[0][0] + x[0][1]*y[1][0] + x[0][2]*y[2][0])

# TASK TWO:
# Make below pattern:
#    *
#   ***
#  *****
# *******
# above is if n = 7 
# n = 12
# h = (n + 1) // 2
# for i in range(h):
#     stars = "*" * (n-2 * (h-i-1))
#     spaces = " " * ((n-len(stars)) // 2)
#     print(spaces + stars)

# Write a program to take multiple inputs in a single line
# If the string ends with "join", combine that string with the next one, then increase counter of joins
# EX: ABC HEFjoin 123 9876join
# OUTPUT: ABC HEF123 9876
# OUTPUT2: 1 join
# EX2: applejoin 23 46 1join join 19
# OUTPUT: apple23 46 119
# length = 14
# EX3: join join 123 96join join join 123 ABCjoin
# OUTPUT: 123 96123 ABC
# length = 13
# counter = 1
# EX4: 123 joinjoin join123 abcd join join 123join abc
# OUTPUT: 123 joinjoin123 abcd 123abc
# length = 27
# counter = 2
# a = [i for i in input().split()]
# result = ""
# counter = 0
# if a[-1][-4:].lower() == "join":
#     a[-1] = a[-1][0:-4]
# for i in a:
#     if i.lower() != "join":    
#         if i[-4:].lower() == "join":
#             i = i[0:-4]
#             result = result + i
#             counter += 1
#         else:
#             result = result + i + " "
# if result[-1] == " ":
#     result = result[0:-1]
# print(result)
# print(len(result))
# print(counter)
# EX 5: 123 join ABCjoin joinjoin 123join joinjoin
# OUTPUT RETURNED IS 123 ABCjoin123 (incorrect!!)
# OUTPUT length RETURNED IS 13
# OUTPUT counter RETURNED IS 3
# fix

# TASK ONE:
# Study the following functions with practical examples
# exec(), eval(), exit(), abs()
# exec(): 'Executes' Python code dynamically. By using it, you can execute code that wasn’t already defined when the
# program started, allowing your code to respond to inputs or other things. exec() does the operations for equations.
# exec() only works with one = (assignment operator), not a ==. It works with only one equation, not double equations.
# Example:
# code = """
# for i in range(3):
#     print("This is loop", i)
# """
# exec(code)
# print(exec("1+1==0"))
# print(eval("1+1"))
# print(exec("a=1+1"))
# print(a)

# TASK ONE
# Write a program to initialize the inputs provided by the user in a space-separated format given in a single line.
# EX: 1, -5, 3, 0, 1.5
# EX output: a=1, b=-5, c=3, d=0, e=1.5
# values = [val for val in input("Enter values separated by spaces: ").split()]
# for i, value in enumerate(values):
#     var_name = chr(97 + (i % 26))
#     print(f"{var_name} = {value}")
#     exec("eval(chr(97 + (i % 26))) = 1")
# print(a, b, c, d)


# TASK TWO
# Study the following topics and include practical examples
# deque, json, accumulate, leftshift, rightshift

# Deque is a double-ended queue that allows elements to be added or removed from both the front and back. It's useful when we need
# fast appending and popping operations from both the front and back of a list.
# Example:
# from collections import deque

# d = deque([1, 2, 3])
# d.append(4)
# d.appendleft(0)
# d.pop()
# d.popleft()
# print(d)
# Output: deque([1, 2, 3])

# Json (JavaScript Object Notation) is a lightweight data-interchange format that’s easy for humans to read and write, and easy for machines to
# parse and generate. It is used for sending and receiving data between a server and a client.
# Example:
# import json

# data = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# json_string = json.dumps(data)
# print(json_string)
# parsed_data = json.loads(json_string)
# print(parsed_data['name'])

# Accumulate is a function that returns accumulated sums or results of binary functions applied to an iterable.
# It is often used in data processing where you want a running total.
# Example:
# from itertools import accumulate
# import operator

# numbers = [1, 2, 3, 4]
# cumulative_sum = list(accumulate(numbers))
# print(cumulative_sum)
# cumulative_product = list(accumulate(numbers, operator.mul))
# print(cumulative_product)

# Leftshift is an operator (<<) that shifts the bits of a number to the left by the specified number of positions. It converts the number
# into binary, which is basically just 0s and 1s, and then performs the shifting. After the shifting, it converts the binary back into
# a number.
# It is used in cryptography, and in other places.
# Example:
# num = 5
# shifted = num << 1
# print(shifted)

# Rightshift is an operator (>>) that shifts the bits of a number to the right by the specified number of positions. It converts the number
# into binary, which is basically just 0s and 1s, and then performs the shifting. After the shifting, it converts the binary back into
# a number.
# It is used alongside leftshift in crytography, and in other places.
# Example:
# num2 = 20
# shifted2 = num2 >> 2
# print(shifted2)



# TASK TWO:
# Study the following modules with practical examples
# sys, platform, typing, json, math

# Sys is a module that has functions which are used for your system, which can be useful for interacting with the Python interpreter
# Example:
# import sys
# print("Beginning of program.")
# sys.exit()
# print("This will not be printed.")

# Platform is a module that gives information about the platform (OS, hardware, etc.)
# Example:
# import platform
# python_version = platform.python_version()
# print("Python Version:", python_version)

# Typing is a module that provides tools to specify types of variables and functions,
# which can make your code clearer and more reliable.
# Example:
# from typing import List

# def greet_all(names: List[str]) -> None:
#     for name in names:
#         print(f"Hello, {name}!")
# greet_all(["Alice", "Bob", "Charlie"])

# Math is a module that gives you math functions
# Example:
# import math
# result = math.sqrt(16)
# print(result)

# TASK THREE:
# Study the following libraries / modules
# itertools, functools, random, datetime
# Itertools is a module that gives tools to make looping iterators, and can perform operations on iterables.
# Example:
# import itertools

# items = ['A', 'B', 'C']
# pairs = list(itertools.combinations(items, 2))
# print(pairs)
# Functools is a module that provides functions that can operate on or return other functions.
# Example:
# from functools import reduce

# numbers = [1, 2, 3, 4]
# total = reduce(lambda x, y: x + y, numbers)
# print(total)
# Random is a module that gives functions that can generate 'randomized' things.
# Example:
# import random

# number = random.randint(1, 10)
# print(number)
# Datetime is a module that gives classes for manipulating dates and times, and it can be used to get the current date and time.
# Example:
# from datetime import datetime

# now = datetime.now()
# print(now)

# TASK FOUR:
# Give three different ways to write a hello world program
# def greet():
#     print("Hello, World!")

# greet()
# print("Hello, world!")
# name = "World"
# print(f"Hello, {name}!")
# import __hello__



# TASK FIVE:
# Understand concept and explain with practical examples
# Walrus (Python operator)
# The walrus operator (:=) allows you to assign a value to a variable as part of an expression.
# This can make your code more concise by combining assignment and expression evaluation in a single line.
# Example:
# data = [5, 12, 15, 20, 25]
# threshold = 15
# filtered_data = []
# for number in data:
#     if (n := number) > threshold:
#         filtered_data.append(n)
# print(filtered_data)

# TASK SIX:
# FIBONACCI
# 0 1 1 2 3 5
# if n = 20, return ONLY the nth fibonacci number from chain (don't include the chain itself)
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     a, b = 0, 1
#     for i in range(2, n + 1):
#         a, b = b, a + b
#     return b
# fibonacci = fibonacci(5)
# print(fibonacci)






# TASK ONE:
# Study zfill, rstrip, rjust, ljust, encode, partition, strip, split (BUILT-IN FUNCTIONS)
# zfill() adds zeros at the beginning of the string, until it reaches the specified length
# x = "100"
# print(x.zfill(5))

# rstrip() removes trailing characters, and removing trailing spaces is its default
# y = "gstringgggggggg"
# y = y.rstrip("g")
# print(y)
# print(len(y))

# rjust() right aligns the string, using a specified character (space is the default) as the fill character
# z = "strings"
# z = z.rjust(9, "g")
# print(z)

# ljust() left aligns the string, using a specified character (space is the default) as the fill character
# z = "strings"
# z = z.ljust(9, "g")
# print(z)

# encode() encodes the string, using the specified encoding (UTF-8 will be used as the default if none is specified)

# partition() searches for a specified string, and splits the string into a tuple containing three elements
# a = "abCstringCba"
# a = a.partition("string")
# print(a)

# strip() removes leading and trailing whitespace characters from a string
# b = "    strings  "
# b = b.strip()
# print(b)
# print(len(b))

# split() splits a string into a list by using a specified separator (whitespace is the default)



# Question:- There are n houses build in a line, each of which contains some value in it.
# A thief is going to steal the maximal value of these houses,
# but he can't steal in two adjacent houses because the owner of the stolen houses will tell his two neighbours left and right side.
# What is the maximum stolen value?
# Sample Input: val[] = {6, 7, 1, 3, 8, 2, 5}
# Sample Output: 20

def calcMaxStealVal(houseVal):
    routeOne = houseVal[::2]
    routeTwo = houseVal[1::2]
    routeOneSum = sum(routeOne)
    routeTwoSum = sum(routeTwo)
    return max(routeOneSum, routeTwoSum)

# print(calcMaxStealVal([6, 7, 1, 3, 8, 2, 5]))

# Q1. Write a Python code to print the position or index of a given string (taken as input from a user) from a given list of strings.
# Ans. The program will take input from the user in the form of a string and will pass the string as an argument to a function.
# The function will take the strings as arguments and return the Position(or index) of the list if the passed string is present
# in the list, else it'll return "String not found". If the passed strings are present at multiple indices, in that case,
# the function should only return The first index of occurrence. Considering the above scenario into account,
# build the logic to print the position of the passed string from a given list of strings.
# account, build the logic to print the position of the passed string from a given list of strings. 
# Refer to the below instructions and sample input-Output for more clarity on the requirement.
# Input:
# 4
# Hello Good Morning
# abcd123Fghy
# India
# Progoti.c

# India

# Output:
# The position of the searched string is: 2

def stringIndexFinder():
    inputNum = int(input("Enter the number of inputs: "))
    inputList = []
    for i in range(inputNum):
        inputList.append(input(f"Enter input string {i+1}: "))
    searchStr = input("Enter a string to search for: ")
    if searchStr in inputList:
        return f"The position of the searched string is: {inputList.index(searchStr)}"
    else:
        return "String not found"

# print(stringIndexFinder())

# Q5. Write a Python program to calculate the salary of the temporary staff using Multilevel Inheritance.
# Description:
# Create a class Person which contains a constructor__init__() and a method display(self).
# The method displays the name of the person
# Create another class Staff which inherits Person.
# It contains a constructor __init__() and a method display(self).
# The method displays Id.
# Create another class Temporarystaff which inherits Staff, it also contains a constructor __init__() and two method displays (self),
# and Salary(self).
# The method Salary(self) returns the total salary earned.
# The method display(self) displays a number of days, hours worked and total salary earned.
# salary earned = total hours worked *150

# Input Format:
# String => name
# Integer => Id
# Integer => number of days
# Integer => hoursworked

# Output Format:
# All outputs contain strings and integers.

# Sample Input:
# Tilak
# 157934
# 20
# 8

# Sample Output:
# Name of Person = Tilak
# Staff Id is = 157934
# No. of Days = 20
# No. of Hours Worked = 8
# Total Salary = 24000
# Case 1
# Case 2

class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name of Person = {self.name}")

class Staff(Person):
    def __init__(self, name, idNum):
        super().__init__(name)
        self.id = int(idNum)

    def display(self):
        super().display()
        print(f"Staff Id is = {self.id}")

class Temporarystaff(Staff):
    def __init__(self, name, idNum, daysNum, hoursWorked):
        super().__init__(name, idNum)
        self.daysNum = int(daysNum)
        self.hoursWorked = int(hoursWorked)

    def Salary(self):
        return self.daysNum * self.hoursWorked * 150

    def display(self):
        super().display()
        print(f"No. of Days = {self.daysNum}")
        print(f"No. of Hours Worked = {self.hoursWorked}")
        print(f"Total Salary = {self.Salary()}")

# if __name__ == '__main__':
#     name = input("Name: ")
#     id_num = input("Id: ")
#     days = input("Days: ")
#     hours = input("Hours worked: ")

#     temp_staff = Temporarystaff(name, id_num, days, hours)
#     temp_staff.display()

# THREE: (DONE)
# Figure out how to fix the above question about the temporarystaff stuff,

# It returns:
# Name: Tilak 
# Id: 157934
# Days: 20
# Hours worked: 8
# Name of Person = Tilak
# Staff Id is = 157934
# No. of Days = 20
# No. of Hours Worked = 8
# Total Salary = 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

# Instead of:
# Name of Person = Tilak
# Staff Id is = 157934
# No. of Days = 20
# No. of Hours Worked = 8
# Total Salary = 24000

# In this example, it says that to find the total salary, you multiple 8 by 150.
# HOWEVER, where does 24000 come from?? 8*150 = 1200
# FIGURED IT OUT: Days * Hours * 150!!


# FOUR (DONE):
# Use just one class object instead of three for the above since we're inheriting the other two classes.
# (Hint: use super() to call a parent class method. Probably just add the parameters of the other two classes to the child function)

# FIVE (DONE):
# Q6. Write a Python program to check the quantity of petrol in the bike using exception handling.
# If there is no petrol i.e. null in the bike it should raise an exception.
# That exception is handled by using except block and it should print “There is no fuel in the bike”. Otherwise, it should the show quantity of petrol on the bike.
 
# Input Format:
# The input consists of a string which denotes a fuel.

# Output Format: 
# Output is a String

# Sample Input: 
# 40

# Sample Output: 
# Petrol Quantity = 40
# Case 1
# Case 2

# Input (stdin)
# 40

# Output (stdout)
# Petrol Quantity =  40

# Input (stdin)
# NulL

# Output (stdout)
# There is no fuel in the Bike

def bikePetrolCheck():
    try:
        fuel = input("Enter the amount of fuel in the bike: ").strip()
        if fuel.lower() == "null":
            raise ValueError("No fuel")
        print("Petrol Quantity = ", fuel)
    except ValueError:
        print("There is no fuel in the bike")

# bikePetrolCheck()

# SIX (DONE):
# Write a Python program to display the Passport details of the Person using composition.
# Description:
# Create a class Passport and class Person. Compose the class Passport in the class Person.
# Class Passport contains constructor __init__() which sets the name, address and passport no.
# Display the name of the person, Address and passport number of the person.

# Input Format:
# Name => String
# Address => String
# passport number => String
 
# Output Format:
# Three outputs. All are String

# Sample Input:
# RamKumar
# Kollam
# J7546891
 
# Sample Output:
# Name: RamKumar
# Address: Kollam
# Passport Number: J7546891
# Case 1
# Case 2

# Input (stdin)
# RamKumar
# Kollam
# J7546891

# Output (stdout)
# Name: RamKumar
# Address: Kollam
# Passport Number: J7546891

# Input (stdin)
# Purushothaman
# Mumbai
# J1535231
 
# Output (stdout)
# Name: Purushothaman
# Address: Mumbai
# Passport Number: J1535231

# Create a class Passport and class Person. Compose the class Passport in the class Person.
# Class Passport contains constructor __init__() which sets the name, address and passport no.
# Display the name of the person, Address and passport number of the person.

# Input Format:
# Name => String
# Address => String
# passport number => String

class Person:
    class Passport:
        def __init__(self, name, address, passportNo):
            self.name = name
            self.address = address
            self.passportNo = passportNo
        def display(self):
            print(f"Name: {self.name}")
            print(f"Address: {self.address}")
            print(f"Passport Number: {self.passportNo}")

# person1 = Person().Passport("Purushothaman", "Mumbai", "J1535231")
# person1.display()