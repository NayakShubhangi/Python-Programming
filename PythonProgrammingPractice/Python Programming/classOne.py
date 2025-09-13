# class one:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.x = 100
#         self.name = "bob"
    
#     def methodOne(self):
#         print(self.first, self.last)
#         print(self.x, self.name)

# var = one("Shubhangi", "Nayak")
# var.methodOne()
# var.x = 10
# var.name = "Pari"
# var.methodOne()


# Make a class and constructor with variable "x" that has a list in it
# Loop through all elements in the list, and print only the elements that have at least 4 letters


class two:
    def __init__(self, x):
        self.x = x
    
    def methodSort(self):
        for i in range(len(self.x)):
            if len(self.x[i]) >= 4:
                print(self.x[i])

varTwo = two(["Two", "Three", "Seven", "Six", "Bike"])
varTwo.methodSort()