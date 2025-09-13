# Ex: 5 -> Square each number starting from 1 to 5 and add together -> Subtract by 100
# -> If negative, print that it's negative -> If positive, add 500 and then cube the result
# Input is integer

# def process_number(n):
#     total = sum(i ** 2 for i in range(1, n + 1))
#     result = total - 100
#     if result < 0:
#         print("The result is negative.")
#     else:
#         result += 500
#         result = result ** 3
#     return result

# user_input = int(input("Enter an integer: "))
# print(process_number(user_input))

# list1 = [1, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 6, 7, 8]
# def findOccurences(list):
#     set1 = set(list)
#     for i in set1:
#         print(f"{i} - {list.count(i)}")

# findOccurences(list1)

# list2 = [[3, 5, 9, 2, 6, -1, "Hello", 33.5], [5, 6, 7, "Mango", -6, 0.0], ["Hello", 2, 3, 5, 7]]

# # Ex: 5 -> Where there is 5 in the list, the suffix of the value should be changed with a different input value, which is also an integer.
# # Ex (Other value): 7 -> Suffix value is replaced with 7.

# list2 = [[3, 5, 9, 2, 6, -1, "Hello", 33.5], [5, 6, 7, "Mango", -6, 0.0], ["Hello", 2, 3, 5, 7]]
# list3 = [[1, -9, 0, "Apple"], [33, 2, 24, "Ball"]]
# user_input = input("Enter two numbers separated by a space: ").split()
# lookup = int(user_input[0])
# replacement = int(user_input[1])
# def func1(lst, lookup, replacement):
#     for i in lst:
#         seen = set()
#         unique_i = []
#         for current_index, item in enumerate(i):
#             if item == lookup and current_index + 1 < len(i):
#                 i[current_index + 1] = replacement
#             if item not in seen:
#                 seen.add(item)
#                 unique_i.append(item)
                
#         i[:] = unique_i
#     return lst


# print(func1(list3, lookup, replacement))

# import os

# var = os.path.exists("index.html")
# print(var)
# dictstr = """dict = {
#                   "name": name,
#                   "username": username,
#                   "password": password
#             }"""
# dictstr = dict(dictstr)
# print(dictstr)

# def readfunc(filename):
#     openfile = open(filename, "r")
#     contentFile = openfile.readlines()
#     print(contentFile)
#     openfile.close()

# readfunc("variables.txt")

# name: Pari
# username: Pari2012
# password: Something

# names = ["name: Pari", "name: something"]
# dict = {}
# dict.add(names[0][:5], names[1][:5])

# chances = 2
# a = False
# while chances != 0:
#     a = False
#     if a:
#         break
#     else:
#         chances-=1
# else:
#     print("This is else")
# import os

# print(help(os))

# def f(x):
#     def f1(*args, **kwargs):
#            print("Sanfoundry")
#            return x(*args, **kwargs)
#     return f1



# x = float(2.8)
# print(type(x))


# y = "    helo   "
# print(y.strip())


# print(33==33.0)
# print(1.0+2.0==3.0)
# print(0.1+0.2==0.3)


# for i in range(100, -1, -2):
#     print(i)
    # 100, 0, -2

# print(pow(2, 2, 2))
# print(pow(a, b, c))
# (a**b)%c

# a = [all(i) for i in range(10)]    # Range starts from 0 and doesn't include last number
# all() evaluates whether ALL of the passed elements of an iterable are True or not
# i is not iterable, and error is given

# a = [bool(i) for i in range(10)]
# print(all(a))
# a is an iterable, since it is a list
# print(any(a))
# any() evaluates whether ANY of the passed elements of an iterable are True
# any() evaluates bool(element) from the interable

# a = int(float(int(all(any((-1, "abc", False, 0+3j, 200))))))
# any((-1, "abc", False, 0+3j, 200))
# any((True, True, False, True, True)) -> True
# all(True) -> Error (not iterable)

# a = int(float(int(all([any((-1, "abc", False, 0+3j, 200))]))))
# print(a)

# def Func1():
#     print("Func1")
#     Func1()
#     return 0

# print(Func1())

# Print numbers 1 to n (where n is an int) using recursive function (with no loops and not simply using print("1") print("2") and so on...)
# def print_numbers(n):
#     if n > 0:
#         print_numbers(n - 1)
#         print(n)

# print_numbers(10)


# TASK OTHER ONE (two)
# Take 2 inputs from user through eval()
# print type() of each
# concatenate them
# if error, then handle that with try and except through custom error message (BOTH ERRORS ARE TYPEERROR FOR STR AND INT, AND STR AND FLOAT)
# MUST TELL THE DIFFERENCE BETWEEN THE INT AND THE FLOAT AND PRINT MESSAGE BASED ON THAT

# try:
#     input1 = eval(input("Enter first value: "))
#     input2 = eval(input("Enter second value: "))
#     print("Type of first input:", type(input1))
#     print("Type of second input:", type(input2))
#     result = input1 + input2
#     print("Concatenated result:", result)
# except TypeError:
#     print("You cannot concatenate a string with an integer")
# except 

# def main():
#     try:
#         input1 = eval(input("Enter first value: "))
#         input2 = eval(input("Enter second value: "))
#         print("Type of first input:", type(input1))
#         print("Type of second input:", type(input2))
#         result = input1 + input2
#         print("Concatenated result:", result)
#     except TypeError as e:
#         if isinstance(input1, str) and isinstance(input2, int):
#             print("Error: You cannot concatenate a string with an integer.")
#         elif isinstance(input1, str) and isinstance(input2, float):
#             print("Error: You cannot concatenate a string with a float.")
#         elif isinstance(input1, int) and isinstance(input2, str):
#             print("Error: You cannot concatenate an integer with a string.")
#         elif isinstance(input1, float) and isinstance(input2, str):
#             print("Error: You cannot concatenate a float with a string.")
#         else:
#             print("TypeError:", str(e))
#     except Exception as e:
#         print("An error occurred:", str(e))
# main()


# TASK OTHER (four)
# print(0.1+0.2==0.3)
# Why does program return False even though 0.1+0.2=0.3?
# EXPLAIN
# When representing 0.1 and 0.2 in binary, there is a rounding error, and because of that,
# adding them together leads to a value that is close, but not the same as 0.3 itself.

# TASK MORE (five)
# other thing: research what all of the things in postman do (like patch and delete and such...) + explore!!
# GET - Retrieves data from a server.
# POST - Send data to a server to create or update a resource.
# PUT - Replaces an existing resource with updated data. (Any data not included in the request is deleted, while new data included is added)
# PATCH - Updates specific properties of a resource without overwriting the others.
# DELETE - Removes data from a database or resource on a server. (Deletes it)
# HEAD - Requests information about a document without returning the document itself. (Similar to GET, but while
# GET retrieves the full data from the server, including the response body,
# HEAD only retrieves the response headers (additional information) without the actual data)
# OPTIONS - Gets information about the supported methods and headers of an API. (Basically the "help" command)




# TASK ONE
# Github keywords
# Pull request, conflicts, merging, cloning, checkout, rebase, fork
# Pull request - A proposal to merge changes from one branch into another branch
# - Combination of comparison and merging
# Conflicts - Something that occurs when two or more developers make different changes to the same file or line of code from different branches
# Merging - The process of combining changes from two or more branches into a single branch
# Cloning - The process of creating a local copy of a repository on your computer
# Checkout - A command that allows users to switch between branches or commits in a LOCAL repository
# Rebase - A command that allows users to change the base of a branch from one commit to another
# Fork - A copy of a repository that allows users to make changes without affecting the original repository



# TASK TWO
# fix issue with class





# TASK ONE
# Take multiple inputs in a single line (space separated)
# EX: abcdadjust ab bcd 12345adjust
# 4 2 3 5
# expected output: abcdd abbbb bcddd 12345
# convert all inputs to length of (5)
# EX2: abc adjust adjust abcadjust adjustab
# expected output: abccc abccc abbbb
# if adjust is in the word, it shouldn't be counted (meaning that it shouldn't show in the output at all)
# However, if something starts with adjust and has something after it, keep whatever is after it (in this case, 'ab')
# EX3: 12 abc abbadjustab adjust adjust_
# expected output: 12222 abccc abbab _____
# (as we can see, 'adjust' was removed from the middle of abb and ab)
# use certain functions: startswith, endswith, zfill, ljust, rjust

# user_input = [i for i in input("Enter space-separated inputs: ").split()]
# for i in range(len(user_input)):
#     if user_input[i].endswith("adjust") and len(user_input[i]) > 6:
#         user_input[i] = user_input[i][:-6]
#     if len(user_input[i]) < 5:
#         user_input[i] = user_input[i].ljust(5, user_input[i][-1])
#     elif len(user_input[i]) > 5:
#         user_input[i] = user_input[i][:5]
# print(" ".join(user_input))
        

# TASK TWO
# Take multiple inputs in a single line without using list comprehension (which is [i for i in input("Enter space-separated inputs: ").split()])
# Print the inputs
# x = input("Enter space-separated inputs: ").split()
# for i in x:
#     print(i)


# TASK THREE
# Go through binary search, linear search
# Binary search is a simple search algorithm that checks each element of a list until a match is found or the entire list has been searched.
# It's straightforward but inefficient for large datasets.

# Linear search is a more efficient algorithm that works only on sorted lists. First, it divides the area that it is searching in half.
# If the value of the search area is less than the item in the exact middle of the area, it will narrow down the search to the lower half.
# Otherwise, it will search just the upper half and leave the lower half untouched. This is very efficent for large datasets.


# TASK FOUR
# Go through all of the python keywords (roughly 35)
# False is a Boolean value, which is either True or False.
# None represents the absence of a value and is used as a default value for variables or function return values.
# True is a Boolean value, which is either True or False.
# and is a logical operator used to combine Boolean expressions.
# as is used to give an alias to an imported module or to rename a variable within a specific scope.
# assert is used to test a condition and if the condition is False, it raises an AssertionError.
# async is used for asynchronous programming, enabling non-blocking operations
# await is also used for asynchronous programming, enabling non-blocking operations.
# break is used to immediately exit a loop.
# class is used to define a class.
# continue is used to skip the current iteration of a loop and move to the next one.
# def is used to define a function.
# del is used to delete references to objects.
# elif is used in conditional statements to check additional conditions if the previous conditions were False.
# else is used in conditional statements to execute code when none of the previous conditions are True.
# except is used in exception handling to catch and handle exceptions.
# finally is used in exception handling to ensure a block of code is executed, no matter whether or not an exception occurs.
# for is used to create a for loop.
# from is used to import modules or specific objects from modules
# global is used to declare a variable as global within a function.
# if is used to create conditional statements, along with elif and else.
# import is also used to import modules or specific objects from modules.
# in is used to check if a value is present in a sequence.
# is is used to compare object identity (compares adresses).
# lambda is used to create anonymous functions.
# nonlocal is used to declare a variable as non-local within a nested function.
# not is a logical operator used to combine Boolean expressions.
# or is a logical operator used to combine Boolean expressions.
# pass is a null statement and is often used as a placeholder.
# raise is used to 'raise' exceptions.
# return  is used to return a value from a function or end the main code (like return 0).
# try is used for exception handling, along with except, else, and finally.
# while is used to create a while loop.
# with is a tool for resource management that ensures that resources, like files or network connections, are properly acquired and released,
# even if an exception happens.
# yield is used to create generators, which are functions that produce a sequence of values.


# TASK FIVE
# Brush up on Jenkins and refresh memory
# Recall file-handling, exception-handling, classes
# Install jupyter notebook


# take two inputs that are integers, and need to get all the numbers between the two
# give numbers that are divisible by seven, but not divisible by five
# user_input1 = int(input("Enter an integer: "))
# user_input2 = int(input("Enter another integer: "))
# result = []
# if user_input1 > user_input2:
#     print(result)
# else:
#     for i in range(user_input1, user_input2 + 1):
#         if i % 7 == 0 and i % 5 != 0:
#             result.append(i)
#     print(result)

# create a function and use the concept of recursion
# have to take an integer input and in each iteration, divide the input by 5
# tell when the value gets less than or equal to 3 and not less than 1 (1<x<=3)
# print true, else print false

# def func1(x):
#     if x <= 3 and x > 1:
#         print("True")
#         print(x)
#     elif x <= 1:
#         print("False")
#         print(x)
#     elif x > 3:
#         func1(x/5)

# user_input = int(input("Enter a number: "))
# func1(user_input)

# Write a program to accept a string input and reverse the string input and print, but without using indexing
# EX: "hello world"   ->    "dlrow olleh"
# user_input = input("Enter a string: ")
# result = ""
# for i in user_input:
#     result = i+result
# print(result)

# Write a program to take an integer input and find factorial using recursion
# EX: 3   -> 3x2x1     ->   6
# def func2(x):
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return x*func2(x-1)


# user_input = int(input("Enter a number: "))
# print(func2(user_input))

# Write a program to take an integer input and validate whether its a perfect number or not
# perfect number is when the sum of all the divisors of it becomes the same number (except for 1, because it isn't a perfect number)
# 6 -> 1, 2, 3 -> 6
# return true or false for yes or no
# user_input = int(input("Enter a number: "))
# total_sum = 0
# if user_input == 1:
#     print("False")
# else:
#     for i in range(1, user_input):
#         if user_input % i == 0:
#             total_sum += i
#     if total_sum == user_input:
#         print("True")
#     else:
#         print("False")




# TASK ONE:
# Write a python program to find the maximum difference between two elements in a list
# EX: [7, 1, 5, 3, 6, 4]
# (all the differences: 7 to 1, 1 to 5, 5 to 3, 3 to 6, and 6 to 4) 6, -4, 2, -3, 2
# return the highest difference (in this case, it's six)
# def max_difference(lst):
#     max_diff = lst[1] - lst[0]
#     for i in range(len(lst) - 1):
#         diff = lst[i + 1] - lst[i]
#         if diff > max_diff:
#             max_diff = diff        
#     return max_diff

# inputed_item = [0, 1, 2, 3, -1, -5]
# print(max_difference(inputed_item))

# TASK TWO:
# EXPLAIN WHAT THE FOLLOWING CODE DOES
# It checks if the string "s" can be split into words that are all present in a specified dictionary
# It does this by recursively attempting to split the string and checking each part to see if it is in the dictionary

# def can_segment_str(s, dictionary):
#    for i in range(1, len(s) + 1):
#         first_str = s[0:i]
#         if first_str in dictionary:
#             second_str = s[i:]
#             if (not second_str or second_str in dictionary or can_segment_str(second_str, dictionary)):
#                 return True
#     return False
# s = "datacamp"
# dictionary = ["data", "camp", "cam", "lack"]
# can_segment_string(s, dictionary)
# True

# TASK THREE:
# Write a program to find the missing number in a given list
# EX: [4, 5, 3, 2, 8, 1, 6]
# in this scenario, the answer is 7
# so basically just sort and then find missing number and then return
# lst = [4, 5, 3, 2, 7, 1, 6, -1]
# lst.sort()
# for i in range(len(lst) - 1):
#     if lst[i] + 1 != lst[i + 1]:
#         missing_number = lst[i] + 1
#         break
# else:
#     missing_number = lst[-1] + 1
# print(missing_number)

# TASK FOUR:
# EXPLAIN WHAT THE FOLLOWING CODE DOES
# Checks if there is a Pythagorean triplet (a set of three numbers a, b, and c, that satisfies a squared plus b squared equals c squared
# in the list of numbers

# def checkTriplet(array):
#     n = len(array)
#     for i in range(n):
#         array[i] = array[i]**2
#     array.sort()
#     for i in range(n - 1, 1, -1):
#         s = set()
#         for j in range(i - 1, -1, -1):
#             if (array[i] - array[j]) in s:
#                 return True
#             s.add(array[j])
#     return False

# arr = [3, 2, 4, 6, 5]
# checkTriplet(arr)
# True

# TASK FIVE:
# Brush up on Jenkins and refresh memory
# Recall file-handling, exception-handling, classes
# Install jupyter notebook





# Write a python program to evaluate a valid phone number


# Write a program to do... this??
lst = [20, -5, -6, 0]
lst2 = [-20, -4, "abc", "xyz"]
lst3 = []
for i in range(len(lst)):
    if isinstance(lst[i], str) or isinstance(lst2[i], str):
        lst3.append(str(lst[i])+str(lst2[i]))
    else:
        lst3.append(lst[i]+lst2[i])
# print(lst3)


# You are provided with the list of stock prices, and you have to return the buy and sell price to make the highest profit. 
# Note: We have to make maximum profit from a single buy/sell, and if we can’t make a profit, we have to reduce our losses. 
# Example 1: stock_price = [8, 4, 12, 9, 20, 1], buy = 4, and sell = 20. Maximizing the profit. 
# Example 2: stock_price = [8, 6, 5, 4, 3, 2, 1], buy = 6, and sell = 5. Minimizing the loss.

# Given an array on non-negative integers representing the elevation map, where the width of each var is 1, calculate how much rainwater
# it can trap after raining.

# There are 12 intermediate stations between two places A and B. Find the number of ways in which a train can be made to stop at 4 of these
# intermediate stations so that no two stopping stations are consecutive.
# EX: n = 12, s = 4
# OUTPUT: 126
# EX: n = 16, s = 5
# OUTPUT: 792

# TASK ONE
# Study briefly about decorators, abstraction, nonlocal, encapsulation
# Decorators are dsesign pattern in Python that allow a user to add new functionality to an existing object without modifying its structure.
# Abstraction is a process of handling complexity by hiding unnecessary information from the user.
# Nonlocal is a keyword which is used to work with variables inside nested functions, where the variable should not belong to the inner function.
# Encapsulation is the concept of bundling data and methods within a single unit.

# Given a sentence containing n strings, remove all duplicate strings
# EX: Trains will be different in each country where no trains are similar.
# OUTPUT: Trains will be different in each country where no are similar.
s = "Trains will be different in each country where no trains are similar."
s = s.lower().split()
t = []
for i in s:
    if i not in t:
        t.append(i)
t = " ".join(t)
# print(t)




class a:
    def __init__(self, x, y):
        self.x = x
        self.__y = y
    
    def publicGetter(self):
        print(self.x)
        self.__privateGetter()
    
    def __privateGetter(self):
        print(self.__y)

# obj1 = a(3, 5)
# obj1.publicGetter()



def practice(a, d, e, c = None, b = 5):
    
    return [e, a, b, d, c]

# print(practice(7, -1, 0))




# TASK ONE
# Check if there is anything else with is part of OOP and go through them (nothing else left)
# Come up with a new example for inheritance, polymorhpism, abstraction, and encapsulation
# INHERITANCE EXAMPLE:
class animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating.")

class dog(animal):
    def bark(self):
        print(f"{self.name} is barking.")

dog = dog("Dog")
# dog.eat()
# dog.bark()

# POLYMORPHISM EXAMPLE:
class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

class square(circle):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

circle = circle(5)
# print(circle.area())
square = square(4)
# print(square.area())


# NEEDS TO BE FIXED!!
# ABSTRACTION EXAMPLE:
from abc import ABC, abstractmethod

class car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    def start(self):
        print("Car started.")
    def stop(self):
        print("Car stopped.")
    def accelerate(self):
        print("Car accelerating.")
    def brake(self):
        print("Car braking.")

car = car("Honda", 1999)
# car.start()
# car.accelerate()
# car.brake()
# car.stop()

# ENCAPSULATION EXAMPLE:
class bankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    def get_balance(self):
        return self.__balance

account = bankAccount(1234, 595.99)
# account.deposit(5)
# account.withdraw(10)
# print(account.get_balance())

# TASK TWO
# Come up with two different examples each for instance methods, class methods, instance variables, class variables, so eight examples in total.
# INSTANCE METHODS EXAMPLES:
class dog2:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def showBreed(self):
        print(self.breed)

my_dog = dog2("Dog", "Golden Retriever")
# my_dog.showBreed()

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("Hi, my name is", self.name, "and I am", self.age, "years old.")

person = person("Shubhangi", 12)
# person.introduce()

# CLASS METHODS EXAMPLES:
class person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year
        return cls(name, age)

person1 = person1("Shubhangi", 12)
person_1 = person1.from_birth_year("Bob", 2012)
# print(person_1.name, person_1.age)

class person2:
    population = 0
    def __init__(self, name):
        self.name = name
        person2.population += 1
    @classmethod
    def get_population(cls):
        return cls.population

person_2 = person2("Alice")
person3 = person2("Bob")
# print(person_2.get_population())

# INSTANCE VARIABLES EXAMPLES:
class car2:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

car_2 = car2("Red", 120)
# print(car_2.color, car_2.speed)

class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employee = employee("Bob", 50000)
# print(employee.name, employee.salary)

# CLASS VARIABLE EXAMPLES:
class company:
    company_creation_date = 2024
    def __init__(self, name, net_worth):
        self.name = name
        self.net_worth = net_worth

company_1 = company("Company Corp", 900000)
# print(company_1.company_creation_date, company_1.name, company_1.net_worth)
# print(company.company_creation_date)

class car3:
    number_of_wheels = 4
    def __init__(self, make, model):
        self.make = make
        self.model = model

car_3 = car3("Honda", "Civic")
# print(car3.number_of_wheels)

# for i in range(10):
#     print(i)
#     break
# else:
#     print("for loop done")

x = 36 / 4 * (3 +  2) * 4 + 2
# print(x)


# TASK ONE:

# Day of the Programmer
# Bill Division
# Sales by Match
# Drawing Book

# TASK TWO:
# Go through Tkinter

# TASK ONE:
# Go through the concept of stack, queue, linkedlist, doublelinkedlist, trees, binary trees, and heap.

# Stack: A linear data structure in which items are added to and removed from the top of the stack.
# Queue: A linear data structure in which items are added to the back and removed from the front.
# Linkedlist: A linear data structure that has nodes where each node contains data, as well as a reference to the next node in the sequence.
# Doublelinkedlist: An extension of a linked list where each node has two links: One to the next node, and one to the node before it.
# Trees: Hierarchical data structures that has a root node at the top, and zero or more child nodes connected by edges.
# Binary trees: Special types of trees where each node has at most two children.
# Heap: A specialized binary tree used for priority-based operations. There is min-heap, and max-heap.
# Min-heap is where the root is the smallest element and the child nodes are greater.
# Max-heap is where the root is the largest element and the child nodes are smaller.

# TASK TWO:
# Understand NthFibonacciNum logic and be able to explain it.

# TASK THREE:
# Rock, Paper, Scissors with single user input, against a computer that has randomized moves that don't have an explaination behind them whatsoever.
# n = # of rounds
# User types one of the following words- rock/paper/scissors- to choose their move.
# Rock beats scissors, scissors beats paper, paper beats rock- announce winner after each round by comparing moves.
# For a win-, winner gets 2 points, draw- both get 1 point, loser- zero points
# import random

# moves = ["rock", "paper", "scissors"]
# n = int(input("Enter the number of rounds: "))
# user_score = 0
# computer_score = 0
# for round_num in range(1, n + 1):
#     print(f"\nRound {round_num}")
#     while user_move not in moves:
#         user_move = input("Choose rock, paper, or scissors: ").lower()
#     # if user_move not in moves:
#         print("Invalid move! Please choose rock, paper, or scissors.")
#     computer_move = random.choice(moves)
#     print(f"Computer chose {computer_move}.")
#     if user_move == computer_move:
#         print(f"Round {round_num} is a draw!")
#         user_score += 1
#         computer_score += 1
#     elif (user_move == "rock" and computer_move == "scissors") or (user_move == "scissors" and computer_move == "paper") or (user_move == "paper" and computer_move == "rock"):
#         print(f"You have won round {round_num}!")
#         user_score += 2
#     else:
#         print(f"The computer has won round {round_num}!")
#         computer_score += 2

# print("\nGame Over!")
# print(f"Your score: {user_score}")
# print(f"Computer's score: {computer_score}")
# if user_score > computer_score:
#     print("You win the game!")
# elif user_score < computer_score:
#     print("Computer wins the game!")
# else:
#     print("It's a tie!")


# TASK FOUR:
# Cover the topics of BFS (Breadth first search) and DFS (Depth first search).
# BFS: A search method that investigates all surrounding nodes after starting at the root node.
# DFS: Algorithm that starts with the first node in the network and continues to explore
# until it discovers the desired node or even a node with no children.




# Create a function for the user which takes the parameter which is a string of any length.
# Return the number of vowels in the string.
from functools import cache

@cache
def vowelCountFinder(text: str):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_counter = 0
    for i in text.lower():
        if i in vowels:
            vowel_counter += 1
    return vowel_counter

# print(vowelCountFinder("I like python programming"))
# print(vowelCountFinder("I like java programming"))



# TWO (DONE) (THREE CONTINUED):
# Make one example EACH for deprecated decorator and atexit decorator.
# from deprecated import deprecated

# @deprecated("This function will be removed soon . . .")
# def old_function():
#     print("Running old function.")

# old_function()


# import atexit

# def say_goodbye():
#     print("Goodbye! Program is exiting.")

# atexit.register(say_goodbye)

# print("Hello! Program is running.")

# TASK TWO (DONE):
# look at teams img thing and work accordingly

class Employee:
    def __init__(self, name, identification_num, age, gender):
        self.name = name
        self.id = identification_num
        self.age = age
        self.gender = gender

class Organization:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def addEmployee(self, name, identification_num, age, gender):
        employee = Employee(name, identification_num, age, gender)
        self.employees.append(employee)

    def getEmployeeCount(self):
        return len(self.employees)

    def findEmployeeAge(self, identification_num):
        for i in self.employees:
            if i.id == identification_num:
                return i.age
        return -1

    def countEmployees(self, age):
        count = 0
        for i in self.employees:
            if i.age > age:
                count += 1
        return count


# org = Organization("OrganizationOne")

# num_employees = int(input("Enter the number of employees you would like to add: "))

# for i in range(num_employees):
#     name = input("Enter the name of the employee: ").strip()
#     identification_num = int(input("Enter the ID of the employee: "))
#     age = int(input("Enter the age of the employee: "))
#     gender = input("Enter the gender of the employee: ").strip()
#     org.addEmployee(name, identification_num, age, gender)

# search_id = int(input("Enter the ID of the employee you would like to find the age of: "))
# search_age = int(input("Enter the age you would like to find the number of employees are older than: "))
# print(org.getEmployeeCount())
# print(org.findEmployeeAge(search_id))
# print(org.countEmployees(search_age))


def function1(name, list1=[]):
    print(f"The name is {name}")
    list1.append(name)
    print(list1)

# function1("Bob")
# function1("Mary", list1=[])
# function1("Alice")
# Expected output:
# The name is Bob
# ["Bob"]
# The name is Mary
# ["Mary"]
# The name is Alice
# ["Bob", "Alice"]


# NOT A GOOD PRACTICE, but it's valid
# string1 = 'string1' 'text' 'more text'
# print(string1)
# Expected output:
# string1textmore text


class Test1:
    @staticmethod
    def testMethod1():
        pass


    def __testMethod2(self):
        pass


    def callMeth2(self):
        self.__testMethod2()


# Output:
# The class name is Test1
# *Test1.testMethod1()
# *obj1.testMethod2() -> We are not able to access that


# obj1 = Test1()
# How to get the class's name: *object*.__class__.__name__
# print(f"The class name is {obj1.__class__.__name__}")

# Test1.testMethod1()

# Can't call a private method using the object,
# instead use a getter method
# obj1.callMeth2()



# TASK ONE: (DONE)
# Ask for input for num of players, then take their names, and have turns
# Second input- integer number, which is the locator
# Third input- name is multiples of

# EX: (Num of players=3), locator=5
#     multiplesof=5
#     (player1):2, (player2):4, (player3):1,
#     7, 25 (player2 enters in the locator value, and if player2 gets it wrong, they are out)

# Every *five* turns (according to the locator value of 5),
# if the player whose turn it is doesn't guess a multiple of *five* (according to multiplesof value of 5),
# they are eliminated
# Last player left wins

# Altogether turns maximum is *maxTotalTurns*- which is currently 50

# TASK FIVE: (DONE)
# Get an array of list of numbers, then get a target,
# Use as many numbers as needed, but must get the target number by adding the numbers in the list (but each number can only be used once)
# EX: nums=[2, 7, 11, 50], target=9 -> [0, 1]
# note: [0, 1] are the indexes of the numbers which resulted in the target (2+7=9)
def findNumberstoGetTarget(numbers, target, start_index, current_sum, chosen_indexes):
    if current_sum == target:
        return chosen_indexes
    if current_sum > target or start_index >= len(numbers):
        return None
    for i in range(start_index, len(numbers)):
        new_sum = current_sum + numbers[i]
        new_indices = chosen_indexes + [i]
        result = findNumberstoGetTarget(numbers, target, i + 1, new_sum, new_indices)
        if result:
            return result
    return None

# print(findNumberstoGetTarget([2, 7, 11, 50], 9, 0, 0, []))

# TASK SIX: (DONE)
# Find the longest substring with no repeating characters
# EX: "abcabba" -> 3
# note: 3 is the length of the longest substring that has no repeating characters,
# and we get that beceause the longest substring with no repeating characters is "abc", since after that, we get a,
# which is a repeating character
def findLongestUniqueSubstring(textStr):
    seen = set()
    leftChar = 0
    max_length = 0
    for rightChar in range(len(textStr)):
        while textStr[rightChar] in seen:
            seen.remove(textStr[leftChar])
            leftChar += 1
        seen.add(textStr[rightChar])
        current_length = rightChar - leftChar + 1
        max_length = max(max_length, current_length)
    return max_length

# print(findLongestUniqueSubstring("dbacb"))

import keyword

# print(keyword.kwlist)
# print(len(keyword.kwlist))
# print(keyword.softkwlist)
# print(len(keyword.softkwlist))


# TASK ONE: (DONE)
# Examples for assert, nonlocal, with, yield, raise

# Assert:
def divide(a, b):
    assert b != 0, "Cannot divide by zero!"
    return a / b

# print(divide(10, 0))   # AssertionError occurs since b is 0

# Nonlocal: 
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20   # x from outer()'s scope is modified
        print(f"Inside inner, x: {x}")
    inner()
    print(f"Inside outer, x: {x}")

# outer()

# With: 
# with open("PracticePy.txt", "w") as f:   # Through 'with', the file automatically closes when done
#     f.write("Hello, world!\n")
#     f.write("This is a test.")
# with open("PracticePy.txt", "r") as f:
#     print(f.read())

# Yield: 
def count_up_to(n):
    i = 0
    while i <= n:
        yield i   # Each time this loops and yield is run, the generator produces a value, then "pauses"
        i += 1
counter = count_up_to(5)
# print(next(counter))   # Each time next() is called on the iterator, the generator "resumes"
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))   # Since this is the 6th time, which is over 5 times, this will return a StopIteration error

# Raise: 
def calculate_age(birth_year, current_year):
    if birth_year <= 0:
        raise customException1("Birth year cannot be zero or negative. Please provide a valid year.")
    age = current_year - birth_year
    return age

class customException1(Exception):
    pass
# print(calculate_age(-2012, 2025))   # The custom exception called customException1 occurs
# since it is raised due to birth_year being zero/negative



# x = 10
# y = 30

# n = *user input*

# x = 10
# y =  30
# n = int(input("Enter a number: "))
# if 10<n<30:
#     print("Perfect")



# TASK ONE: (DONE)
# Brush up on all of the decorator concepts
# Make examples for all of the built-in decorators

# @staticmethod
class mathFunctions:
    @staticmethod
    def add(a, b):
        return a + b

print(mathFunctions.add(3, 5))


# @classmethod
class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_string(cls, string):
        name = string.strip().title()
        return cls(name)

p = Person.from_string("  Shubhangi ")
print(p.name)


# @lru_cache()
from functools import lru_cache

@lru_cache(maxsize=100)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(35))   # Easier this way because with fibonacci, the same sequence occurs again and again


# @cache
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

# print(factorial(10))


# NOTE: Search for Python certifications in the US from Microsoft and Google

# TASK ONE: (DONE)
# Comparison between static method, class method, and instance method
# Static Method: Don't depend on the class or its instances
# Class Method: Associated with the class itself
# Instance Method: Operate on specific objects of a class


# TASK TWO: (DONE)
# Come up with an example of typehinting using the typing module
from typing import List, Tuple, Dict

def process_scores(scores: List[int]) -> Tuple[int, float]:
    total = sum(scores)
    average = total / len(scores)
    return total, average


# TASK THREE: (DONE)
# Come up with an example for each: List comprehension, set comprehension, generator comprehension
# squares = [x**2 for x in range(10)]
# print(squares)

# unique_lengths = {len(word) for word in ["apple", "banana", "pear", "apple"]}
# print(unique_lengths)

# even_numbers = (x for x in range(20) if x % 2 == 0)
# for num in even_numbers:
#     print(num, end=" ")


# TASK FOUR: (DONE)
# Come up with an example for permutations and combinations using the module itertools
from itertools import permutations, combinations

items = ['A', 'B', 'C']

# print(list(permutations(items, 2)))  # Order matters

# print(list(combinations(items, 2)))  # Order doesn't matter

# TASK FIVE: (DONE)
# Briefing on regular expressions (one program on how to validate a mobile number) and os module built-in functions
# To validate:
# Check if starts with 6-9, then if it has 9 digits
import re

def is_valid_mobile(number: str) -> bool:
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, number))


# print(is_valid_mobile("9876543210"))   # True
# print(is_valid_mobile("1234567890"))   # False (Starts with 1, not 6-9)
# print(is_valid_mobile("92345678"))   # False (Too short)
# print(is_valid_mobile("9234567890B"))   # False (Has an invalid character of 'B' when there should be only integers)


# TASK SIX: (DONE)
# Brush up on mysql connectors (from create_database.py)



# TASK ONE: (DONE)
# Make an example each for ternary and walrus operators (two examples)
# n = -5

# result = "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
# print(result)

# numbers = [1, 2, 3]

# while (n := len(numbers)) > 0:   # In this case, n is assigned to len(numbers) and is then used in the expression n > 0
#     print(numbers.pop())


# TASK TWO: (DONE)
# Look at Github Actions: Runners, Workflow Call, Workflow Dispatch, Schedule
# Github Actions: A platform for automating software development workflows, primarily used for continuous integration (CI)
# and continuous delivery (CD).
# Runners: Machines that execute the jobs defined in workflows.
# Workflow Call: A feature that allows one workflow to call another workflow, enabling modularity and code reuse.
# Workflow Dispatch: An event trigger that allows you to manually start a workflow run from the GitHub UI or API.
# Schedule: An event that allows you to define a schedule (using cron syntax) for your workflow to run automatically at specific intervals.



# a = [1, 2, 3, 4, 5]
# rotate = r2
# a = [4, 5, 1, 2, 3]
# rotate = l3
# a = [2, 3, 4, 5, 1]

# a = [1, 2, 3, 4, 5]
# rotate = -r2
# a = [5, 4, 1, 2, 3]
# b = [-1, 0, "ABC", True]
# rotate = -l3
# b = [True, "ABC", 0, -1]

import sys

a = [eval(i) for i in input("Enter the elements in a list: ").split()]
rotate = input("Enter the rotation factor: ").split()   # Structured (-) (l/r) (#)

def Rotate_Elements(a, rotate):
    if len(a) == 0:
        print("The list cannot be empty")
        sys.exit(1)

    if len(rotate) == 2:
        rotate[1] = abs(int(rotate[1]))
        if int(rotate[1]) > len(a):
            rotate[1] = rotate[1] % len(a)
        if rotate[0].lower() == "r":
            shifting_elements = a[-(rotate[1]):]
            not_shifting = a[:-(rotate[1])]
            return (shifting_elements + not_shifting)
        else:
            shifting_elements = a[:(rotate[1])]
            not_shifting = a[(rotate[1]):]
            return (not_shifting + shifting_elements)
    if len(rotate) == 3:
        rotate[2] = abs(int(rotate[2]))
        if rotate[2] > len(a):
            rotate[2] = rotate[2] % len(a)
        if rotate[1].lower() == "r":
            shifting_elements = a[-(rotate[2]):]
            not_shifting = a[:-(rotate[2])]
            flipped_shifting_elements = shifting_elements[::-1]
            return (flipped_shifting_elements + not_shifting)
        else:
            shifting_elements = a[:(rotate[2])]
            not_shifting = a[(rotate[2]):]
            flipped_shifting_elements = shifting_elements[::-1]
            return (not_shifting + flipped_shifting_elements)


# TASK ONE: (DONE)
# Fix the function above, so that in the case of a negative rotation number (like the case below),
# treat the number in the rotation factor like it's positive

print(Rotate_Elements(a, rotate))