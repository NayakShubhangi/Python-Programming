# The __new__ dunder method is responsible for creating a new instance of a class.
# It's called before the __init__ dunder method and is used to control object creation.
# It returns a new instance of the class.
# It is mostly used when you need to customize instance creation, such as for single-turn patterns, immutable objects, or meta classes.

class class1:
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            print("Creating instance. . .")
            cls.__instance = super().__new__(cls)
        else:
            print("Instance already exists. . .", cls.__instance)
        return cls.__instance
    
    def __init__(self):
        print("This is from the constructor.")
        # self is an instance of the class, and when we assign a parameter to the instance of the class, we're changing it.
        # This DOES NOT create a new instance. We are just modifying it.
        # The instance that we're modifying has been created by __new__.

# clsobj = class1()
# clsobj2 = class1()
# print(clsobj == clsobj2)
# print(clsobj is clsobj2)
# Even though there are two objects, they're referring to the same instance.


# TASK ONE: NOTE: It's in WalrusOperator.py

# TASK TWO:
# Come up with one example using the __new__ dunder method.
class roundedInt(int):
    def __new__(cls, value):
        rounded = round(value)
        return super().__new__(cls, rounded)


num1 = roundedInt(3.7)
print(num1)

# TASK THREE:
# Come up with an example for slicing object and cache decorator
numbers = [-9, -2.5, 1, 7, 1.9]
positive_slice = slice(-3, None, 2)
filtered_numbers = numbers[positive_slice]
print(filtered_numbers)

from functools import lru_cache
from time import perf_counter


@lru_cache(maxsize=None)
def sumSublist(start: int, end: int, data: tuple) -> int:
    return sum(data[start:end])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

start = perf_counter()
print(sumSublist(0, 5, tuple(numbers)))
print(sumSublist(5, 10, tuple(numbers)))
print(sumSublist(0, 5, tuple(numbers)))
end = perf_counter()
print("It took:", end - start, "seconds")

# TASK FOUR:
# try to fix the project and maybe improve it..?