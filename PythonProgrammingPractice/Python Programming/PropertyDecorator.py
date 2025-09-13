# @property tells Python to treat the method like an attribute, except by default you can't set a value for that method-attribute.
# @*method-attributename*.setter tells Python that you can set that method-attribute to equal something. 

# class class1:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
    
#     def meth1(self):
#         return (f"{self.a} {self.b} {self.c}")

# obj1 = class1(1, 2, 3)
# print(obj1.a)
# print(obj1.meth1)

# How to Convert a Method into an Attribute
class class1:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    @property
    def meth1(self):
        return (f"{self.a} {self.b} {self.c}")


    @meth1.setter
    def meth1(self, value):
        self.a, self.b, self.c = value.split(" ")

# obj1 = class1(1, 2, 3)
# print(obj1.a)
# obj1.a = 4
# obj1.b = 5
# obj1.meth1 = "1 2 3"
# print(obj1.meth1)

# TASK ONE:
# Come up with a new example for decorators (DO NOT DISTURB ORIGINAL FUNCTION NEEDED TO MODIFY):
# Goal is to keep the result positive, even when there is a negative
def ensure_positive(func):
    def inner_func(a, b):
        a, b = abs(a), abs(b)
        return func(a, b)
    return inner_func

@ensure_positive
def multiply(a, b):
    print(a * b)

# multiply(-1, 2)

# TASK TWO:
# Come up with a new example for property decorators, including setter.
class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name_set(self):
        return self.__name

    @name_set.setter
    def name_set(self, value):
        self.__name = value

    # @name_set.getter
    # def name_set(self):
    #     return self.name

    @name_set.deleter
    def name_set(self):
        del self.__name

obj_person = Person("Shubhangi")
print(obj_person.name_set) # Getter
obj_person.name_set = "SHUBHANGI" # Setter
print(obj_person.name_set) # Getter
# del obj_person.name_set # Deleter
print(obj_person.name_set) # Getter

# TASK THREE;
# Just like method.setter, there is a method.getter and method.deleter. Come up with examples for both method.getter and method.deleter.
# NOTE: Added .getter and .deleter to the .setter example (See above.)