from typing import List, Union

list1: List[Union[int, int, str, float, bool]] = [1, 2, "string", 3.14, True]
tuple1 = (3, 1, 81, 34)
str1 = "This is a sentence."

# print(list1[::-1])
# print(tuple1[::-1])
# print(str1[::-1])

rev = slice(None, 3, -1)     # The advantage with the slice object is that you can change everything from one place.
print(list1[rev])
print(tuple1[rev])
print(str1[rev])