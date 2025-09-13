# Create a class Painting with the below attributes:
# paintingID: string type
# painterName: string type
# paintingPrice: int type
# painting type: string type
class Painting:
    def __init__(self, paintingID, painterName, paintingPrice, paintingType):
        self.paintingID = paintingID
        self.painterName = painterName
        self.paintingPrice = paintingPrice
        self.paintingType = paintingType


# create constructor (__init__ method) which takes all the above attributes in the same sequence.
# Method will set the values passed as an argument to the attributes of the Painting object created.
class ShowRoom:
    def __init__(self, paintingList):
        self.paintingList = paintingList
    
    def getTotalPaintingPrice(self, pType):
        pPrice = 0
        flag = False
        for obj in self.paintingList:
            if obj.paintingType == pType:
                flag = True
                pPrice += obj.paintingPrice
        if flag == False:
            return None
        return pPrice
    
    def getPainterWithMaxCountOfPaintings(self):
        names = []
        name_count = {}
        for obj in self.paintingList:
            result = name_count.get(obj.painterName, "not found")
            if result != "not found":
                name_count[obj.painterName] += 1
            else:
                name_count[obj.painterName] = 1
        sorted_list = sorted(name_count.items(), key=lambda x: x[1], reverse=True)
        maxNum = sorted_list[0][1]
        for i in range(len(sorted_list)):
            if sorted_list[i][1] == maxNum:
                names.append(sorted_list[i][0])
        names = sorted(names)
        return names[0]
        

# Create a class ShowRoom with the attribute as a list of paintings obtained from the main function.
# paintingList: of type List of Painting objects.

# Define two methods inside ShowRoom class.
# getTotalPaintingPrice: It takes a string representing the painting type as argument, and returns the total painting price of the paintings of the given type from the paintingList of the ShowRoom. If no paintings of the given type is present in the list then the method returns None.
# getPainterWithMaxCountOfPaintings: It finds the name of the painter from the paintingList of the ShowRoom who has the highest count of Paintings. If more than one painter has the highest count of paintings, the method returns the name of the painter whose name comes first as per the alphabetical orders(A-Z).


count = int(input())
paintingList = []
for i in range(count):
    paintingID = int(input())
    painterName = input().lower()
    paintingPrice = int(input())
    paintingType = input().lower()

    paintingObj = Painting(paintingID, painterName, paintingPrice, paintingType)
    paintingList.append(paintingObj)

showroomObj = ShowRoom(paintingList)
pType = input().lower()
totalPrice = showroomObj.getTotalPaintingPrice(pType)
maxPainting = showroomObj.getPainterWithMaxCountOfPaintings()
if totalPrice:
    print("\n")
    print(totalPrice)
else:
    print("Painting not found")

print(maxPainting)



# Instructions to write the main function:
# a. You would require to write the main section completely. Hence please follow the below instructions for the same.
# b. You would require to write the main program which is inline to the “sample input description section” mentioned below and to read the data in the same sequence.
# c. Create the respective objects(Painting and ShowRoom) with the given sequence of arguments to fulfill the __init__ method as mentioned in requirements, defined to the respective classes referring to the below instructions.

# i) Create a list of Painting objects which will be passes as argument while calling the functions in main. To create the list,
# a. Read a number for the count of Painting objects to be created and added to the list.
# b. Create a Painting object after reading the data related to it and add the objects to the list to be created. This points repeats for the number of Paintings object to be created(considered in the first line of input) as per point #c.i.a
# ii) Create the ShowRoom object by passing the list created in point #c.i
# d. Read a value for painting type to be passed as argument to the method getTotalPaintingPrice.
# e. Call the method getTotalPaintingPrice by passing the value read in point #d.
# f. Call the method getPainterWithMaxCountOfPaintings.
# g. Display the value returned by the method getTotalPaintingPrice. If function return None,Then display “Painting not found”(excluding the quotes).
# h. Display the value returned by the method getPainterWithMaxCountOfPaintings.
# You can use/refer the below-given sample input and output for more details of the format for input and output.
# Sample Input description:
# a) First line represents the integer value which represents the number of Painting objects.
# b) Next lines of input represents one Painting specific data as below one by one in each line.

# paintingId
# paintingName
# paintingPrice
# paintingType
# c) The points #b repeats for the number of objects mentioned in the point #a.
# d) The last line of input is the painting type to be passed as argument to the method getTotalPaintingPrice.

# Consider Case Insensitive for this problem statement.


# INPUT:
# 5
# 101
# Raman
# 50000
# portrait
# 102
# kamaal
# 30000
# portrait
# 103
# Raman
# 25600
# modern
# 104
# sumiran
# 31000
# landscape
# 105
# sumiran
# 50000
# Modern
# Modern

# OUTPUT:
# 75600
# raman