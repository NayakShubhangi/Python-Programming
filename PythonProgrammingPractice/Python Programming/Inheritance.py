# class friendOne:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def methodOne(self):
#         print(self.name, self.age, self.id)

# class friendTwo(friendOne):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.id = 76
    
#     # In python, whatever starts with __ and ends with __ are called dunder methods
#     # Each dunder method has a functionality, like __init__, which is a constructor, and __str__, which customizes the object
#     def __str__(self):
#         return f"{self.name}, {self.age}"

#     def methodTwo(self):
#         print("Method Two")

# obj = friendTwo("Pari", 12)
# obj.methodOne()
# obj.methodTwo()
# print(obj)


# TASK ONE
# Create a parent class and add a few attributes/variables from the constructor and define them
# Create a child class and the child class should be empty (use pass)
# When you call the function, create an object for the child class, and then use the obj add properties to the child class (same as in the parent class)
# Using the parent class object, print those variables
# Using the child class object, print the same variables (parent and child classes have separate objects)
# Using child class object, delete one of the variables, and try to print those variables by using both the parent class object and the child class object
# Child class will obviously inherit from the parent class
class ParentClass:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

class ChildClass(ParentClass):
    pass

child_obj = ChildClass("Pari", "12", "424919")
parent_obj = ParentClass("Satya", "48", "313808")
print("Parent Object Variables:")
print(f"Name: {parent_obj.name}")
print(f"Age: {parent_obj.age}")
print(f"ID: {parent_obj.id}")

print("\nChild Object Variables:")
print(f"Name: {child_obj.name}")
print(f"Age: {child_obj.age}")
print(f"ID: {child_obj.id}")

del child_obj.age

print("\nAfter Deleting Age from Child Object:")
print("\nParent Object Variables:")
print(f"Name: {parent_obj.name}")
print(f"Age: {parent_obj.age}")
print(f"ID: {parent_obj.id}")

print("\nChild Object Variables:")
print(f"Name: {child_obj.name}")
try:
    print(f"Age: {child_obj.age}")
except AttributeError as e:
    print(f"Age: Error - {e}        *this is an exception*")
print(f"ID: {child_obj.id}")


# TASK TWO
# Read the .txt file provided and give the number of occurrences of each word and the number of spaces
# Add python script in jenkins, and give parameter so that you can upload a file to jenkins, and jenkins will run a python script to do the rest.
# EX: a .txt file given by the user says "The user name is user" -> *Dictionary will be returned and key would be each word, while value would be number of occurences*
# -> *4 different words, so 4 keys and 4 values* -> The: 1, User: 2, name: 1, is: 1 -> *Number of spaces should be provided as well* -> Spaces: 4
# task.groovy
# ERROR