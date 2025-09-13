# Create a class Property with the below attributes:

# property_type -> String(house/land/real estate etc)
# property_value -> Number
# max_bid_price -> Number
# where property_type attribute is the type of property(like house/land/real estate etc) is unique, property_value attribute is the base price of the property and max_bid price attribute is the value for maximum bidding price.
# Assume, max_bid_price > property_value
# Create the __init__ method which takes as an argument the value for 3 attributes in the above sequence to initialize the attributes of the object created.
class Property:
    def __init__(self, property_type, property_value, max_bid_price):
        self.property_value = float(property_value)
        self.max_bid_price = float(max_bid_price)
        if self.max_bid_price <= self.property_value:
            raise ValueError("Max_bid_price should be greater than Property_value")
        self.property_type = str(property_type)

# Create a class Tender with the below attributes:

# buyerName -> String
# propertyType -> String
# bidPrice -> Number
# where buyerName attribute represents the name of the buyer, propertyType attribute represents the type of the property and bidPrice attribute represents the biding price.

# Create the __init__ method which takes as an argument the value for these attributes in the above sequence and initializes the attributes of the object created.

# Define the function – bidProperty. This function is not part of any class. This function will take as input parameters- a list of Property objects and a list of Tender objects.
# The function will check for each Tender in the list passed as the second argument the validity and return the names of the buyer’s in a list for all valid Tenders. If no valid Tender found, the function returns an Empty list.

# A Tender is considered valid only if the allowing conditions are fulfilled:

# The Property for the given property type in the Tender must be present in the Property list passed as first argument.
# For a given property type, only the Tender with the highest bidPrice will be considered (e.g in the list of Tenders if there are 3 Tender objects with property Type ‘land’ and the bid price 40000,50000 and 60000 respectively. In that case, the Tender with a bid price of 60000 will be considered).
# The bid price given in the Tender can not be lower than the property_value and higher than the max_bid price of the Property found.
# The function will remove the Property from the Property list passed as the first argument which fulfills the conditions 1 and 3 mentioned above (which is considered for bidding) and update the list.

# Note:

# Assume no two property in the Property list passed as the first argument to the function can have same property_type
# All the string comparisions are case insensitive
# This function should be called from the main section.
# Instructions to write the main section of the code:

# a) You would require to write the main section completely, hence please follow the below instructions for the same
# b) You would require to write the main program which is in line to the “sample input description section” mentioned below and to read the data in the same sequence.
# c) Create the respective object(Property and Tender) with the given sequence of arguments to fulfill the __init__ method requirement defined in the respective classes referring to the below instructions.

# 1) Create a list of Property objects which will be provided to the bidProperty function as the first argument.
# a) Read a number for the count of Property objects to be created and added to the list.
# b) Create a Property object after reading the data related to it and add the object to the list of Property objects. This point repeats for the number of Property objects (considered in the first line of input) point #c.1.a
# 2) Create a list of Tender objects which will be provided to the bidProperty function as the second argument
# a) Read a number for the count of Tender objects to be created and added to the list.
# b) Create a Tender object after reading the data related to it and add the object to the list of Tender objects. This point repeats for the number of Tender objects (considered in the first line of input) point #c.1 a
# c) Call the function bidProperty by passing the lists created in point #c.1 and #c.2 respectively.
# d) Print the names from the list returned by the function bidProperty. If the function returns Empty list, print “Property Not found” exluding the quotes
# e) Print the types of Property (property type) from the Property list updated by the function bidProperty.
# You can use/refer the below-given sample input and output to verify your solution using Test against Custom Input
# Sample Input (below) description:

# a. The 1st input taken in the main section is the number of Property objects to be added to the list of PropertyDealer.
# b. The next set of inputs are the property_type, property_value, max_bid_price for each Property object taken one after other and is repeated for number of Property objects given in the first line of input
# c. The next line of input is the count of Tender objects to be added to the list of Tender objects to be passed as argument to the bidProperty function.
# d. The next set of inputs are the are the values buyerName, property_Type and bidPrice for each Tender object taken one after other and is repeated for number of Tender objectsetiven in the point #c.