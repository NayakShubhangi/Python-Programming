# Instance methods, class methods, static methods
# All kinds of methods that start and end with __ are called dunder methods (like __init__)
# Whatever method takes the first argument as "self," it is an instance method (like meth1() from instance() class)
# Instance methods are used for objects of a class
# While it is suggested to use the word "self" as the first argument, it isn't mandatory to use the exact word, and you are able to use
# other words, as long as they are used throughout the method, such as the argument "random" used for the method list_dev_names()
# in the netflix() class, because "random" is an alias for "self"
# class instance:
#     var = "Variable"
#     def __init__(self):
#         self.number = 35
    
#     def meth1(self):
#         print(self.number)


# obj = instance()
# obj.meth1()
# print(obj.var)

# Class method
# Class methods takes the first argument as "cls" instead of self (like dev_profile() method from neflix() class)
# Cls is a class property and has access to all of the class variables and methods (such as dev_profile() method has access to everything
# in neflix() class)
class netflix:
    dev1_name = "Bob"
    dev2_name = "Alex"
    color = "red"
    def __init__(self, language):
        self.language = language
    
    def display(self):
        print(f"Your selected language is {self.language}")

    def list_dev_names(random):
        print(random.dev1_name)
        print(random.dev2_name)

    def profile(self):
        print(f"User selected profile is {self.color}")

    @classmethod
    # In python, whatever is written above a method starting with an "@" is called a decorator
    def dev_profile(cls):
        cls.color = "orange"
        print(cls.color)


# obj2 = netflix("English")
# obj2.display()
# obj2.list_dev_names()
# obj2.profile()
# obj2.color = "blue"
# obj2.profile()
# print(netflix.color)
# obj2.dev_profile()
# print(netflix.color)

# Static Method
# Static methods are used to make things accessable to everyone
# Static Methods don't require "self" or "cls" and they have a decorator that says "@staticmethod"
class netflix2:
    dev1_name = "Bob"
    dev2_name = "Alex"
    color = "red"
    def __init__(self, language):
        self.language = language
    
    def display(self):
        print(f"Your selected language is {self.language}")

    def list_dev_names(random):
        print(random.dev1_name)
        print(random.dev2_name)

    def profile(self):
        print(f"User selected profile is {self.color}")

    @classmethod
    # In python, whatever is written above a method starting with an "@" is called a decorator
    def dev_profile(cls):
        cls.color = "orange"
        print(cls.color)
    
    @staticmethod
    def greetings():
        print("Welcome to Netflix")

obj3 = netflix2("English")
obj3.greetings()
netflix2.greetings()