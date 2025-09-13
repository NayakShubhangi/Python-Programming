# Local, nonlocal, nonglobal, global, method scope
# TASK ONE
# Create three classes with any names
# First class has constructor (init) and define any one property, then define one method which will print something random that's not the property
# Second class doesn't have anything, so just type pass
# Third class doen't have constructor, but it has a method which will have the same method as the first class's method
# which will function the same, but won't print the same random thing as the one in the first class's method
# Class two and three will inherit from class one
# Create objects for the last two classes, but not for class one
# Print the methods that they have, including inherited ones (but only for class two), but class three will have its own method
# Create another object for class three and using that object, call the class one method

class firstClass:
    def __init__(self):
        self.randomproperty = 45

    def print_random_message(self):
        print("This is a random message from FirstClass.")


class secondClass(firstClass):
    pass


class thirdClass(firstClass):
    def __init__(self):
        self.property = "This is thirdClass property"

    def print_random_message(self):
        print("This is a different random message from ThirdClass.")


second_obj = secondClass()
second_obj.print_random_message()

third_obj = thirdClass()
third_obj.print_random_message()

third_obj_2 = thirdClass()
third_obj_2.new_property = "This is a new property added through a new object"
print(third_obj_2.new_property)
third_obj_2.print_random_message()