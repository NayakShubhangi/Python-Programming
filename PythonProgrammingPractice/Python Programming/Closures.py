# A CLOSURE is an inner function, inside another function, which consists of some nonlocal variables.
# There are three scopes: global, nonlocal, and local.
# global and nonlocal can be set explicitly, while local gets set automatically in a function or loop, and otherwise can't be set.

# var2 = 4
# def outerfunction():
#     var = 3
#     print(var2)
#     def innerfunction():
#         nonlocal var
#         var += 1
#         print(var)
#         print(var2)
#     return innerfunction

# outfunc = outerfunction()
# outfunc()

# def outerfunction2():
#     var4 = 10
#     def innerfunction2():
#         nonlocal var4
#         # Without using nonlocal, var4 can't be changed since it has a local scope only for outerfunction2, but it can be accessed
          # nonlocal works with closures
#         var4 += 5
#         print(var4)
#     print(var4)
#     return innerfunction2()

# outerfunction2()

# var3 = 8
# def outerfunction3():
#     global var3
#     # Without using global, there's an error since it can only be accessed, not changed
#     # nonlocal can't be used here since it isn't the scope and isn't a closure, so global is used instead since it's a global variable
#     var3 -= 2
#     print(var3)

# outerfunction3()

# --------------------------------------------------------------------------------------
# EXAMPLE:
# var5 = 11
# def outerfunction4():
#     var5 = 16
#     print(var5)
#     var5 += 10
#     print(var5)

# print(var5)
# outerfunction4()
# print(var5)

# The same variable name can be used here without any conflict since the two variables exist on different scopes.
# var5 outside of the function is 11, and is on the global scope, while the var5 inside the function is 16 (then 26) is on the local scope.
# Both var5's exist on different scopes simultaneously and can be called.
# The output for the above code is 11, 16, 26, 11
# because the line 49 and 51 refer to the global var5, while outerfunction4 refers to the local var5

# SHORTCUT REFERENCE:
# Outisde of function but used inside of function ---> global
# Inside of function but used inside of nested function ---> nonlocal
# var5 = 11   # GLOBAL
# def outerfunction4():
#     var6 = 16   # LOCAL
#     print(var6)
#     global var5
#     var5 += 10  # GLOBAL
#     print(var5)

# print(var5)   # GLOBAL
# outerfunction4()
# print(var5)   # GLOBAL (but it's been changed)

# Returns 11, 16, 21, 21
# because line 70 refers to global var5,
# line 71 refers to local var6 then global var5 (which gets incremented by 10 and becomes 21),
# line 72 refers to global var5 (which was changed in line 71)
# --------------------------------------------------------------------------------------

# def outer():
#     x = "outer"
#     def inner():
#         nonlocal x
#         x = "inner"
#     inner()
#     print(x)

# outer()
# Expected output: inner

# x = "global"
# def outer():
#     x = "outer"
#     def inner():
#         x = "inner"
#         print(x)
#     inner()
#     print(x)
# outer()
# print(x)
# print("globals", globals())
# print("locals", locals())
# Expected output:
# inner, outer, global (ALL OF THEM EXIST ON SEPARATE SCOPES)



# TASK 1:
# Figure out how that works (globals and locals) and why they're useful (WITH AN EXAMPLE)

# globals() returns a dictionary which represents all of the global variables and functions in the current file.
# It's useful when modifying global variables dynamically.

# locals() Returns a dictionary which represents all of the variables within the current function or scope.
# It's useful for debugging or dynamically working with local variables.

# TASK 2:
# Find out the difference between instance and object in Python

# An object is any entity created from a class.
# (Everything in Python, like integers, lists, functions, are objects.)

# An instance is a specific object created from a particular class.
# (When a class is called, the result is called an instance of that class.)
# EVERY INSTANCE IS AN OBJECT, BUT NOT EVERY OBJECT IS AN INSTANCE!

# TASK 3:
# Find out the difference between self and cls in Python classes

# self refers to the instance of the class. (INSTANCE METHOD)
# It's used in instance methods to access and modify instance attributes.
# Each instance of the class gets its own self.

# cls refers to the class itself rather than an instance. (CLASS METHOD)
# Used in class methods (decorated with @classmethod).
# Can access and modify class-level attributes shared by all instances.

# TASK 4:
# Brush up on static methods, class methods, and instance methods, and MAKE AN EXAMPLE FOR EACH
class car:
    wheels = 4
    def __init__(self, brand: str, color: str):
        self.brand = brand
        self.color = color
    
    def show_details(self):     # INSTANCE METHOD
        print(f"Brand: {self.brand}, Color: {self.color}")
    
    @classmethod
    def change_wheels(cls, new_wheel_count: int):     # CLASS METHOD
        cls.wheels = new_wheel_count
        print(f"Updated wheels for all cars to {cls.wheels}")
    
    @staticmethod
    def general_info():     # STATIC METHOD
        print("Cars are a common mode of transportation.")

# car1 = car("Toyota", "Red")
# car1.show_details()
# car.change_wheels(3)
# car.general_info()

# TASK 5:
# Brush up on static variables, class variables, and instance variables, and MAKE AN EXAMPLE FOR EACH
# NOTE: Static variables are also known as class variables.
# In the above example, static/class variable would be: wheels
# In the above example, instance variables would be: self.brand and self.color