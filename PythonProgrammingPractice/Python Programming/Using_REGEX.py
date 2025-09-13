# A module and is a sequence of characters that form a search pattern
# Can be used to check if a string contains the specific search pattern
# Metacharacters: Has a special meaning and help to evaluate a pattern

import re

# s = "This is a string sentence."
# n = re.search("^This", s)
# x = re.search("sentence$", s)
# print(bool(n))
# print(bool(x))
m = "The forest in the globe consists 80%."
x = re.findall("[a-e]", m)
print(x)