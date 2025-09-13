import sys
import math


# print(len(sys.argv))
# print(sys.argv[0])    # Prints filename
# n = len(sys.argv)
# for i in range(1, n):
#     print(sys.argv[i])


def lowestnum(x, y, z):
    var = min(x, y, z)
    return var


if len(sys.argv)!=4:
    print("You can only enter 3 values")
else:
    print(lowestnum(sys.argv[1], sys.argv[2], sys.argv[3]))