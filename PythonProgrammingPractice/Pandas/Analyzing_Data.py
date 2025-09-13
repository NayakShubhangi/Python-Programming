import pandas as pd

dict1 = {
    "Colors" : ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Brown", "Black"],
    "Numbers" : [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Letters": ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
}
myDf1 = pd.DataFrame(dict1)
# print(myDf1.head(8))
# The default record retrival count will always be five when we use head(), unless you specify otherwise
# head() works with the top-down approach as it retreives values
# print(myDf1.tail())
# Similar to head(), tail() will always retreive 5 values, unless you specify otherwise
# tail() works with the bottom-up approach as it retrieves values
# print(myDf1.tail(9))
# print(myDf1.info())

# make a dataframe, but exclude "books" WIHOUT USING ANOTHER DATAFRAME
dict2 = {
    "Users" : ["Bob", "Tom", "Alice", "Jerry", "Max"],
    "Items" : ["Pencil", "Eraser", "Pen", "Ruler", "Tape"],
    "Books" : [1, 2, 3, 4, 5]
}
myDf3 = pd.DataFrame(dict2, columns=["Users", "Items"])
print(myDf3)

dict3 = {
    "Day1" : "Sunday",
    "Day2" : "Monday",
    "Day3" : "Tuesday"
}
myseries1 = pd.Series(dict3, index=["Day1", "Day2"])
print(myseries1)