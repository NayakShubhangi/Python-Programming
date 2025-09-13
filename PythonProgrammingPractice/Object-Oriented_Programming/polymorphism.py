# Polymorphism means one name but many forms.
# In python, polymorphism is achieved by method overloading and method overriding

# Method Overriding: Two or more classes that have the same method with the same name.

class classOne:
    def __init__(self):
        print("This is classOne constructor.")

    def methOne(self):
        print("This is method one.")

class classTwo(classOne):
    def __init__(self):
        print("This is classTwo constructor.")

    def methTwo(self):
        print("This is inside classTwo.")

obj1 = classTwo()
obj1.methOne()

# Method Overloading: A single method inside a class but deferring to the number of parameters.

# Method named sum, which should take at least one parameter, and at most three, and perform the sum between them, and returns the result
# EX INPUT: 5
# EX OUTPUT: 5
# EX2 INPUT: 2, 4
# EX2 OUTPUT: 6
# EX3 INPUT: 1, 2, 3
# EX3 OUTPUT: 6

class classSum:
    def sum(self, x, y = 0, z = 0):
        return x + y + z

obj1 = classSum()
print(obj1.sum(1))