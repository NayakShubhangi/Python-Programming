list1 = [1, 2, 3, 4, 5]
list1.append([6, 7])     # Append "appends" the values in an iterable format
print(list1)
# [1, 2, 3, 4, 5, [6, 7]]
list2 = [5, 6, 7, 8, 9]
list2.extend([10, 11])     # Extend picks up the variables and adds them to the list without the iterable formatting
print(list2)
# [5, 6, 7, 8, 9, 10, 11]


list1.append(["Bob"])
print(list1)
# [1, 2, 3, 4, 5, [6, 7], ["Bob"]]
list2.extend(["Mary"])
print(list2)
# [5, 6, 7, 8, 9, 10, 11, "Mary"]


list1.append("Bob")
print(list1)
# [1, 2, 3, 4, 5, [6, 7], ["Bob"], "Bob"]
list2.extend("Bob")
print(list2)
# [5, 6, 7, 8, 9, 10, 11, "Mary", "B", "o", "b"]
# # Note: Strings are iterables, so .extend() has to separate it



groceries = ['milk', 'eggs']
extras = ['bread', 'butter']
groceries.append(extras)
extras.extend(['jam', 'honey'])  # Since groceries references extras, the nested list that is extras will be extended with these values
groceries[2].append('cheese')    # Appends to index of 2, which is the nested list
groceries.extend(['apples', 'bananas'])
print(groceries)
# ["milk", "eggs", ["bread", "butter", "jam", "honey", "cheese"], "apples", "bananas"]