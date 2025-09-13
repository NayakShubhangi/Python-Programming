# TASK THREE
# Create a class DairyProduct with bellow attributes:
# dairyId -> Number
# dairyBrand -> String
# productType -> String
# price -> Number
# grade -> String
# Define the __init__ method which takes parameters in above sequence and sets the values frot he attributes dairyId, dairyBrand, productType, price, and grade.
# Create another class ProductGrade with attribute as below:
# dairyList -> list, which has List of DairyProduct Objects
# weightageDict -> dictionary, with grade as key and weightage as value where each key represents a distinct grade and value represents weightage tagged to that grade denoted by the key.
# (grade: weightage)
# For eg:
# Grade1: 20
# Grade2: 10
# Grade3: 5
# Define the __init__ method to initialize the attributes in the above sequence.
# Create another method inside the class with the name priceBasedOnBrandAndType.
# The method takes two arguments-
# 1. A string value depicting dairy brand as the 1st argument.
# 2. A string value depicting product type as the 2nd argument.
# From the dairyList of the ProductGrade, the method will find all dairy products having dairyBrand and producttype values same as the values
# passed as arguments.
# Method will calculate the updated price for all these DairyProduct and update the price value with the calculated price.
# The value for the weightage corresponding to the grade available for the dairy Product is found from the weightageDict of the ProductGrade and
# this eightage value is used to calculate the updated price.
# Updated Price is calculated using the below formula:
# updatedPrice=price+price*weightage/100
# For example:
# If the grade of dairyProduct is Grade2, then from the weightageDict of ProductGrade, the weightage for the grade will be fetched. Assume if
# price is 250 and weightage is 10 then
# updatedPrice=250+250*10/100=275
# If no dairy Product having the given dairy brand and product type is available, method will return None.
# Note: All string comparisons should be case insensitive.
# Instructions to write main section of the code:
# a. You would require to write the main section completely, hence please follow the below instructions for the same.
# b. You would require to write the main program which I inline to the “sample input description section” mentioned below and to read the data
# in the same sequence.
# c. Create the respective objects (DairyProduct and ProductGrade) with the given sequence of arguments to fulfill the __init__ method requirement
# defined in the respective classes referring to the below instructions.
# i. Create a list DairyProducts. To create the list
# 1. First read the number of DairyProduct you want to store in the list.
# 2. Read the values for the DairyProduct, create the DairyProduct object and add to the list. This point repeats for the number of DairyProduct
# objects (consider the input taken in point # above) to be created.
# a. First read the id of the DairyProduct.
# b. Then read the brand of DairyProduct, producttype, price, and grade.
# c. Then, read the number representing the count of dictionary elements.
# d. Read key and value representing the weightageDict elements and add to the dictionary. This point repeats for the count taken in point #2.c
# above.
# ii. Create ProductGrade object by passing the dairyList (a list of DairyProduct objects created as mentioned in point #2) and weightageDictionary
# as the arguments to the constructor.
# iii. Read values for dairyBrand and producttype to be passed as argument to the method priceBasedOnBrandAndType.
# iv. Call the method priceBasedOnBrandAndType from the main section. Display the dairyBrand and price of the dairyProduct returned by the method
# separated by “:”. If None is returned by the method, then display the message ‘No dairy product found’ (excluding the quotes).
class DairyProduct: 
    def __init__(self, dairyId, dairyBrand, productType, price, grade):
        self.dairyId = dairyId
        self.dairyBrand = dairyBrand
        self.productType = productType
        self.price = price
        self.grade = grade

class ProductGrade:
    def __init__(self, dairyList, weightageDict):
        self.dairyList = dairyList
        self.weightageDict = weightageDict
        
    def priceBasedOnBrandAndType(self, dairyBrand, productType):
        dairyBrand = dairyBrand.lower()
        productType = productType.lower()
        updated_products = []
        for dairyProduct in self.dairyList:
            if dairyProduct.dairyBrand.lower() == dairyBrand and dairyProduct.productType.lower() == productType:
                weightage = self.weightageDict.get(dairyProduct.grade, 0)
                if weightage != 0:
                    dairyProduct.price = dairyProduct.price + (dairyProduct.price * weightage) / 100
                    updated_products.append(dairyProduct)
        if updated_products:
            return updated_products
        else:
            return None


num_products = int(input())
dairyList = []
for i in range(num_products):
    dairyId = int(input())
    dairyBrand = input()
    productType = input()
    price = float(input())
    grade = input().lower()
    
    obj = DairyProduct(dairyId, dairyBrand, productType, price, grade)
    dairyList.append(obj)

weightageDict = {}
dict_count = int(input())
for i in range(dict_count):
    grade = input().lower()
    weightage = int(input())
    weightageDict[grade] = weightage

obj = ProductGrade(dairyList, weightageDict)
dairyBrand = input()
productType = input()
new_price = obj.priceBasedOnBrandAndType(dairyBrand, productType)

if new_price:
    for i in new_price:
        print(f"Dairy Brand: {i.dairyBrand}")
        print(f"Price: {i.price:.2f}")
else:
    print("No dairy product found")

# FIXED: Instead of accessing i[0] and i[1], we now use the attributes of DairyProduct objects i.dairyBrand and i.price

# c. Create the respective objects (DairyProduct and ProductGrade) with the given sequence of arguments to fulfill the __init__ method requirement
# defined in the respective classes referring to the below instructions.
# i. Create a list DairyProducts. To create the list
# 1. First read the number of DairyProduct you want to store in the list.
# 2. Read the values for the DairyProduct, create the DairyProduct object and add to the list. This point repeats for the number of DairyProduct
# objects (consider the input taken in point # above) to be created.
# a. First read the id of the DairyProduct.
# b. Then read the brand of DairyProduct, producttype, price, and grade.
# c. Then, read the number representing the count of dictionary elements.
# d. Read key and value representing the weightageDict elements and add to the dictionary. This point repeats for the count taken in point #2.c
# above.
# ii. Create ProductGrade object by passing the dairyList (a list of DairyProduct objects created as mentioned in point #2) and weightageDictionary
# as the arguments to the constructor.
# iii. Read values for dairyBrand and producttype to be passed as argument to the method priceBasedOnBrandAndType.
# iv. Call the method priceBasedOnBrandAndType from the main section. Display the dairyBrand and price of the dairyProduct returned by the method
# separated by “:”. If None is returned by the method, then display the message ‘No dairy product found’ (excluding the quotes).