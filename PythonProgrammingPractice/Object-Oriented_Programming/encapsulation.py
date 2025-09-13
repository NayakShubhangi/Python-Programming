# Encapsulation is a way to make methods or variables as private inside a class.
# Helps to implement security and unauthorization layering
# _ makes it protected, but not private, so while it warns users not to change it, it can still be changed.
# __ makes it private. It can no longer be changed by the user.

class encapsulation:
    def __init__(self):
        print("This is inside the encapsulation constructor.")
        # This is a private variable as it starts with __.
        self.__var = 100

    def getter(self):
        print(self.__var)


# obj1 = encapsulation()
# obj1.getter()

# How to make a method private
class privateMethod:
    def __init__(self, x):
        self.x = x
    
    def publicGetter(self):
        print("This is public getter method.")
        self.__privateGetter()
    
    def __privateGetter(self):
        print("This is private getter method.")

obj2 = privateMethod(8)
obj2.publicGetter()