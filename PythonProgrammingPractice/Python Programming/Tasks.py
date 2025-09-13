# EX: Haae -> Hae
# Use lambda to replace input that starts with h and ends with e with the same string, but removes the second to last character
replace_h_e = lambda i: i[:-2] + i[-1] if i.startswith('h') and i.endswith('e') else i
string1 = "Haae"
result = replace_h_e(string1)
print(result)

# EX: (1, 2, 3), (3, 6, 4) -> (1, 2, 3, 3, 6, 4)
# Use map() and lambda to concatenate two tuples
tuple1 = (1, 2, 3)
tuple2 = (3, 6, 4)
concatenate_tuples = lambda t1, t2: t1 + t2
result = tuple(map(lambda i: i, [concatenate_tuples(tuple1, tuple2)]))
print(result[0])

# EX: "Apple" -> (z)...pple
# Pick up each character in the string and replace each with its reverse character
# If uppercase letter, replace with reverse uppercase letter
# If lowercase letter, replace with reverse lowercase letter
# Make it functional for sentences as well
# (if a, then reverse char is z)
reverse_char = lambda i: chr(219 - ord(i)) if 'a' <= i <= 'z' else (chr(155 - ord(i)) if 'A' <= i <= 'Z' else i)
transform_string = lambda s: ''.join([reverse_char(c) for c in s])
string2 = "Apple"
result = transform_string(string2)
print(result)