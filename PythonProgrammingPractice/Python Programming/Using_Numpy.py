# Numpy is a Python library that helps us to work with arrays
# Also referred to as Numerical Python
# Created in 2005
# Arrays are faster, which make them more preferred to use over lists sometimes

# Comparison between arrays and lists
# list1 = [-1, "string", 83, 20]
# list2 = [5, 2, 19, -4]
# # The location of the values in a list are kind of scattered, which makes retrieving it slightly slower
# print(id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]))
# # The location of the values in an array, on the other hand, are simultanious, which makes retrieving it faster than lists
# print(id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]))
# Arrays can take only one type of value, while lists can take more than one type

import numpy as np

# print(np.__version__)  # 2.1.2
# When we see the type of an array, we see that it is a 'numpy.ndarray'
# nd stands for ndimensional array
# ndimensional is like a nested list
# array1 = np.array([4, -2, 6, -8, 3.14159])
# When a string is included in an array with other types of values, the array assumes that everything is a string, and converts them into strings
# When a float is included in an array with other types of values, the array assumes that everything is a float, and converts them into floats
# and assumes that each 'float' has the same number of numbers after the decimal as the first float that started it, and gives that much space

# array2 = np.array(42)
# When we don't include the square brackets, it becomes a ZERO DIMENSIONAL ARRAY
# similar to list1 = list(3, 4)

# 1-D array is an array that has 0-D arrays as its elements (An array in an array) (the default, basically)
# array3 = np.array([1, 2, 3])

# 2-D array is an array that has 1-D arrays as its elements (Another array in an array)
# array4 = np.array([[5, 3, 7], [9, 2, 6]])

# 3-D array is an array that has 2-D arrays as its elements (Yet another array in an array)
# array5 = np.array([[[2, 8, 5], [0, 1, 6]], [[2, 8, 5], [0, 1, 6]]])
# ndimension means that it can have n dimensions, so it is infinite

# Using ndmin, we can make a 4-D array, which has FOUR brackets in a basic way
# array6 = np.array([1, 2, 3, 4], ndmin=4)
# print(array6)

array7 = np.array([2, 3, 4, 7, 5])   # This 1-D has 1 row, 5 columns
# print(array7[0])     # Supports indexing, just like lists

# print(array1.ndim)
# print(array2.ndim)
# print(array3.ndim)
# print(array4.ndim)
# print(array5.ndim)
# print(array6.ndim)

array8 = np.array([[8, 3, 5, 1, 4], [2, 3, 4, 5, 6]])    # This 2-D has 2 rows, 5 columns
# print(array8[0][1])
# print(array8[0, 1])
# Both do the same thing

array9 = np.array([[9, 3, 5, 2, 4], [2, 25, 86, 5, 6]])
# print(array9[1][2])
# print(array9[1, 2])

array9 = np.array([[[9, 3, 5], [2, 4, 3]], [[2, 25, 86], [5, 6, 9]]])
# print(array9[0][1][2])
# print(array9[0, 1, 2])

array1 = np.array([[2, 3, 4, 5, 6], [1, 7, 8, 9, 0]])
# print(array1[1, 1:4])
# [7, 8, 9]
# print(array1[0:2, 1:4])
# [3, 4, 5], [7, 8, 9]

array10 = np.array([[4, 7, 8, 2], [1, 0, 9, 3]])
array11 = np.array([[4, 7, 8, 2]])
# print(array10.ndim)
# print(array11.ndim)

# COPY IN ARRAYS
# Copy simply copies the array, then becomes independent of it
array12 = np.array([1, 2, 3, 4, 5])
array13 = array12.copy()
array12[0] = 6
# print(array12)
# print(array13)

# VIEW IN ARRAYS
# View is like a reflection of the array it is copying, so it will change along with the original
array14 = np.array([7, 8, 9, 0, 1])
array15 = array14.copy()
array16 = array14.view()
array14[2] = 6
# print(array14)
# print(array15)
# print(array16)

# Base is an attribute that tells whether it is a copy or view
# If it is a copy or original array, it will return None
# If it is a view, it will return the array that it is copying
# print(array15.base)
# print(array16.base)
# print(array14.base)

# SHAPE IN ARRAYS
# Returns a tuple that tells how many dimensions it consists of starting from each level
# Evaluates the top-level to the deep-level of how many elements there are

array17 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(array17.shape)

# ndmin is an argument that is used to specify what dimension you want to make an array as
array18 = np.array([1, 2, 3, 4], ndmin=5)
# print(array18)
# print(array18.shape)

array19 = np.array([[2, 3, 4, 5], [6, 7, 8, 9], [0, 1, 23, 45]])
# print(array19.shape)
# print(array19.ndim)

array20 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(help(array20.shape))
# print(array20.ndim)

array21 = np.array([[[[[3, 9, 10], [9, 10, 11]]]]])
# 1, 1, 1, 2, 3
# print(array21.shape)

array22 = np.array([(1, 2), (3, 4), (5, 6), (7, 8)])
# 4, 2
# print(array22.shape)

# USING RESHAPE
# reshape is used to 'reshape' an existing array to another dimensional array by specifying the shape
array23 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
array24 = array23.reshape(4, 3)
# array24 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# print(array23)
# print(array24)
array25 = array23.reshape(2, 3, 2)
# array25 = [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]
# print(array23)
# print(array25)
# for i in array25:
#     print(i)

# ARRAY SPLITTING
# array_split() is used to split one array into multiple arrays
array26 = np.array([1, 2, 3, 4, 5, 6])
array27 = np.array_split(array26, 3)
# print(array26)
# print(array27)

# SEARCHING ARRAYS
# where() is used to search an array for a certain value and returns the index of the match(es)
# It returns a tuple which consists of indexes of the match(es)
array28 = np.array([1, 2, 2, 5, 4, 5, 7, 5])
x = np.where(array28 % 2 == 0)
# print(x)

# SEARCH SORTED
# searchsorted() is used to perform a binary search on a SORTED array and returns the index where the specified value would be
# inserted to maintain the search order
# searchsorted() 
array29 = np.array([2, 3, 3, 4])
y = np.searchsorted(array29, 5)
# print(y)

array30 = np.array([2, 2, 4, 5, 7, 8, 8, 11, 15, 16])
z = np.searchsorted(array30, 8)
# print(z)