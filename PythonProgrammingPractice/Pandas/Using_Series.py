# Series is like a table in pandas
# It's a one dimensional array holding data of any type
import pandas as pd

# print(pd.__version__)
list1 = [6, 1, 5, 2, 4, 3]
myseries = pd.Series(list1)
# print(myseries[3])
list2 = [2, 9, 4, 7, 1]
myseries2 = pd.Series(list2, index=["a", "b", "c", "d", "e"])
# print(myseries2["b"])
dict1 = {
    "One" : 1,
    "Two" : 2,
    "Three" : 3
}
myseries3 = pd.Series(dict1)
print(myseries3)