# Dataframes are two dimensional structures or two-dimensional arrays or tables with rows and columns
import pandas as pd

dict1 = {
    "Colors" : ["Red", "Blue", "Green", "Yellow"],
    "Numbers" : [2, 5, 8, 3]
}
myDf = pd.DataFrame(dict1)
# print(myDf)

dict2 = {
    "Letters": ["a", "b", "c", "d", "e"],
    "Numbers" : [1, 4, 6, 9, 0]
}
myDf2 = pd.DataFrame(dict2, index=["A", "B", "C", "D", "E"])
# print(myDf2)
# print(myDf2.loc["A"])

dict3 = {
    "Colors" : ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Brown", "Black"],
    "Numbers" : [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Letters": ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
}
myDf3 = pd.DataFrame(dict3)
print(myDf3)