# By default, Python doesn't support abstraction.
# Need to use an external module (abc) to utilize abstraction.
# If a class contains an abstract method in it, then we call it as an abstract class.
# If you call an abstract method with no definition but only a declaration, it throws an error:
# TypeError: Can't instantiate abstract class *NAME OF CLASS* without an implementation for abstract method '*NAME OF METHOD*'
# Using abstraction, we are establizhing a layered way of security, where the first layer acts as a declaration, and
# the second layer acts as a definition.

from abc import ABC, abstractmethod


class abstraction(ABC):
    @abstractmethod
    def getter(self):
        pass

class postabstraction(abstraction):
    def getter(self):
        print("This is from postabstraction class.")

obj1 = postabstraction()
obj1.getter()