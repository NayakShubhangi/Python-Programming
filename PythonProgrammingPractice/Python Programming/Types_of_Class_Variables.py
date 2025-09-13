# Instance variable, class variable or static variable
# Instance Variable
# Instance variable is self.name
class amazon:
    def __init__(self):
        self.name = "Bob"
    
    def write(self):
        print(self.name)

# obj = amazon()
# obj.write()

# Class Variable / Static Variable
class flipkart:
    brand = "shopping"
    def __init__(self):
        self.name = "Bob"

    @classmethod
    def thing(cls):
        print(cls.brand)

obj2 = flipkart()
# obj2.thing()
# flipkart.thing()
print(obj2.brand)
print(flipkart.brand)