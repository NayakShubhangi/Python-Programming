list1 = [25, "string", True, 83.468, 3.14159, 4, 5, 9]
list2 = ["text", False, 1.8, "str", 543, 2, 89]

# Get a separate list which should contain tuples:
# the tuples should have the values which have the same index
# [(25, "text"), ("string", False)...]

list3 = []
for i in range(max(len(list1), len(list2))):
    if i >= len(list1):
        list3.append((list2[i],))
    elif i >= len(list2):
        list3.append((list1[i],))
    else:
        list3.append((list1[i], list2[i]))

# print(list3)


# Only works with an even number of elements
print(list(zip(list1, list2)))

# TASK THREE: (DONE)
# Find the key differences between pass keyword and ellipsis keyword.
# Pass: Used as a placeholder where a statement is required, but you don't want to execute any code yet.
# Ellipsis: Used as an placeholder to show that the section is going to be implemented soon, but it hasn't been done at the moment.

# DIFFERENCE: Pass is a statement while Ellipsis is an object/instance of the ellipsis class.
# Pass is usually used as a placeholder for empty pieces of code, while ellipsis is usually used as a placeholder with "to be filled",
# type hinting, slicing. Pass has no value, while ellipsis refers to the ellipsis object.


# TASK FOUR: (DONE)
# Try to get some high-level view of natural language processing (NLP).
# *brief* understanding
