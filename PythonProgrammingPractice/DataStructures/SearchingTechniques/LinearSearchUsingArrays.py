def LinearSearch(elements, searchval):
    for i, j in enumerate(elements): # Enumerate gives the index and value, so there are two variables (if just one, then it will be a tuple)
        if j == searchval: # j is the value
            return i # i is the index
    return -1 # If the element isn't found, we need to return -1

elements = [7, 9, -1, 3, 0, 22, 41, 67]
search_val = int(input("Enter a number: "))
print(LinearSearch(elements, search_val))