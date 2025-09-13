def BinarySearch(elements, searchval):
    left = 0
    right = len(elements) - 1
    while left <= right:
        mid = (left + right) // 2
        if elements[mid] == searchval:
            return mid
        elif elements[mid] > searchval:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# elements = [-3, -1, 0, 19, 26, 34, 58, 71, 96]
# search_val = int(input("Enter a number: "))
# print(BinarySearch(elements, search_val))
# left = 0, right = 8, mid = 4
# left = 0, right = mid - 1 = 3, mid = 2
# left = 0, right = mid - 1 = 1, mid = 1
# left = 0, right = mid - 1 = 0, mid = 0

# left = 0, right = 8, mid = 4
# left = mid + 1 = 5, right = 8, mid = left + right + 1 // 2 = 5 + 8 + 1 // 2 = 7
# left = mid + 1 = 8, right = 8, mid = 8

# TASK ONE: -Fixed-
# For some reason, mid = 9 in the end, which causes an error since there isn't a 9th index. fix that.

# TASK TWO:
# Make a function that performs binary search as shown above, but using recursion.
def BinarySearch_Recursive(elements, searchval, left, right):
    if left > right:
        return -1
    mid = left + right // 2
    if elements[mid] == searchval:
        return mid
    elif elements[mid] > searchval:
        return BinarySearch_Recursive(elements, searchval, left, mid - 1)
    else:
        return BinarySearch_Recursive(elements, searchval, mid + 1, right)

def Binary_Search(elements, searchval):
    return BinarySearch_Recursive(elements, searchval, 0, len(elements) - 1)

elements2 = [-13, -8, 1, 8, 16, 32, 49, 73, 89]
search_val2 = int(input("Enter a number: "))
print(BinarySearch(elements2, search_val2))

# TASK THREE:
# Make a function that does linear search for (normal) queues or stacks.
# NOTE: Code has been moved to QueueUsingArrays.py

# TASK FOUR:
# Find out how to calculate the space complexity of a program. -> Couldn't find.
# Denotions:
# O(1): Constant time.
# O(log n): Logarithmic time.
# O(n): Linear time.
# O(n log n): Log-linear time.
# O(n^2): Quadratic time.
# O(2^n): Exponential time.
# O(n!): Factorial time.